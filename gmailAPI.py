import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.modify"]


def gmail_api():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None

    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    # Call the Gmail API
    service = build("gmail", "v1", credentials=creds)
    return service


def get_email(service):
    try:
	#Search for unread message
        results = service.users().messages().list(
            userId="me", 
            q="is:unread", #Uses Gmail search syntax to filter emails
            maxResults=1  #Limits to one message
        ).execute()

        #Get list of messages Ids from API
        msgs = results.get("messages", [])

	#If there's no unread message return none
        if not msgs:
            return None

	#Get ID of first message
        msg_id = msgs[0]["id"]

	#Get message metadata
	#metadata gets headers only
        msgs = service.users().messages().get(
            userId="me",
            id=msg_id,
            format="metadata",
            metadataHeaders=["From", "Subject"]
        ).execute()

        # Get Email information
	#Convert header list into disctionary
        headers = {h["name"]: h["value"] 
	    for h in msgs["payload"]["headers"]
	}

	#Returns email information
        return {
            "id": msg_id,
            "subject": headers.get("Subject", "(no subject)"),
            "from": headers.get("From", "(no from)"),
            "snippet": msgs.get("snippet", "")
        }

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f"An error occurred: {error}")
        return None
