#include <iostream>

int main() {
    std::cout << R"({"timestamp":"2026-01-01T00:00:00Z","level":"INFO","service_name":"cpp-service","version":"0.0.1","trace_id":"stub","message":"hello from cpp","context":{}})" << std::endl;
    return 0;
}
