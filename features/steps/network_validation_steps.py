from behave import given, then
import requests
import socket
import subprocess
import ipaddress


# Step 1: Retrieve Public IP
@given('I retrieve my public IP address')
def step_impl(context):
    try:
        response = requests.get("https://ipinfo.io/ip")
        context.public_ip = response.text.strip()
    except Exception as e:
        context.public_ip = None
        print(f"Error retrieving public IP: {e}")

# Step 2: Validate Public IP Range
@then('My public IP should not fall within the range "{start_ip}" to "{end_ip}"')
def step_impl(context, start_ip, end_ip):
    if context.public_ip:
        ip = ipaddress.ip_address(context.public_ip)
        start = ipaddress.ip_address(start_ip)
        end = ipaddress.ip_address(end_ip)
        if start <= ip <= end:
            raise AssertionError(f"Public IP {context.public_ip} falls within the restricted range.")
        else:
            print(f"Public IP {context.public_ip} is outside the restricted range.")
    else:
        raise AssertionError("Failed to retrieve public IP.")

# Step 3: Verify Domain Resolution
@given('I resolve the domain "{domain}"')
def step_impl(context, domain):
    try:
        resolved_ip = socket.gethostbyname(domain)
        context.resolved_ip = resolved_ip
    except socket.gaierror:
        context.resolved_ip = None
        print(f"Error resolving domain: {domain}")

@then('The resolved IP address should be "{expected_ip}"')
def step_impl(context, expected_ip):
    if context.resolved_ip != expected_ip:
        raise AssertionError(f"Expected IP {expected_ip}, but got {context.resolved_ip}")
    else:
        print(f"Domain {context.resolved_ip} correctly resolves to {expected_ip}.")

# Step 4: Perform Traceroute
@given('I perform a traceroute to "{target_ip}"')
def step_impl(context, target_ip):
    try:
        result = subprocess.run(['traceroute', target_ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = result.stdout.decode()
        context.hops = output.count("\n")
    except Exception as e:
        context.hops = None
        print(f"Error performing traceroute: {e}")

@then('The traceroute should complete within {max_hops} hops')
def step_impl(context, max_hops):
    if context.hops and context.hops <= int(max_hops):
        print(f"Traceroute completed in {context.hops} hops.")
    else:
        raise AssertionError(f"Traceroute exceeded {max_hops} hops, actual hops: {context.hops}")