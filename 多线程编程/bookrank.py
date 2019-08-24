from atexit import register
from re import compile
from threading import Thread
from time import ctime
from urllib.request import urlopen as uopen
import ssl


REGEX = compile('#([/d,]+) in Books')
AMZN = 'http://amazon.com/dp/'
ISBNs = {
    '0132269937': 'Core Python Programming',
    '0132356139': 'Python Web Development with Django',
    '0137143419': 'Python Fundamentals'
}
context = ssl._create_unverified_context()

def getRank(isbn):
    page = uopen('%s%s' %(AMZN, isbn), context = context)
    data = page.read()
    page.close()
    return REGEX.findall(data)[0]


def _showRanking(isbn):
    print('- %r ranked %s' %(ISBNs[isbn], getRank(isbn)))


def main():
    print('At', ctime(), 'on Amazon')
    for isbn in ISBNs:
        _showRanking(isbn)

@register
def _atexit():
    print('All Done at:', ctime())


if __name__ == '__main__':
    main()