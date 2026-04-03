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
        "text": """Artificial Intelligence (AI) technology has become one of the most transformative innovations of the modern era, influencing nearly every industry and aspect of human life. At its core, AI refers to the development of computer systems that can perform tasks traditionally requiring human intelligence, such as understanding language, recognizing images, making decisions, and learning from data. Over the past decade, advances in computing power, the availability of massive datasets, and breakthroughs in machine learning algorithms have significantly accelerated the development of AI systems. One of the most important branches of AI is machine learning, where algorithms learn patterns from data rather than being explicitly programmed."""
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
