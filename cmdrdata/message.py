import json
import logging
import os

def GetText(category, frequency):
  logging.info('Category %s; frequency %s', category, frequency)
  filename = os.path.dirname(os.path.realpath(__file__)) + '/messages.json'
  data = json.load(open(filename))
  try:
    return data[category][str(frequency)]
  except KeyError:
    return ''
