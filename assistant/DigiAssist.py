from bardapi import Bard
import os
#import requests

os.environ['_BARD_API_KEY'] = 'ZAgOdU7kKiGjPABrdK45qj5vfcVaaz3NC5A-i4mmUUBH_2SQLRSwTE8it3KlgjL3Iw8neQ.'
token = os.getenv("_BARD_API_KEY")
#url = "https://api.bard.ai/generate"


# bard = Bard(token=token)


def ask_anything(user_input):
    bard = Bard(token=token)
    response = bard.get_answer(user_input)
    return response['content']


# def bardResponse(user_input):
#     headers = {
#         "Authorization": token,
#         "Content-Type": "application/json",
#     }
#
#     data = {
#         'prompt': user_input,
#         'max_tokens': 256
#     }
#
#     response = requests.post(url, headers=headers, json=data, verify=False)
#     print(response)
