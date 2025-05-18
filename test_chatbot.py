import requests

def lookup(query):
    url = "http://localhost:8080/chat"
    try:
        response = requests.post(url, json={"message": query})
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Lookup error: {e}")
        return {"response": "Error during lookup"}
