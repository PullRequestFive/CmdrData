import json
import logging

def GetText(category, frequency):
  logging.info('Category %s; frequency %s', category, frequency)
  data = json.load(open('messages.json'))
  try:
    return data[category][str(frequency)]
  except KeyError:
    return ''
