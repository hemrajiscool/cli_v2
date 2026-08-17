import requests
import os
from dotenv import load_dotenv

load_dotenv()

class AIclient:
    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        self.model_name = "gemini-3-flash-preview"
    def generate(self, messages):
        contents = []
        for message in messages:
            if message["role"] == "assistant":
                role = "model"
            else:
                role = message["role"]
            constructed_msg = {
                "role": role,
                "parts": [
                    {
                        "text": message["content"]
                    }
                ]
            }
            contents.append(constructed_msg)
        payload = {
            "contents": contents
        }
        headers = {
        "x-goog-api-key": self.api_key,
        "Content-Type": "application/json"
        }

        response = requests.post(
            f"https://generativelanguage.googleapis.com/v1beta/models/{self.model_name}:generateContent",
            headers=headers,
            json=payload,
            timeout=30
        )
        
        response.raise_for_status()

        data = response.json()
        answer = data["candidates"][0]["content"]["parts"][0]["text"]
        return answer