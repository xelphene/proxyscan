
import sys
import httplib
import re

success = []

class FileParseError(Exception):
	pass

def load_proxies(path='proxies'):
	proxies = []
	lineno=0
	for line in open(path):
		lineno+=1
		if line.startswith('#'):
			continue
		line = line.strip()
		parts = line.split(' ')
		if len(parts)!=2:
			raise FileParseError('Proxies file %s line %d is invalid: Incorrect number (%d) of space-separated parts.' % (path,lineno, len(parts)))
		if not parts[1].isdigit():
			raise FileParseError('Proxies file %s line %d is invalid: Port number (%s) is not valid.' % (path, lineno, repr(parts[1])))
		proxies.append((parts[0], int(parts[1])))
	return proxies

def load_interesting_hosts(path='interesting_hosts'):
	hosts = []
	lineno=0
	for line in open(path):
		lineno+=1
		if line.startswith('#'):
			continue
		line = line.strip()
		hosts.append(line)
	return hosts
	
def load_interesting_ports(path='interesting_ports'):
	ports = []
	lineno=0
	for line in open(path):
		lineno+=1
		if line.startswith('#'):
			continue
		line = line.strip()
		if not line.isdigit():
			raise FileParseError('Ports file %s line %d is invalid: Port number (%s) is not valid.' % (repr(path), lineno, repr(line)))
		ports.append(int(line))
	return ports

def doreq(proxyhost, proxyport, host, port):
	dest = '%s:%s' % (host,port)

	headers = {
		'Host': dest
	}

	c = httplib.HTTPConnection(proxyhost,proxyport, timeout=3)
	try:
		c.request('CONNECT', dest, None, headers)
		r = c.getresponse()
		if r.status>=200 and r.status<300:
			prefix = '***'
			success.append((
				proxyhost, proxyport,
				host, port, r.status
			))
		else:
			prefix = '   '
	
		print '%s %15s  %-5s %15s  %-5s %-3s' % (prefix, proxyhost, proxyport, host, port, r.status)
	except Exception, e:
		print '%s %15s  %-5s %15s  %-5s %-3s' % ('   ', proxyhost, proxyport, host, port, e)
		
def main():
	proxies = load_proxies()
	interesting_hosts = load_interesting_hosts()
	interesting_ports = load_interesting_ports()
	
	for (proxyhost, proxyport) in proxies:
		for host in interesting_hosts:
			for port in interesting_ports:
				doreq(proxyhost, proxyport,host,port)

	print '--- successful connection summary ---'
	for (proxyhost, proxyport, host, port, status) in success:
		print '%s %15s  %-5s %15s  %-5s %-3s' % ('   ', proxyhost, proxyport, host, port, status)

if __name__ == '__main__':
	main()

	