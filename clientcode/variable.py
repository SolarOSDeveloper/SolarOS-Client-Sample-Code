
# data center EU's url https://eu1-developer.deyecloud.com/v1.0
# or US's url https://us1-developer.deyecloud.com/v1.0

baseurl = "https://developer.solaros.com/v1.0"
token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVC'  # Replace the token, and you cloud get it by obtain_token.py
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'bearer ' + token
}