import requests
from .config import ACCESS_TOKEN

LOG_API = "http://4.224.186.213/evaluation-service/logs"

def Log(stack, level, package, message):

    payload = {
        "stack": stack,
        "level": level,
        "package": package,
        "message": message
    }

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(
            LOG_API,
            json=payload,
            headers=headers
        )

        print("Log Response:", response.status_code)
        print(response.json())

    except Exception as e:
        print("Logging Error:", str(e))