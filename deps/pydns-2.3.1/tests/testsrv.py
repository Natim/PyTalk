#!usr/bin/python

import sys ; sys.path.insert(0, '..')

import DNS
# automatically load nameserver(s) from /etc/resolv.conf
# (works on unix - on others, YMMV)
DNS.ParseResolvConf()

r=DNS.Request(qtype='srv')
res = r.req('_ldap._tcp.openldap.org')
res.show()
print res.answers
