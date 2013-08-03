import webapp2
import json
import urllib2
import datetime

class GenerateCounsel(webapp2.RequestHandler):
  def get(self):
    response = self.request.get('checkin')
    json_data = json.loads(response.text)
    user_id = json_data['user']['id']
    parameters = 'limit=100&afterTimestamp='
    urllib2.urlopen('https://api.foursquare.com/v2/users/%s/checkins?' + parameter % user_id)
