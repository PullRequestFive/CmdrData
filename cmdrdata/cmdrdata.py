import logging
import message
import os
import random
import datetime
import time
import collections

from google.appengine.ext.webapp import template

try: import simplejson as json
except ImportError: import json

from abstract_app import AbstractApp


class CmdrData(AbstractApp):
  # A user who has authorized your app has checked in. This runs inside
  # AppEngine's task queue, and contains the check-in payload for you to
  # process.
  def checkinTaskQueue(self, client, checkin_json):
    logging.debug('Current checkin: %s', checkin_json)
    user_id = checkin_json['user']['id']
    categories = checkin_json['venue']['categories']
    category_name = find_primary_category(categories)

    now = datetime.datetime.now()
    tsd = datetime.timedelta(days=7)
    t = now - tsd
    epoch_seconds = int(time.mktime(t.timetuple()))
    limit = 100
    parameters = {'limit': limit,
                  'afterTimestamp': epoch_seconds}
    week_checkins = client.users.checkins(user_id, parameters)
    logging.debug('Received the following JSON response from 4sq: %s', week_checkins)
    checkins = week_checkins['checkins']['items']
    frequency = collections.defaultdict(int)
    for c in checkins:
      categories = c['venue']['categories']
      frequency[find_primary_category(categories)] += 1
    message_text = message.GetText(category_name, frequency[category_name])
    if message_text:
      self.makeContentInfo(
          checkin_json = checkin_json,
          content = json.dumps({}),
          text = message_text,
          reply = True)

def find_primary_category(categories):
  for category in categories:
    if category['primary']:
      return category['name']
