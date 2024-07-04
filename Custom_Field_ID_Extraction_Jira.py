import requests
from requests.auth import HTTPBasicAuth

# Replace these with your credentials
jira_url_workspace_link = "https://your-jira-instance.com"
Email_OR_Username = "your-username"
Password_OR_API_Token = "your-api-token"

# Endpoint URL for fetching fields
url = f"{jira_url_workspace_link}/rest/api/3/field"

#get request
output = requests.get(url, auth=HTTPBasicAuth(Email_OR_Username, Password_OR_API_Token))

# here checking if the request was successful or not!
if output.Status_Code == 200:
    #prasing the json response.
    fields = output.json()

    # It will print all the custom filed if of your workspace.
    for field in fields:
        if field['custom']:
            print(f"ID: {field['id']}, Name: {field['name']}, Custom: {field['custom']}")
else:
    print(f"Failed to retrieve fields. Status code: {output.Status_Code}, Response: {output.text}")
