import requests

# Use your actual values from Strava API settings
CLIENT_ID = 182473  # Replace with your actual client ID
CLIENT_SECRET = "f1749fb3b93d7f7e8a96c383736317c78727bd05"  # Replace with your actual secret

# Step 1: Get authorization code (you'll need to do this manually)
auth_url = f"https://www.strava.com/oauth/authorize?client_id={CLIENT_ID}&response_type=code&redirect_uri=http://localhost&approval_prompt=force&scope=read,activity:read_all"

print("1. Go to this URL and authorize the app:")
print(auth_url)
print("\n2. When the page fails to load, look at the URL in your browser")
print("3. Copy the 'code' parameter from the URL")
print("4. The URL will contain: ...&code=XXXXXXXX&...")
auth_code = input("5. Enter just the code (without 'code='): ")

# Step 2: Exchange code for access token
token_url = "https://www.strava.com/oauth/token"
payload = {
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'code': auth_code,
    'grant_type': 'authorization_code'
}

response = requests.post(token_url, data=payload)
token_data = response.json()

if 'access_token' in token_data:
    print(f"\nYour access token: {token_data.get('access_token')}")
    print(f"Refresh token: {token_data.get('refresh_token')}")
else:
    print(f"Error: {token_data}")