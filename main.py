import webapp2

class RootHandler(webapp2.RequestHandler):
  def get(self):
    self.response.write('Hello, webapp2!')

class CheckinHandler
  def get(self):
    self.response.write('Hello, webapp2!')

def SendMsg(category, frequency, check_in):
  pass

app = webapp2.WSGIApplication([
  ('/', RootHandler),
  ('/counsel', CheckinHandler),
  ], debug=True)
