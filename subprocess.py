from subprocess import Popen, PIPE, STDOUT


input1 = "103.10.124.0 24 32590\n"
input2 = "103.10.232.0 24 1280\n"

p = Popen(['/home/skims/git/rtrHttpServer/validator', 'rpki-validator.realmv6.org', '8282'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)




p.stdin.write(input1)

one_line_output = p.stdout.readline()

print one_line_output

p.stdin.write(input2)

one_line_output = p.stdout.readline()

print one_line_output
