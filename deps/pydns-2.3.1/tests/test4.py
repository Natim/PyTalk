#!/usr/bin/python

import sys ; sys.path.insert(0, '..')

import DNS

DNS.ParseResolvConf()

print DNS.mxlookup("connect.com.au")
