import re
import requests
import json
from jsonpath import jsonpath

def state0():
    url = f"https://api.seniverse.com/v3/life/suggestion.json?key=SczjlbdgCuaWr74Sr&location=guangan&language=zh-Hans"
    resp = requests.get(url)
    result = jsonpath(resp.json(),'$..brief')

    text0 = result[0] + "洗车," + "温度" + result[1] + "," + result[2] + "感冒" + ",紫外线" + result[5]
    return text0

