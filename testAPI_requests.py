import requests

BASE_URL = "http://127.0.0.1:8000"

def test_root():
    print("Testing GET /")
    response = requests.get(f"{BASE_URL}/")

    print("Status Code:", response.status_code)
    print("Response:", response.json())
    print("-" * 50)


def test_health():
    print("Testing GET /health")
    response = requests.get(f"{BASE_URL}/health")

    print("Status Code:", response.status_code)
    print("Response:", response.json())
    print("-" * 50)


def test_generate():
    print("Testing POST /generate")

    data = {
        "text": """Artificial intelligence is transforming many industries including healthcare,
        finance, and education. It allows machines to learn patterns from data and make
        decisions automatically. Many companies are adopting AI technologies to improve
        productivity and create new services."""
    }

    response = requests.post(f"{BASE_URL}/generate", json=data)

    print("Status Code:", response.status_code)

    try:
        print("Response:", response.json())
    except Exception:
        print("Response is not JSON:", response.text)

    print("-" * 50)


if __name__ == "__main__":
    print("Starting API tests...\n")

    test_root()
    test_health()
    test_generate()

    print("\nAll tests completed.")
