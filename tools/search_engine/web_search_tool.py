import os
import requests
from dotenv import load_dotenv

load_dotenv()

class WebSearch:
    def __init__(self, user_url):
        self.tavily_api_key = os.getenv('TAVILY_API_KEY')
        self.user_url = user_url


    def web_search(self):
        url = "https://api.tavily.com/extract"

        payload = {
            "urls": self.user_url,
            "include_images": False,
            "extract_depth": "advanced"
        }

        headers = {
            "Authorization": f"Bearer {self.tavily_api_key}",
            "Content-Type": "application/json"
        }

        response = requests.request(
            "POST",
            url,
            json=payload,
            headers=headers
        )

        print(response.text)