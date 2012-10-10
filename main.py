import webapp2
import jinja2
import os

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


class MainPage(webapp2.RequestHandler):
    def get(self):
        
        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render({}))
   
class StartPage(webapp2.RequestHandler):
    def get(self):
        
        template = jinja_environment.get_template('start.html')
        self.response.out.write(template.render({}))
        
class InfoPage(webapp2.RequestHandler):
    def get(self):
        
        template = jinja_environment.get_template('info.html')
        self.response.out.write(template.render({}))
        
class Hash(webapp2.RequestHandler):
    def get(self, roothash):
        template_values = {'roothash': roothash,
                           
                           }
        valid_hash = False
        if len(roothash) == 40:
            try:
                _ = int(roothash, 16)
                valid_hash = True
            except (Exception):
                pass
        if valid_hash:
            template = jinja_environment.get_template('index_hash.html')
        else:
            template = jinja_environment.get_template('index_invalid.html')
        self.response.out.write(template.render(template_values))
            

app = webapp2.WSGIApplication([
                               ('/', MainPage),
                               ('/start.html', StartPage),
                               ('/info.html', InfoPage),
                               ('/(.+)', Hash)
                               ], debug=True)