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
        handlers=[(r'/', IndexHandler),
        (r'/(.*)', tornado.web.StaticFileHandler, 
            {'path': os.path.dirname(__file__)})],
        debug=True
        )
    # set debug to False when running on production/Heroku!
    http_server = tornado.httpserver.HTTPServer(app) 
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()        