import os
import vt


def check_url(url: str):
    #Get VirusTotal API key
    apikey = os.getenv("VT_API_KEY")
    if not apikey:
        print("VT_API_KEY not set.")
        return

    #Create vt client using API key
    with vt.Client(apikey) as client:
        url_id = vt.url_id(url)
        obj = client.get_object("/urls/{}", url_id)
	stats = obj.last_analysis_stats or {}

    #Get the values for malicious and suspicious, default 0 if missing
    malicious = int(stats.get("malicious", 0))
    suspicious = int(stats.get("suspicious", 0))

    #Mark threat if malicious or suspicious, else, mark it safe
    result = "THREAT" if (malicious + suspicious) > 0 else "SAFE"

    return stats, result
