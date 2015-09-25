# coding: UTF-8

f = open('readme.txt', 'w')
readme_txt = u"リードミー"
f.write(readme_txt.encode('utf-8'))
f.close

print readme_txt
f = open('readme.txt', 'r')
print f.read().decode('utf-8')
f.close
