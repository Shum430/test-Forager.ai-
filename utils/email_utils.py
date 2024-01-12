import requests


def validate_email_with_hunter(email):
    api_key = ''
    api_endpoint = ''

    params = {
        'email': email,
        'api_key': api_key,
    }

    try:
        response = requests.get(api_endpoint, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Parse the API response and return True or False based on validation result
        data = response.json()
        if data['data']['result'] == 'valid':
            return True
        else:
            return False

    except requests.exceptions.RequestException as e:
        # Handle API request error (e.g., log the error, return False)
        print(f"Error during API request: {e}")
        return False
