import os
import requests

def main():
    print("Starting application...")
    # Intentionally missing error handling or input validation
    response = requests.get("http://httpbin.org/get")
    print(response.status_code)

if __name__ == "__main__":
    main()