#! /bin/python

import os.path 

# tornado imports
import tornado.httpserver 
import tornado.ioloop 
import tornado.options 
import tornado.web

# define a port for serving requests. Heroku uses 5000
from tornado.options import define, options
define("port", default=5000, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler): 
    def get(self):
        self.render('index.html')

if __name__ == '__main__': 
    tornado.options.parse_command_line() 
    app = tornado.web.Application(
        handlers=[(r'/', IndexHandler)], 
        # if you want to use any templates, uncomment the below line
        # create a new directory called templates and move your templates in that
        # template_path=os.path.join(os.path.dirname(__file__), "templates"), 
        #static_path=os.path.join(os.path.dirname(__file__), "static"), 
        debug=True
        )
    # set debug to False when running on production/Heroku!
    http_server = tornado.httpserver.HTTPServer(app) 
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()        