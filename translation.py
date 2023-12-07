
import requests, uuid, json
from iso639.iso639 import _Language

class translate:
    """
    This class making use in Azure translation API to translat messages from english to any other language
    """

    def __init__(self, api_key, endpoint, location) -> None:
        self.api_key = api_key
        self.endpoint = endpoint
        self.location = location

    def convert_to_langauage_code(self, language: str):
        try:
            converted_to_iso = _Language(language.title())
            return converted_to_iso.pt1 if converted_to_iso is not None else None
        except ValueError:
            return None

    def translate(self, message: str, target_language: str) -> str:
        if not target_language.__eq__("english"):
            print("target len " , target_language )

            path = '/translate'
            constructed_url = self.endpoint + path
            params = {
                'api-version': '3.0',
                'from': 'en',
                'to': self.convert_to_langauage_code(target_language) 
            }

            headers = {
                'Ocp-Apim-Subscription-Key': self.api_key,
                # location required if you're using a multi-service or regional (not global) resource.
                'Ocp-Apim-Subscription-Region': self.location,
                'Content-type': 'application/json',
                'X-ClientTraceId': str(uuid.uuid4())
            }

            # You can pass more than one object in body.
            body = [{
                'text': message
            }]

            request = requests.post(constructed_url, params=params, headers=headers, json=body)
            response = request.json()
            response = json.dumps(response[0]["translations"][0]["text"])
            return response[1:-1] if response is not None else None
    
        return message