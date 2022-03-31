import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticators=IAMAuthenticator(apikey)
language_translator= LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticators
)
language_translator.set_service_url(url)

# Function englishToFrench
def EnglishToFrench(english_text):
    """ Traslate english to french """
    translation = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    frenchtext = translation['translations'][0]['translation']
    return frenchtext

# Function frenchToEnglisg
def FrenchToEnglish(french_text):
    """Traslate french to english"""
    translation = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    englishtext = translation['translations'][0]['translation']
    return englishtext