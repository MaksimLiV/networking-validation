import ipaddress
import requests
import socket
import subprocess
from behave import given, then


@given("I retrieve the public IP address")
def step_retrieve_public_ip(context):
    try:
        response = requests.get("https://ipinfo.io/ip", timeout=5)
        response.raise_for_status()
        context.public_ip = response.text.strip()
    except requests.RequestException as e:
        raise AssertionError(f"Failed to retrieve public IP: {str(e)}")


@then('the IP should not be in range "{start_ip}" to "{end_ip}"')
def step_validate_ip_range(context, start_ip, end_ip):
    try:
        ip = ipaddress.ip_address(context.public_ip)
        start = ipaddress.ip_address(start_ip)
        end = ipaddress.ip_address(end_ip)

        if start <= ip <= end:
            raise AssertionError(
                f"Public IP {context.public_ip} falls within restricted range {start_ip} - {end_ip}"
            )
    except ValueError as e:
        raise AssertionError(f"Invalid IP address format: {str(e)}")


@given('I resolve the domain "{domain}"')
def step_resolve_domain(context, domain):
    try:
        context.resolved_ip = socket.gethostbyname(domain)
    except socket.gaierror as e:
        raise AssertionError(f"Failed to resolve domain {domain}: {str(e)}")


@then('the IP address should be "{expected_ip}"')
def step_validate_resolved_ip(context, expected_ip):
    if context.resolved_ip != expected_ip:
        raise AssertionError(
            f"Domain resolved to {context.resolved_ip}, expected {expected_ip}"
        )


@given('I perform a traceroute to "{target}"')
def step_perform_traceroute(context, target):
    try:
        if subprocess.getoutput("which traceroute") == "":
            raise AssertionError("Traceroute command not found")

        cmd = ["traceroute", "-m", "10", "-n", target]
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()

        if process.returncode != 0:
            raise AssertionError(f"Traceroute failed: {error.decode()}")

        context.traceroute_output = output.decode().split("\n")

    except subprocess.SubprocessError as e:
        raise AssertionError(f"Traceroute execution failed: {str(e)}")


@then("the target should be reached within {max_hops:d} hops")
def step_validate_traceroute_hops(context, max_hops):
    if not context.traceroute_output or len(context.traceroute_output) > max_hops:
        raise AssertionError(f"Target not reached within {max_hops} hops")
