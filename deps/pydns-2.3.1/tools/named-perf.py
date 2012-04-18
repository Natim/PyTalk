#!/opt/python/bin/python

servers = [ "192.92.129.1",
	"192.189.54.17", # yarrina
	    "192.189.54.33", # warrane
	    "203.8.183.1",   # yalumba
	    "192.189.54.65", # gnamma 
	    "128.250.1.21",  # munnari

	  ]

lookups = [ ( 'munnari.oz.au', 'A' ),
            ( 'connect.com.au', 'SOA' ),
            ( 'parc.xerox.com', 'MX' ),
	    ( 'bogus.example.net', 'A'),
	  ]

rpts = 5

def main():
	import DNS, timing, socket, time
	res = {}
	for server in servers:
	    res[server] = [100000,0,0,0] # min,max,tot,failed
	for what,querytype in lookups:
	    for count in range(rpts):
		for server in servers:
		    d = DNS.DnsRequest(server=server,timeout=1)
		    fail = 0
		    timing.start()
		    try:
			r=d.req(name=what,qtype=querytype)
		    except DNS.Error:
			fail = 1
		    timing.finish()
		    if fail:
			res[server][3] =  res[server][3] + 1
			print "(failed)",res[server][3]
		    if 0:
		      if r.header['ancount'] == 0:
			print "WARNING: Server",server,"got no answers for", \
				what, querytype
		    t = timing.milli()
		    print server,"took",t,"ms for",what,querytype
		    res[server][0] = min(t,res[server][0])
		    res[server][1] = max(t,res[server][1])
		    res[server][2] = res[server][2] + t
	for server in servers:
	    queries = rpts * len(lookups)
	    r = res[server]
	    print "%-30s %2d/%2d(%3.2f%%) %dms/%dms/%dms min/avg/max" % (
			socket.gethostbyaddr(server)[0], 
			queries - r[3], queries, 
			((queries-r[3])*100.0)/queries,
			r[0],
			r[2] / queries,
			r[1])

if __name__ == "__main__":
    main()
