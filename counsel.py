import webapp2
import json
import urllib2
import datetime
import time
import collections
import logging

class GenerateCounsel(webapp2.RequestHandler):
  def get(self):
    response = self.request.get('checkin')
    json_data = json.loads(response.response)
    logging.debug('Received the following JSON response from 4sq: %s', json_data)
    user_id = json_data['user']['id']
    category_name = json_data['venue']['categories']['name']
    now = datetime.datetime.now()
    tsd = datetime.timedelta(days=7)
    t = now - tsd
    epoch_seconds = time.mktime(t.timetuple())
    limit = 100
    parameters = 'limit=%s&afterTimestamp=%s' % (limit, epoch_seconds)
    week_checkins = urllib2.urlopen('https://api.foursquare.com/v2/users/%s/checkins?' + parameters % user_id)
    c_json = json.loads(week_checkins.response)
    logging.debug('Received the following JSON response from 4sq: %s', c_json)
    checkins = c_json['items']['checkins']
    frequency = collections.defaultdict(int)
    for c in checkins:
      categories = c['venue']['categories']
      for category in categories:
        if category['primary']:
          frequency[category['name']] += 1
