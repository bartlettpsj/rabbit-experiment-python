#!/usr/bin/env python
import pika
import sys

print "arguments", len(sys.argv), sys.argv

if (len(sys.argv) > 1):
	msg = sys.argv[1]
else:
	msg = "hello world!"

# hope its a number
if (len(sys.argv) > 2):
	count = int(sys.argv[2])
else:
	count = 1


connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

for i in range(count):

	msg2 = msg + str(i)
	channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=msg2)

print " [x] Sent", msg, count, "times"

connection.close()