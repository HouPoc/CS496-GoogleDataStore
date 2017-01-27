from google.appengine.ext import ndb
from ndb_definition import *
import json
import webapp2


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')

class BookHandler(webapp2.RequestHandler):		#Handlers for actions related to book
    def post(self):					#Hnadlers for post requests
        book_data = json.loads(self.request.body)	#load the data
	query = Books.query()
        count = len(query.fetch())
        new_book = Books(
            book_id = count + 1,
            title = book_data['title'],
            isbn = book_data['isbn'],
            genre = book_data['genre'],
            author = book_data['author'],
            check_in = book_data['check_in']
        )
        new_book.put()
        book_dict = new_book.to_dict()
	self.response.write(json.dumps(book_dict))
 
    def get(self, book_id):   			        #Get Request Handler
        query_book = Books.query(Books.book_id == int(book_id))
        back_data = query_book.fetch()
        self.response.write(json.dumps(back_data[0].to_dict()))

#class CustomerHandler(webapp2.RequestHandler):
#    def post(self):
#        self.response.write("Customer Handler")

allowed_methods = webapp2.WSGIApplication.allowed_methods
new_allowed_methods = allowed_methods.union(('PATCH',))
webapp2.WSGIApplication.allowed_methods = new_allowed_methods
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/book',BookHandler),
    ('/book/(\d+)', BookHandler),
], debug=True)

