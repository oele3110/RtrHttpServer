from bottle import redirect, request, route, run, static_file, template
from subprocess import Popen, PIPE, STDOUT

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

	val = valThread.validatePrefix(prefix, length, asn)

	return template('{{val}}', val=val)

class Validator(threading.Thread):

	p = None

	def __init__(self):
		threading.Thread.__init__(self)
		print "start validator"
		Validator.p = Popen(['/home/skims/git/RtrHttpServer/validator', 'rpki-validator.realmv6.org', '8282'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
		print "validator started"

	def validatePrefix(sefl, prefix, length, asn):

		Validator.p.stdin.write(prefix + " " + length + " " + asn + "\n")

		one_line_output = Validator.p.stdout.readline()

		return one_line_output


valThread = Validator()
valThread.start()

run(host='0.0.0.0', port=5003)
