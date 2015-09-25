# coding: UTF-8

users = {"camaro": 200, "tahoe": 450, "cuda": 750}

for key, value in users.iteritems():
    print "key %s value: %d" % (key, value)

for key in users.iterkeys():
    print key

for value in users.itervalues():
    print value
