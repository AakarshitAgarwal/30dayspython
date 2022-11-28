import json

data = '{"var1":"harry","var2":56}'

parsed = json.loads(data)
# print(parsed)


data2 = {
    "channel_name": "CodeWithHarry",
    "car": ['bmw','audi a8','ferrari'],
    "fridge": ('roti',540),
    "isbad": False
}


jsondump = json.dumps(data2)
print(jsondump)