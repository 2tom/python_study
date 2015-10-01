# cording: UTF-8

sales = [13, 23, 321, 456]
sum = 0

for sale in sales:
    sum += sale
else:
    print sum

print "sale"
print sale

for i in range(10):
    if i == 3:
        continue
    if i == 5:
        break
    print i

print "----------------"

for i in range(5):
    for j in range(5):
        if i == 3:
            break
        print "j: %d" % j
    print "i: %d" % i
