# SpamScanner – Gmail Threat Analyzer

This is a Python prototype that authenticates to Gmail using Google OAuth, reads unread emails, and checks URLs and IP addresses using the VirusTotal and AbuseIPDB APIs. It outputs one of the labels that the final program will use: **SAFE** or **THREAT**.

This prototype uses Python, Gmail API, VirusTotal API, and the AbuseIPDB API. Kali Linux was used to develop and test the program, but it is not required. The script can run on any operating system that supports Python 3.

---

## Gmail Authentication

To read your inbox, the script requires a `credentials.json` file. You need to generate this file in Google Cloud after enabling the Gmail API.

### Steps:

1. Create a Google Cloud project.
2. Enable the Gmail API.
3. Create OAuth credentials.
4. Download the `credentials.json` file.
5. Place it in the project root directory.

Because the Google Cloud project is in testing mode, you need to add your email address to the test users list in the OAuth consent screen settings. If your email is not added, Google will block authentication.

For security reasons, `credentials.json` and `token.json` are not included in this repository. You must generate your own credentials.

The first time you run the script, it opens a browser window and asks you to log in and authorize access. After authorization, a `token.json` file is created locally to store your session.

---

## API Keys Required

You must create accounts and obtain API keys from:

- [VirusTotal](https://docs.virustotal.com/docs/api-overview)
- [AbuseIPDB]( https://www.abuseipdb.com/api.html)

Set them as environment variables:

```bash
export VT_API_KEY="YOUR_VIRUSTOTAL_KEY"
export ABUSEIPDB_KEY="YOUR_ABUSEIPDB_KEY"

How to Install and Run
1. Clone the repository
git clone [your github link]

2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

3. Install dependencies
pip install google-api-python-client google-auth google-auth-oauthlib vt-py requests streamlit

4. Run the program
python main.py

