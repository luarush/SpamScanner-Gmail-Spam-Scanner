from gmailAPI import gmail_api, get_email
from extract_url import extract_url
from virusTotal_api import check_url
from abuseIpdb_api import check_ip

#Extract domain from URL
from urllib.parse import urlparse
#Convert domain name to IP address
import socket


def main():
    #Connect to Gmail (gmail_api authenticates user 
    #and returns object that allows API calls 
    connection = gmail_api()

    #Get one unread Email (returns subject, sender, message and id)
    email_obj = get_email(connection)
    #If no email exists, stop
    if not email_obj:
        print("No unread emails found.")
        return

    #Output for Gmail
    print("Subject:", email_obj["subject"])
    print("From:", email_obj["from"])
    print("Message:", email_obj["snippet"])
    print("")

    #Looks for urls on the email
    url = extract_url(email_obj["snippet"])
    print("Found URL:", url if url else "(none)")
    print("")

    #If no url found, skip
    if not url:
        print("No URL found. Skipping VirusTotal analysis.")
        return

    #Check url  on VirusTotal and returns statistics and threat results
    stats, result = check_url(url)
    print("VirusTotal stats:", stats)
    print("Result:", result)
    print("")

    #Check on AbuseIPDB (requires an IP address)
    #Get the domain name  from url
    parsed = urlparse(url)
    domain = parsed.netloc

    #Convert domain name to IP address using DNS lookup
    ip = socket.gethostbyname(domain)

    #check_ip sends IP to AbuseIPDB API and retuns abuse data and results
    #each on one index
    abuse_data, abuse_result = check_ip(ip)
    print("AbuseIPDB score:", abuse_data["abuseConfidenceScore"])
    print("AbuseIPDB result:", abuse_result)


if __name__ == "__main__":
    main()
