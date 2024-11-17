GREEN='\033[0;32m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m'

log() {
    echo -e "${BLUE}[$(date +'%Y-%m-%d %H:%M:%S')]${NC} $1"
}

check_error() {
    if [ $? -ne 0 ]; then
        echo -e "${RED}$1${NC}"
        exit 1
    fi
}

mkdir -p reports

log "Cleaning old reports..."
rm -rf reports/*

log "Cleaning up old containers..."
docker-compose down --remove-orphans
check_error "Failed to clean up containers"

log "Building Docker image..."
docker-compose build
check_error "Docker build failed"

log "Running tests..."
docker-compose up --abort-on-container-exit
check_error "Tests execution failed"

if [ -f "reports/test_results.txt" ]; then
    if grep -q "failed" reports/test_results.txt; then
        echo -e "${RED}Tests FAILED!${NC}"
        echo "Check reports/test_results.txt for details"
        exit 1
    else
        echo -e "${GREEN}All tests PASSED!${NC}"
    fi
else
    echo -e "${RED}Test results file not found!${NC}"
    exit 1
fi

log "Cleaning up..."
docker-compose down
check_error "Failed to clean up after tests"

log "Test run completed successfully!"