import urllib2
from collections import Counter


def find_most_occ_char(input):

    wc = Counter(input)
    s = max(wc.values())
    i = wc.values().index(s)

    print wc.items()[i]

k = raw_input("Website URL")
content = urllib2.urlopen(k).read()
find_most_occ_char(content)

