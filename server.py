from bottle import redirect, request, route, run, static_file, template
from subprocess import Popen, PIPE, STDOUT
import sys

import threading

valThread = None


@route('/')
def index():
	return static_file('index.html', root='./')

@route('/request', method='GET')
def index():
	prefix = request.query.prefix
	length = request.query.length
	asn = request.query.asn

	# after getting prefix, length, asn via http get validate prefix
	val = valThread.validatePrefix(prefix, length, asn)
	# return validated line to template
	return template('{{val}}', val=val)

class Validator(threading.Thread):

	p = None

	def __init__(self):
		threading.Thread.__init__(self)
		print "start validator"
		Validator.p = Popen(['/home/skims/git/RtrHttpServer/validator', 'rpki-validator.realmv6.org', '8282'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
		print "validator started"

	def validatePrefix(sefl, prefix, length, asn):
		# print correct snytax to stdin
		Validator.p.stdin.write(prefix + " " + length + " " + asn + "\n")
		# get result from validator
		one_line_output = Validator.p.stdout.readline()
		# return line to http server
		return one_line_output


host = ""
port = 0

# start routine
if len(sys.argv) < 5:
	print "wrong usage, use:\npython server.py -h host -p port"
else:
	for i in range(1, len(sys.argv)):
		if(sys.argv[i] == "-h"):
			host = sys.argv[i+1]
		if(sys.argv[i] == "-p"):
			port = int(sys.argv[i+1])

	# start new validator thread
	valThread = Validator()
	valThread.start()
	
	# run bottle http server
	run(host=host, port=port)
