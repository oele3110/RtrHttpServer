This is a HTTP Validator for RPKI Origin Prefix Validation.

## Prerequisites:

### Bottle: Python Web Framework

You need to install the Bottle: Python Web Framework http://bottlepy.org/

<pre>
pip install bottle
</pre>

### RTRLib

You need to install the C RTRLib http://rpki.realmv6.org/

## Usage

### Run

<pre>python server.py -h host -p port</pre>

### Request

To make a request go to

http://host/request?prefix=[IP-PREFIX]&length=[LENGTH]&asn=[ASN]

### example:

http://tanger.imp.fu-berlin.de:5003/request?prefix=103.10.232.0&length=24&asn=1280

## Return Value

The Server returns a line constructred as follows:

validity | prefix length asn [ | roa-asn roa-prefix roa-minlenght roa max-lenght, ... ]

### unknown:

-1|103.10.141.0 22 32590

### invalid:

0|103.10.232.0 24 1285|1283 103.10.232.0 24 24,1280 103.10.232.0 24 24,1281 103.10.232.0 24 24

### valid

1|103.10.232.0 24 1280|1283 103.10.232.0 24 24,1280 103.10.232.0 24 24,1281 103.10.232.0 24 24
