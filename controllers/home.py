import json

import cherrypy
import redis
import os

import cherrypy
import time
from jinja2 import Environment, FileSystemLoader

from download_bhav_script import getBhav

CUR_DIR = os.path.dirname(os.path.abspath(__file__))
env=Environment(loader=FileSystemLoader(CUR_DIR),
trim_blocks=True)
from controllers.base import BaseController


class HomeController(BaseController):

    @cherrypy.expose()
    def index(self):
        redis_server = getBhav()
        bseobjs = redis_server.get('bhavcopy')
        bseobjtop = redis_server.get('bsetop')
        bsedatestr = redis_server.get('datestr')
        bseobjs = json.loads(bseobjs)
        bseobjtop = json.loads(bseobjtop)
        bsedatestr = time.strftime("%d %b %Y",time.strptime(
                bsedatestr, "%Y-%m-%d %H:%M:%S.%f"
            )
        )
        return self.render_template(
            'home/index.html',
            {
                'list_header' : bsedatestr,
                'bseobjs' : bseobjs,
                'bseobjtop' : bseobjtop,
                'site_title' : "Stock list"
            }
        )

