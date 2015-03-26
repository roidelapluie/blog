import hashlib
def colorize(txt):
    m = hashlib.md5()
    m.update(txt)
    return '#%s0' % m.hexdigest()[1:6]

