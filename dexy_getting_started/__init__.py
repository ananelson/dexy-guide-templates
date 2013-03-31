from dexy.template import Template
import os

for i in xrange(14):
    key = "t%02d" % i
    if not key in Template.plugins:
        args = {
                'help' : "Help for %s" % key,
                'contents-dir' : os.path.join(os.path.dirname(__file__), "%s-template" % key)
                }
        Template.register_plugin(key, 'Template', args)
