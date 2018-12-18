import re
from urllib.request import *

class ML():
    def fetch(self, link):
        '''
        Will return a Dictionary with:
        - title -> String
        - price -> Float
        - discount -> Boolean
        '''

        patterns = {
            'title': re.compile(r'''<h1 class="item-title__primary\s">\n\t\t(.+)\n\t</h1>'''),
            'regular_price': re.compile(r'''class="price-tag-symbol"\scontent="(.+)"'''),
        }

        # Header required to open terabyteshop pages with urllib
        hdr = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'
        }

        # Open the link
        try:
            page = urlopen(Request(link, headers = hdr)).read().decode('UTF-8')
        except Exception as e:
            print(e)

        infos = dict()
        # Title fetch
        title_re = patterns['title'].search(page)

        try:
            infos['title'] = title_re.group(1)
        except Exception as e:
            raise Exception('No title found on the link: %s' % link)

        # Price fetch
        regular_price_re = patterns['regular_price'].search(page)
        try:
            infos['price'] = regular_price_re.group(1)
            infos['discount'] = False
        except Exception as e:
            raise Exception('No price found on link: %s' % link)

        # Convert price to a float
        infos['price'] = float(infos['price'])

        # Everything went OK by this point
        self.fetched = True
        return infos
