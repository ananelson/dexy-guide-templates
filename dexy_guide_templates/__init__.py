from dexy.template import Template
import os

template_dir = os.path.dirname(__file__)

n = len([f for f in os.listdir(template_dir) if f.endswith("-template")])

for i in xrange(n):
    key = "t%02d" % i
    if not key in Template.plugins:
        args = {
                'help' : "Help for %s" % key,
                'contents-dir' : os.path.join(template_dir, "%s-template" % key)
                }
        Template.register_plugin(key, 'Template', args)
