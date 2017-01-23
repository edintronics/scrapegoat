from bs4 import BeautifulSoup
import urllib
import random

# IE10 - Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)
# Chrome - Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36
# Chrome (WinV2) - Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36
# Safari iOS10 - Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0 Mobile/14C92 Safari/602.1
# GSA on iOS10 - Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/22.0.141836113 Mobile/14C92 Safari/600.1.4

#Things to do:
# Make the goat reuseable i.e. feeding it URLs and having it open them with the same user-agent
# Commit python3 version

class Goat:
    """ **Tell the goat which pasture to graze and it returns with a pot of soup**
    
    Creates an object (Webgoat) with a URL target. The Goat will open the URL with a randomised user-agent from the pool of five options or
    you can specify the user-agent. It will then parse and return the target page as a BeautifulSoup object available at Goat.soup 
    
    User-agent options:
    IE
    Chrome
    Chrome2 (Different windows version from the last)
    Safari
    Google (the iOS search app)
    
    """
    
    def __init__(self,pasture,ua=None):
        
        self.hats = {"IE":"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
        "Chrome":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        "Chrome2":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        "Safari":"Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0 Mobile/14C92 Safari/602.1",
        "Google":"Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/22.0.141836113 Mobile/14C92 Safari/600.1.4"}
        self.pudding = self.putHatOn(ua)
        print(self.pudding)
        self.soup = BeautifulSoup(urllib.request.urlopen(urllib.request.Request(pasture,headers={"user-agent":self.pudding})),"html.parser")
        
    def putHatOn(self,ua):
        if ua == None:
            return list(self.hats.values())[random.randrange(0,5)]
        else:
            return self.hats[ua]
