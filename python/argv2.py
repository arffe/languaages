#!/usr/bin/env python
from sys import argv
script, user_name = argv
prompt = "enter something here > "

print "Hi! {0}, I'm the {1} script".format(user_name, script)
print "do you like me {0}?".format(user_name)
likes = raw_input(prompt)

print "you said '{0}' about liking me".format(likes)
print "you said %r about liking me" % likes
