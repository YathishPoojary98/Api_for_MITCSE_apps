import requests
import json
import argparse
import sys


url = 'https://mitcse.manipal.edu/translate_api'

langs = {'Kannada':'kn','Tamil':'ta','Hindi':'hi','kannada':'kn','tamil':'ta','hindi':'hi'}

parser = argparse.ArgumentParser(description="Token Classification")
parser.add_argument("--text", type=str, help="Input Text")
parser.add_argument("--slang", type=str, help="Source Language")
parser.add_argument("--tlang", type=str, help="Target Language")
args = parser.parse_args()

sentence = args.text
source_lang = args.slang
target_lang = args.tlang

#print(sentence)

if source_lang in langs.keys():
    sl_lang = langs[source_lang]
else:
    sl_lang = source_lang
if target_lang in langs.keys():
    tl_lang = langs[target_lang]
else:
    tl_lang = target_lang

data = {
    "inputText": sentence,
    "sourcelang": sl_lang,  
    "targetlang": tl_lang,  
    "version": "V3.1"    
}


response = requests.post(url, json=data, verify=False)

if response.status_code == 200:
    translated_text = response.json()
    print("Input Text :", sentence)
    print("Translated Text :", translated_text)
else:
    print("Error:", response.status_code)
