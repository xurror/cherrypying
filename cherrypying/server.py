import os
import cherrypy

from controllers import Root, Compute

if __name__ == "__main__":
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/compute': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './static'
        }
    }
    root = Root()
    root.compute = Compute()
    cherrypy.quickstart(root, '/', conf)
