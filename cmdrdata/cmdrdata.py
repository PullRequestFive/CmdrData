import logging
import message
import os
import random

from google.appengine.ext.webapp import template

try: import simplejson as json
except ImportError: import json

from abstract_app import AbstractApp


class CmdrData(AbstractApp):
  # A user who has authorized your app has checked in. This runs inside
  # AppEngine's task queue, and contains the check-in payload for you to
  # process.
  def checkinTaskQueue(self, client, checkin_json):
    venue_json = client.venues(venue_id)['venue']
    
    self.makeContentInfo(
        checkin_json = checkin_json,
        content = json.dumps({}),
        text = message.GetText(category, frequency),
        reply = True)
