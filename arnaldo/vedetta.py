#! /usr/bin/env python
# vim: set fileencoding=utf-8:

import tornado.httpserver
import tornado.ioloop
import tornado.web

import threading

from arnaldo.brain import brain
from arnaldo import dimme
import bcrypt

def htmella(s, code, content, msg):
    s.clear()
    s.set_status(code)
    s.set_header('Content-Type', content)
    s.finish(msg)


class onore(tornado.web.RequestHandler):
        def get(self):
            htmella(self,200,'text/html',"<html><h1>ONORE AL COMMENDATORE!</h1></html>")

class sputa(tornado.web.RequestHandler):
        def get(self):
            htmella(self,404,'text/html',"che ti levi di ulo?")

        def post(self):

            author  = self.get_argument("chie")
            message = self.get_argument("msg")

            if message:
                bazza = self.get_argument("hasho")
                print "%s,%s,%s" % (author, message, bazza)

                cecco = bcrypt.verify(message + brain.get("httppasswd"), str(bazza))
                if cecco:
                    if author:
                        out = (author,message)
                    else:
                        out = message
                    dimme.send(out)
                    self.redirect("/")
                else:
                     htmella(self, 404, 'text/html', "che ti levi di ulo?")

class Vedetta(threading.Thread):
    def run(self):
        accatitipi = tornado.web.Application([(r"/", onore), (r"/catarro", sputa)])
        http_server = tornado.httpserver.HTTPServer(accatitipi)
        http_server.listen(50102, '0.0.0.0')
        tornado.ioloop.IOLoop.instance().start()

    def stop(self):
        tornado.ioloop.IOLoop.instance().stop()

