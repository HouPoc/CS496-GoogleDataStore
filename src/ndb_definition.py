#The definitions of entities(Books and customers) 
from google.appengine.ext import ndb


class Books(ndb.Model):
    book_id = ndb.IntegerProperty(required=True)
    title = ndb.StringProperty(required=True)
    isbn = ndb.StringProperty(required=True)
    genre = ndb.StringProperty(repeated=True)
    author = ndb.StringProperty(required=True)
    check_in = ndb.BooleanProperty()
    
    def to_dict(self):
	genres = {}
        index = 1
        for item in genre:
            genres[index] = item
            index += 1               
        return { 
                'book_id': self.book_id,
                'title': self.title,
                'isbn': self.isbn,
                'genre': genres,
                'author': self.author,
                'check_in': self.book_id,
        }

class Customers(ndb.Model):
    customer_id = ndb.IntegerProperty(required=True)
    name = ndb.StringProperty(required=True)
    balance = ndb.IntegerProperty(required=True)
    check_out = ndb.StringProperty(repeated=True)
    def to_dict(self):
        ckeck_list = {}
        index = 1
        for item in check_out:
            check_list[index] = item
            index += 1

    return {
            'customer_id' = self.customer_id,
            'name' = self.name,
            'balance' = self.balance,
            'checked_out' = check_list
	}
