import webapp2
import jinja2
import os

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
class EnterInfoHandler(webapp2.RequestHandler):
    def get(self):  # for a get request
        the_variable_dict = {
            "greeting": "Welcome!!!", 
            "adjective": "splendid"
        }
        
        locations_template = the_jinja_env.get_template('templates/locations.html')
        self.response.write(locations_template.render(the_variable_dict))


class ShowMapHandler(webapp2.RequestHandler):
    def get(self):  # for a get request
        mappage_template = the_jinja_env.get_template('templates/mappage.html')
        the_variable_dict = {
            "line1": "Hurrah for Utsab!", 
            "line2": "Hurrah!!!!!!!!", 
            "img_url": "http://www.atozpictures.com/admin/uploads/2016/11/cute-cockatiel-wallpapers.jpg"
        }
        self.response.write(mappage_template.render(the_variable_dict))
        
    def post(self):
        self.redirect("/showmap")
            


app = webapp2.WSGIApplication([
    ('/', EnterInfoHandler),
    ('/showmap', ShowMapHandler),
], debug=True)