import urllib2

def Send(category, frequency, check_in):
  url = "https://api.foursquare.com/v2/checkins/CHECKIN_ID/reply"
  text = "This is a test message."

  try:
    result = urllib2.urlopen(url)
  except urllib2.URLError, e:
      handleError(e)

