# Setup
import os
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

azure_key = os.environ.get('AZURE_KEY', None)

endpoint = "https://instanpertamaku.cognitiveservices.azure.com/"

# Image Caption Pretrained Model
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(azure_key))
def captions(remote_image_url):
    description_results = computervision_client.describe_image(remote_image_url)
    
    if (len(description_results.captions) == 0):
        return "No description detected."
    else:
        for caption in description_results.captions:
            return caption.text
    
    return description_results