# cording: UTF-8

sales = [13, 23, 321, 456]
sum = 0

for sale in sales:
	sum += sale
else:
	print sum

print sale

for i in range(10):
	if i == 3:
		continue
	if i == 5:
		break
	print i