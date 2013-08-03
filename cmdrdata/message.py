import json

def GetText(category, frequency):
  data = json.load(open('messages.json'))
  return data[category][str(frequency)]
