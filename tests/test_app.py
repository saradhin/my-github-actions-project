from fastapi.testclient import TestClient
from main import app  # Import your FastAPI app instance

# Create a TestClient instance
client = TestClient(app)


# Define your test functions
def test_read_root():
    # Use the TestClient to make a simulated GET request
    response = client.get("/")

    # Assert the expected status code
    assert response.status_code == 200

    # Assert the expected JSON response
    assert response.json() == {"message": "Hello, World!"}
