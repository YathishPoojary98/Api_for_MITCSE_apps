import requests
import json
import argparse
import sys


url = 'https://mitcse.manipal.edu/parse_convert_api'

parser = argparse.ArgumentParser(description="Token Classification")
parser.add_argument("--text", type=str, help="Input Text")
args = parser.parse_args()

input_text = args.text

data = {
    "inputText": input_text
}

response = requests.post(url, json=data, verify =False)

if response.status_code == 200:
    converted_text = response.json()
    print("Input Text : ", input_text)
    print("Parsed text : \n",converted_text)
else:
    print("Error:", response.status_code)
