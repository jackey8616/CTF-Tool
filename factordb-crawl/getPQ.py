from __future__ import print_function
import sys, re, requests

if sys.version_info >= (3, 0):
    long = int

def getPQ(N):
    r = requests.post('http://factordb.com/index.php?query=' + N)
    td = re.compile('<td><a href="index\.php\?id=.*</td>').search(r.text).group(0)
    split = re.compile('<\/sub> = <a').split(td)
    p = re.compile('"index\.php\?id=.*"><font').search(split[0]).group(0)[14:-7]
    q = re.compile('"index\.php\?id=.*"><font').search(split[1]).group(0)[14:-7]
    return (long(p), long(q))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Input a N to get p, q')
        exit(0)
    
    n = sys.argv[1]
    p, q = getPQ(n)
    print('p= %d, q= %d' % (p, q))

