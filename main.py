import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type']='text/html'
        self.response.write('<body style=\'background-color:black color:white\'>Cambio de color Git hub</body>')


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)


