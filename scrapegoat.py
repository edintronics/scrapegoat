from bs4 import BeautifulSoup
import urllib2
import random

# IE10 - Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)
# Chrome - Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36
# Chrome (WinV2) - Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36
# Safari iOS10 - Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0 Mobile/14C92 Safari/602.1
# GSA on iOS10 - Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/22.0.141836113 Mobile/14C92 Safari/600.1.4


class Goat:
    """Tell the goat which pasture to graze and it returns with a pot of soup"""
    
    def __init__(self,pasture):
        self.hats =["Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0 Mobile/14C92 Safari/602.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/22.0.141836113 Mobile/14C92 Safari/600.1.4"]

        self.food = BeautifulSoup(urllib2.urlopen(urllib2.Request(pasture,headers={"user-agent":self.putHatOn()})),"html.parser")
        
    def putHatOn(self):
        return self.hats[random.randrange(0,5)]
