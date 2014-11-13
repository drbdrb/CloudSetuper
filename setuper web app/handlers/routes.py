#!/usr/bin/env python
# -*- coding: utf-8 -*-

from joinhandler import JoinHandler
from loginhandler import LoginHandler, LogoutHandler
from indexhandler import IndexHandler
from uploadfilehandler import UploadFileHandler
from helphandler import HelpHandler, HelpCliHandler
from abouthandler import AboutHandler
from contacthandler import ContactHandler
from sockethandler import SocketHandler
import os
import tornado.web


routes = [
    (r"/", IndexHandler),
    (r"/ws", SocketHandler),
    (r"/join", JoinHandler),
    (r"/login", LoginHandler),
    (r"/logout", LogoutHandler),
    (r"/upload", UploadFileHandler),
    (r"/help", HelpHandler),
    (r"/help/cli", HelpCliHandler),
    (r"/about", AboutHandler),
    (r"/contact", ContactHandler),
    (r'/static', tornado.web.StaticFileHandler, {'path': os.path.join(os.getcwd(), "static")})
]
