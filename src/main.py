from google.appengine.ext import ndb
import json
import ndb_definition
import webapp2


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')

class BookHandler(webapp2.RequestHandler):		#Handlers for actions related to book
    def post(self):					#Hnadlers for post requests
        book_data = json.loads(self.request.body)	#load the data
	self.response.write(json.dumps(book_data))
#class CustomerHandler(webapp2.RequestHandler):
#   def post(self):
allowed_methods = webapp2.WSGIApplication.allowed_methods
new_allowed_methods = allowed_methods.union(('PATCH',))
webapp2.WSGIApplication.allowed_methods = new_allowed_methods
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/book'BookHandler),
], debug=True)
