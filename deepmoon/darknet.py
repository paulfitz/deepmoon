import requests


DARKNET_URL = "https://api.github.com/repos/pjreddie/darknet/commits"


def fetch_messages():
    commits = requests.get(DARKNET_URL).json()
    messages = [commit['commit']['message'] for commit in commits]
    return messages
