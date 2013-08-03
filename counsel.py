import webapp2
import json
import urllib2
import datetime
import time

class GenerateCounsel(webapp2.RequestHandler):
  def get(self):
    response = self.request.get('checkin')
    json_data = json.loads(response.text)
    user_id = json_data['user']['id']
    now = datetime.datetime.now()
    tsd = datetime.timedelta(days=7)
    t = now - tsd
    epoch_seconds = time.mktime(t.timetuple())
    limit = 100
    parameters = 'limit=%s&afterTimestamp=%s' % (limit, epoch_seconds)
    urllib2.urlopen('https://api.foursquare.com/v2/users/%s/checkins?' + parameter % user_id)
