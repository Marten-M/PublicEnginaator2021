import requests
import json
import http.client

class AzurClient(object):
    """
    AzurClient class to communicate with Microsoft Azur Cognitive Services.
    """
    
    def __init__(self, subscription_key: str, environment = "TEST") -> None:
        self.subscription_key = subscription_key
        self.environment = 0 if environment == "TEST" else 1

    def read_number(self, image: bytes) -> float:
        """
        Read number on the image.

        Params:

        image - image as raw binary data
        """
        if self.environment:
            headers = {
                'Content-Type': 'application/octet-stream',
                "Ocp-Apim-Subscription-Key" : self.subscription_key
            }
            conn = http.client.HTTPSConnection('trafineo-ocr.cognitiveservices.azure.com')
            conn.request("POST", "/vision/v3.2/ocr", image, headers)
            response = conn.getresponse()
            data = response.read()
            conn.close()
        else:
            headers = {"Ocp-Apim-Subscription-Key" : self.subscription_key}
            url = "http://localhost:8080/vision/v3.2/ocr"
            data = requests.post(url, data = image, headers = headers).text

        
        value = self.get_number_from_json(data)

        return value

    def get_number_from_json(self, file: str) -> float:
        """
        Read the number value from a json file.

        Params:
        file - json file formated as a string
        """

        acceptable_chars = "1234567890.,"
        file = json.loads(file)

        if "regions" not in file:
            return -2
        
        regions = file["regions"]

        for region in regions:
            lines = region["lines"]
            for line in lines:
                words = line["words"]
                for word in words:
                    number = True
                    text = word["text"]

                    for char in text:
                        if char not in acceptable_chars:
                            number = False
                            break
                    
                    if number:
                        val = float(text.replace(",", "."))

                        return val

        return -1
        