# Networking Validation

This project automates networking validation tests using Behave and Docker. The tests validate the public IP, domain resolution, and traceroute to a specific target.

## Requirements

- Python 3.12
- Docker (for running the tests in a containerized environment)
- Git
- `pip` (for managing dependencies)

## Getting Started

Follow these steps to set up the project and run the tests:

### 1. Clone the repository
Clone the project repository to your local machine:

```bash
git clone https://github.com/MaksimLiV/networking-validation.git
cd networking-validation
```

2. Run the tests using Docker
To run the tests in a Docker container, use the provided run-tests.sh script:

```bash
chmod +x run-tests.sh
./run-tests.sh
```

3.  Test Results
After running the tests, you will see the output in the terminal, indicating whether all tests passed or if there were any failures.
Test Scenarios
The tests validate the following scenarios:

3.1 Public IP Validation
Ensure that your public IP does not fall within the range 101.33.28.0 - 101.33.29.0.

3.2 Domain Resolution
Verify that you can resolve the domain google-public-dns-a.google.com to the IP address 8.8.8.8.

3.3 Traceroute Validation
Perform a traceroute to 8.8.8.8 from your local machine. Validate that the target is reached within 10 hops.


Docker Setup

The project uses Docker to run the tests in a containerized environment. The following Docker files are included:

•	Dockerfile: Defines the environment for running the tests.

•	docker-compose.yml: Defines the service and environment for running the tests with Docker Compose.

•	run-tests.sh: A script that checks prerequisites and runs the tests using Docker.

Notes

	•	Make sure Docker is installed on your machine to run the tests in a containerized environment.


### Steps to run the project:
1. **Clone the repository.**
2.	**Run the tests using the run-tests.sh script.**
