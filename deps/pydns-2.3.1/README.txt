Release 2.3 Mon May  6 16:18:02 EST 2002

This is a another release of the pydns code, as originally written by 
Guido van Rossum, and with a hopefully nicer API bolted over the
top of it by Anthony Baxter <anthony@interlink.com.au>. 

This code is released under a Python-style license. 

I'm making this release because there hasn't been a release in a 
heck of a long time, and it probably deserves one. I'd also like to
do a substantial refactor of some of the guts of the code, and this
is likely to break any code that uses the existing interface. So
this will be a release for people who are using the existing API...

There are several known bugs/unfinished bits

- processing of AXFR results is not done yet.
- doesn't do IPv6 DNS requests (type AAAA) 
- docs, aside from this file
- all sorts of other stuff that I've probably forgotten.
- MacOS support for discovering nameservers
- the API that I evolved some time ago is pretty ugly. I'm going
  to re-do it, designed this time.

Stuff it _does_ do:
- processes /etc/resolv.conf - at least as far as nameserver directives go.
- tries multiple nameservers.
- nicer API - see below.
- returns results in more useful format.
- optional timing of requests.
- default 'show' behaviour emulates 'dig' pretty closely.
  

To use:

import DNS
reqobj=DNS.Request(args)
reqobj.req(args)

args can be a name, in which case it takes that as the query, and/or a series
of keyword/value args. (see below for a list of args)

when calling the 'req()' method, it reuses the options specified in the
DNS.Request() call as defaults.

options are applied in the following order:
  those specified in the req() call
  or, if not specified there,
  those specified in the creation of the Request() object
  or, if not specified there,
  those specified in the DNS.defaults dictionary

name servers can be specified in the following ways:
- by calling DNS.DiscoverNameServers(), which will load the DNS servers
    from the system's /etc/resolv.conf file on Unix, or from the Registry
    on windows.
- by specifying it as an option to the request
- by manually setting DNS.defaults['server'] to a list of server IP
    addresses to try
- XXXX It should be possible to load the DNS servers on a mac os machine, 
    from where-ever they've squirrelled them away

name="host.do.main"   # the object being looked up
qtype="SOA"           # the query type, eg SOA, A, MX, CNAME, ANY
protocol="udp"        # "udp" or "tcp" - usually you want "udp"
server="nameserver"   # the name of the nameserver. Note that you might
                      # want to use an IP address here
rd=1                  # "recursion desired" - defaults to 1.
other: opcode, port, ...

There's also some convenience functions, for the lazy:

to do a reverse lookup:
>>> print DNS.revlookup("192.189.54.17")    
yarrina.connect.com.au

to look up all MX records for an entry:
>>> print DNS.mxlookup("connect.com.au")
[(10, 'yarrina.connect.com.au'), (100, 'warrane.connect.com.au')]

Documentation of the rest of the interface will have to wait for a 
later date. Note that the DnsAsyncRequest stuff is currently not
working - I haven't looked too closely at why, yet.

There's some examples in the tests/ directory - including test5.py,
which is even vaguely useful. It looks for the SOA for a domain, checks
that the primary NS is authoritative, then checks the nameservers
that it believes are NSs for the domain and checks that they're
authoritative, and that the zone serial numbers match.

see also README.guido for the original docs.

comments to me, anthony@interlink.com.au, or to the mailing list,
pydns-developer@lists.sourceforge.net.

bugs/patches to the tracker on SF - 
               http://sourceforge.net/tracker/?group_id=31674
