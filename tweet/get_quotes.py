import urllib.request
import requests
from urllib.parse import urlparse
import re


class ProverbsAntjan:
    """
    This will read the antjan api
    """

    API_URL = "http://proverbs-app.antjan.us/random"

    def _hit_api(self):
        return urllib.request.urlopen(self.API_URL).read()

    def _get_author(self, quote):
        var = requests.get(r'http://www.google.com/search?q="%s"&btnI' % quote)
        parsed_uri = urlparse( var.url )
        domain = '{uri.netloc}'.format(uri=parsed_uri)
        print('{uri.netloc}'.format(uri=parsed_uri))

        unwanted = ("\.com", "www\.", "blog\.")
        for s in unwanted:
            domain = re.sub(s, '', domain)

        return domain

    def get_quote(self):
        random_quote = self._hit_api()
        #domain = self._get_author(random_quote)
        #return "%s - %s" % (random_quote, domain)
        return random_quote


if __name__ == "__main__":
    p = ProverbsAntjan()
    print(p.get_quote())
    #print(p._get_author("The Best Code is No Code at All"))

