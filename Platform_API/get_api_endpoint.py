import requests
from Auth.login_get_token import login_and_retrieve_token # gives no error only when running python manage.py runserver

DATA_URL = 'http://localhost:3000/api/rt/'


def get_data_with_token(token):
    print(token)
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(DATA_URL, headers=headers)
    if response.status_code == 200:
        data = response.json().get('data')
        # Process and analyze your data here
        print("Data retrieval successful.")
        return data
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None


# Main function to demonstrate the workflow
def main():
    email = 'user@gmail.com'  # Replace with actual email
    password = 'user123456'  # Replace with actual password

    # Step 1: Login and retrieve token
    token = login_and_retrieve_token(email, password)

    if token:
        # Step 2: Use the token to get data for extraction and analysis
        data = get_data_with_token(token)
        # Add your data processing and analysis here
        print("Data:", data)
    else:
        print("No token available. Cannot retrieve data.")


# Run the main function
if __name__ == "__main__":
    main()