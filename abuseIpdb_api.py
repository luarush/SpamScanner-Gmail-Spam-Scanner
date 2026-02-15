import os
import requests

def check_ip(ip):
    #Define AbuseIPDB API
    url = 'https://api.abuseipdb.com/api/v2/check'

    #Define query parameters
    #ipAddress is the IP to check
    #maxAgeInDays consider reports from last 90 days
    querystring = {
        'ipAddress': ip,
        'maxAgeInDays': '90'
    }

    #Define HTTP headers
    #key is the abuseIPDB API key
    headers = {
        'Accept': 'application/json',
        'Key': os.getenv("ABUSEIPDB_KEY")
    }

    #Send GET request to AbuseIPDB
    response = requests.request(
        method='GET',
        url=url,
        headers=headers,
        params=querystring
    )

    #Convert json response into dictorinary
    data = response.json()
   #Abuse score is defined in AbuseIPDB docs
    score = data["data"]["abuseConfidenceScore"]

    #If score is above 50, it gets classified as a threat
    result = "THREAT" if score > 50 else "SAFE"

    return data["data"], result
