import webapp2
from webapp2_extras import jinja2

class BaseHandler(webapp2.RequestHandler):

  @webapp2.cached_property
  def jinja2(self):
    # Returns a Jinja2 renderer cached in the app registry.
    return jinja2.get_jinja2(app=self.app)

  def render_response(self, _template, **context):
    # Renders a template and writes the result to the response.
    rv = self.jinja2.render_template(_template, **context)
    self.response.write(rv)

class RootHandler(BaseHandler):
  def get(self):
    context = {}
    self.render_response('root.html', **context)

app = webapp2.WSGIApplication([
  ('/', RootHandler),
  ('/counsel', None), # TODO(kayvon): Correct class here.
  ], debug=True)
