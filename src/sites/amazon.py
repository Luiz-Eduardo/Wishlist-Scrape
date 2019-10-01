class Amazon:
    def fetch(self, link):
        # Here you fetch on the link given the information you want
        # then, after fetched, return a dictionary with the following
        # keys:
        # dict['title'] -> product title, need to be a String
        # dict['price'] -> product price, need to be a Float
        
        # Open the link
        try:
            response = requests.get(link)
            page = response.text
        except Exception as e:
            print("Link Error: %s" % link)
            infos = {'title': link.split('/')[-1], 'price': 0.00, 'discount': False}
            return infos

        infos = dict()
        soup = bSoup(page, 'html.parser')

        # Title fetch
        try:
            infos['title'] = soup.h1.string.replace('\n', '').replace('\t', '')
        except Exception as e:
            raise Exception('No title found on the link: %s' % link)

        # Price fetch
        try:
            infos['price'] = soup.fieldset.span.span['content']
            infos['discount'] = False

        except Exception as e:
            raise Exception('No price found on link: %s' % link)

        # Convert price to a float
        infos['price'] = float(infos['price'])

        # Everything went OK by this point
        self.fetched = True
        return infos