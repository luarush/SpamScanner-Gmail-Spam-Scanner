import re

def extract_url(text: str):
    if not text:
        return None

    # Find http and https links
    urls = re.findall(r"https?://[^\s)>\"]+", text)

    # Find www links without protocol
    www_urls = re.findall(r"\bwww\.[^\s)>\"]+", text)

    # Normalize www links
    urls.extend(["https://" + u for u in www_urls])

    # Remove duplicates while preserving order
    seen = set()
    urls = [u for u in urls if not (u in seen or seen.add(u))]

    return urls[0] if urls else None
