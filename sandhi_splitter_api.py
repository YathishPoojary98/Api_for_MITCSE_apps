import requests
import json
import argparse
import sys


url = 'https://mitcse.manipal.edu/splitter_api'

parser = argparse.ArgumentParser(description="Token Classification")
parser.add_argument("--word", type=str, help="Input word")
args = parser.parse_args()

input_word = args.word

data = {
    "inputword": input_word
}

response = requests.post(url, json=data, verify=False)


if response.status_code == 200:
    converted_text = response.json()
    if "ಸಂಧಿ ಪದ ಛೇದ ಸಫಲವಾಗಿದೆ" in converted_text['1']:
        print(converted_text['1'])
        print("ಹುಡುಕಿದ ಪದ : ", converted_text['2'])
        print("ಪೂರ್ವಪದ   :", converted_text['3'])
        print("ಉತ್ತರಪದ    :", converted_text['4'])
        print("ಸಂಧಿ        : ", converted_text['5'])
    else:
        print(converted_text['1'])
else:
    print("Error:", response.status_code)
