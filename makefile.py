f = open('jack.txt', 'w')
for i in range(200):
    f.write('%03d) All work and no play makes Jack a dull boy.\n' % i)
f.close()
