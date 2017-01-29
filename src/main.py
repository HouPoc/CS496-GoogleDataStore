from google.appengine.ext import ndb
from ndb_definition import *
import json
import webapp2


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')
    
    def delete(self):
        ndb.delete_multi(Books.query().fetch(keys_only=True))    
#        ndb.delete_multi(Customers.query().fetch(keys_only=True))

    
class BookHandler(webapp2.RequestHandler):		#Handlers for actions related to book
    def p(self):					#Hnadlers for post requests
        book_data = json.loads(self.request.body)	#load the data
	query = Books.query()
        count = len(query.fetch())
        new_book = Books(
            id = count + 1,
            title = book_data['title'],
            isbn = book_data['isbn'],
            genre = book_data['genre'],
            author = book_data['author'],
            check_in = book_data['check_in']
        )
        new_book.put()
        book_dict = new_book.to_dict()
	self.response.write(json.dumps(book_dict))
 # no error
    def get(self, **args):   			        #Get Request Handler
        if 'book_id' in args:
       	    query_book = Books.query(Books.id == int(args['book_id']))
       	    back_data = query_book.fetch()
            self.response.write(json.dumps(back_data[0].to_dict()))
        else:
            query_key = self.request.get('check_in')
            if query_key:
                checkedIn = (query_key == "true")
                query_book = Books.query(Books.check_in == checkedIn)
                book_list = query_book.fetch()
                back_data = []
                for item in book_list:
                    back_data.append(item.to_dict())
                self.response.write(json.dumps(back_data))
            else:				
                query_book = Books.query()
                book_list = query_book.fetch()
                back_data = []
                for item in book_list:
                    back_data.append(item.to_dict())
                self.response.write(json.dumps(back_data))  
#delete no error 
    def delete(self, **args):
        query_book = Books.query(Books.id == int(args['book_id']))
        target_book = query_book.get()
        target_book_id = target_book.id
        target_book.key.delete()
        self.response.write("book %d has been deleted" % target_book_id)
# Customer handler no error
class CustomerHandler(webapp2.RequestHandler):
    def put(self):
        customer_data = json.loads(self.request.body)
        query = Customers.query()
        count = len(query.fetch())
        if (len(customer_data['checked_out']) != 0):
            new_customer = Customers(
                id = count + 1,
                name = customer_data['name'],
                balance = float(customer_data['balance']),
                check_out = customer_data['checked_out']
           )
        else:
            new_customer = Customers(
                id = count + 1,
                name = customer_data['name'],
                balance = float(customer_data['balance']),
                check_out = []
           ) 
        new_customer.put()
        customer_dict = new_customer.to_dict()
        self.response.write(json.dumps(customer_dict))

    def get(self, **args):
        if 'customer_id' in args:
            query_customer = Customers.query(Customers.id == int(args['customer_id']))
            back_data = query_customer.fetch()
            self.response.write(json.dumps(back_data[0].to_dict()))   
        else:
            query_customer = Customers.query()
            customer_list = query_customer.fetch()
            back_data = []
            for item in customer_list:
                back_data.append(item.to_dict())
            self.response.write(json.dumps(back_data))

    def delete(self, **args):
        query_customer = Customers.query(Customers.id == int(args['customer_id']))
        target_customer = query_customer.get()
        target_customer_id = target_customer.id
        target_customer.key.delete()
        self.response.write("customer %d has been deleted" % target_customer_id)

class EventHandler(webapp2.RequestHandler):
	def put(self, **args):
		if ('customer_id' in args and 'book_id' in args):
			query_customer = Customers.query(Customers.id == int(args['customer_id']))
			query_book = Books.query(Books.id == int(args['book_id']))
			book = query_book.get()
			book.check_in = False
			book.put()
			customer = query_customer.get()
			book_link = ("/books/%d" % book.id)
			customer.check_out.append(book_link)
			customer.put()
			self.response.write(json.dumps(customer.to_dict()))
	def delete(self, **args):
		if ('customer_id' in args and 'book_id' in args):
			self.response.write(json.dumps(customer.to_dict()))
		
allowed_methods = webapp2.WSGIApplication.allowed_methods
new_allowed_methods = allowed_methods.union(('PATCH',))
webapp2.WSGIApplication.allowed_methods = new_allowed_methods
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/books', BookHandler),
    ('/customers', CustomerHandler),
], debug=True)
app.router.add(webapp2.Route('/books/<book_id:\d+>', handler=BookHandler))
app.router.add(webapp2.Route('/customers/<customer_id:\d+>', handler=CustomerHandler))
app.router.add(webapp2.Route('/customers/<customer_id:\d+>/books/<book_id:\d+>', handler=EventHandler))
