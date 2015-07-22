# cofing: UTF-8

users = {"taguchi":200, "fkoji":300, "dotinstall":500}

for key, value in users.iteritems():
	print key
for key, value in users.iteritems():
	print value

print "-----"

for key, value in users.iteritems():
        print "key: %s value: %d" % (key, value)
