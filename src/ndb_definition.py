#The definitions of entities(Books and customers) 
from google.appengine.ext import ndb


class Books(ndb.Model):
    id = ndb.IntegerProperty(required=True)
    title = ndb.StringProperty(required=True)
    isbn = ndb.StringProperty(required=True)
    genre = ndb.StringProperty(repeated=True)
    author = ndb.StringProperty(required=True)
    check_in = ndb.BooleanProperty()
    
class Customers(ndb.Model):
    customer_id = ndb.IntegerProperty(required=True)
    name = ndb.StringProperty(required=True)
    balance = ndb.IntegerProperty(required=True)
    check_out = ndb.StringProperty(repeated=True)
