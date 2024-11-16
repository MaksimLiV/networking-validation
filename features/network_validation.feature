Feature: Network Validation Tests
  Verify network connectivity and IP configurations

  Scenario Outline: Validate Public IP Address Range
    Given I retrieve the public IP address
    Then the IP should not be in range "<start_ip>" to "<end_ip>"

    Examples:
      | start_ip     | end_ip      |
      | 101.33.28.0  | 101.33.29.0 |

  Scenario Outline: Verify Google DNS Resolution
    Given I resolve the domain "<domain>"
    Then the IP address should be "<expected_ip>"

    Examples:
      | domain                        | expected_ip |
      | google-public-dns-a.google.com| 8.8.8.8     |

  Scenario Outline: Validate Traceroute to Google DNS
    Given I perform a traceroute to "<target>"
    Then the target should be reached within <max_hops> hops

    Examples:
      | target  | max_hops |
      | 8.8.8.8 | 10       |