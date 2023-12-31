import requests
from Auth.login_get_token import login_and_retrieve_token

DATA_URL = 'http://localhost:3000/api/rt/'

def get_data_with_token(token):
    print(token)
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(DATA_URL, headers=headers)
    if response.status_code == 200:
        data = response.json().get('generators')
        print("Data retrieval successful.")
        return data
    else:
        print(f"Failed to fetch generators. Status code: {response.status_code}")
        return None


# Main function to demonstrate the workflow
def main():
    email = 'user@gmail.com'  # Replace with actual email
    password = 'user123456'  # Replace with actual password

    # Step 1: Login and retrieve token
    token = login_and_retrieve_token(email, password)

    if token:
        # Step 2: Use the token to get generators for extraction and analysis
        data = get_data_with_token(token)
        # Add your generators processing and analysis here
        print("Data:", data)
    else:
        print("No token available. Cannot retrieve generators.")


# Run the main function
if __name__ == "__main__":
    main()