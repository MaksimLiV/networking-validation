Feature: Network Validation

  Scenario: Retrieve and validate the public IP
    Given I retrieve my public IP address
    Then My public IP should not fall within the range "101.33.28.0" to "101.33.29.255"

  Scenario: Verify domain resolution
    Given I resolve the domain "google-public-dns-a.google.com"
    Then The resolved IP address should be "8.8.8.8"

  Scenario: Perform traceroute to 8.8.8.8
    Given I perform a traceroute to "8.8.8.8"
    Then The traceroute should complete within 10 hops