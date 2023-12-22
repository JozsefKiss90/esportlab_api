import requests

AUTH_URL = 'http://localhost:3000/api/external_auth'  # Adjusted to the new endpoint

def login_and_retrieve_token(email, password):
    credentials = {'email': email, 'password': password}
    response = requests.post(AUTH_URL, json=credentials)
    if response.status_code == 200:
        token = response.json().get('token')
        print("Authentication successful. Token retrieved.")
        return token
    else:
        print(f"Failed to authenticate. Status code: {response.status_code}")
        return None

