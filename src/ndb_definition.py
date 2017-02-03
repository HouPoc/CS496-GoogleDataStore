#The definitions of entities(Books and customers) 
from google.appengine.ext import ndb


class Books(ndb.Model):
    title = ndb.StringProperty(required=True)
    isbn = ndb.StringProperty(required=True)
    genre = ndb.StringProperty(repeated=True)
    author = ndb.StringProperty(required=True)
    checkedIn = ndb.BooleanProperty()
    
class Customers(ndb.Model):
    name = ndb.StringProperty(required=True)
    balance = ndb.FloatProperty(required=True)
    check_out = ndb.StringProperty(repeated=True)
