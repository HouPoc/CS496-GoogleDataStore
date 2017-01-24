import webapp2

class MainHandler(webapp2.RequestHandler)
    def get(self)
	    self.response.write('hello from handler.py')
		
class SecondHandler(webapp2.RequestHandler)
	def get(self)
		self.response.write('hello from handler.py second')
		
app = webapp2.WSGIApplication(
	[('/osu/1/?', MainHandler),('/osu/1.*', SecondHandler)]
	, debug=True)
