import os
import json
import cherrypy
from jinja2 import Template, Environment, FileSystemLoader

localDir = os.path.dirname(__file__)
absDir = os.path.join(os.getcwd(), localDir)
current_dir = os.path.dirname(os.path.abspath(__file__))

#setup some rendering templates
env = Environment(loader=FileSystemLoader(current_dir), trim_blocks=True)

class Root(object):
    @cherrypy.expose
    def index(self):
        template_index = env.get_template("views/index.html")
        return template_index.render()

@cherrypy.expose
class Compute(object):

    def GET(self):
        template_index = env.get_template("views/compute.html")
        return template_index.render()

    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def POST(self):
        mylist = []
        sm_list = []
        input_json = cherrypy.request.json
        for i in input_json:
            for key, val in i.items():
                sm_list.append(val)
            mylist.append(sm_list)
            sm_list = []

        cherrypy.log("Post request param type: \n" + str(mylist))
        return input_json

    def PUT(self, another_string):
        pass
        # cherrypy.session['mystring'] = another_string

    def DELETE(self):
        pass
        # cherrypy.session.pop('mystring', None)