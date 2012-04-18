# 
# From: KevinL <darius@bofh.net.au>
#   A simple dns answer cache - it's author notes:
#     "It's probably really bodgy code, tho - it was my early python..."
#   So don't send him abusive messages if you hate it. 
#
class DNSCache:
    """
    Covers the DNS object, keeps a cache of answers.  Clumsy as hell.
    """
    forCache = {}
    revCache = {}
    # cache failures for this long, in seconds
    negCache = 3600

    def __init__(self):
       import DNS
       DNS.ParseResolvConf()

    def lookup(self,IP = None,name = None):
        import DNS
	now = time.time()
        if (not IP) and (not name):
            return None
        if IP:
            if type(IP) != type(''):
                return None
            a = string.split(IP, '.')
            a.reverse()  
            name = string.join(a, '.')+'.in-addr.arpa'
            cache = self.revCache
            qt = 'ptr'
        else:
            if type(name) != type(''):
                return None
            cache = self.forCache
            qt = 'a'
        if cache.has_key(name):
	    # Check if it's timed out or not
            if cache[name][1] < now:
                del(cache[name])
            else:
                return(cache[name][0])
        x = DNS.DnsRequest(name,qtype=qt)
        try:
            x.req()
        except:
            return 'Timeout'
        if len(x.response.answers) > 0:
            cache[name] = ( x.response.answers[0]['data'], x.time_finish + 
			    x.response.answers[0]['ttl'])
        else:
            cache[name] = (None,now+self.negCache)
        return cache[name][0]

