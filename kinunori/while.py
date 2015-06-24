# coding: UTF-8
# while でループ処理

n = 0

# n が 10未満の場合はループ
while n < 10:
	print n
	n += 1
# while の条件が偽の場合はelseの処理
else: 
	print "end of 1st while"

p = 0
while p < 10:
	# p が 3の時は処理をスキップ
	if p == 3:
		p += 1
		continue
        # p が 6になったら処理を抜ける
	if p == 6:
		break
	print p
	p += 1

