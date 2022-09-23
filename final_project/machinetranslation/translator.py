import json
from statistics import mode
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2022-09-23',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-east.language-translator.watson.cloud.ibm.com')

def englishToFrench(englishText):
    #Code
    frenchText = language_translator.translate(
        text=englishText,
        model_id='en-fr').get_result();
    # print(frenchText['translations'][0]['translation'])
    return frenchText['translations'][0]['translation']


def frenchToEnglish(frenchText):
    englishText = language_translator.translate(
        text=frenchText,
        model_id='fr-en').get_result();
    # print(frenchText['translations'][0]['translation'])
    return englishText['translations'][0]['translation']

print(englishToFrench("Hello") )
print(frenchToEnglish("Bonjour")  ) 

# languages = language_translator.list_languages().get_result()
# print(json.dumps(languages, indent=2))