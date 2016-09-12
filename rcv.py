#!/usr/bin/env python
import pika

rcvcount = 0

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

print ' [*] Waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
#    print " [x] Received %r" % (body,)
    global rcvcount
    rcvcount = rcvcount + 1

    if (rcvcount < 1000 or rcvcount % 1000 == 0):
 		print "received", rcvcount, body

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

channel.start_consuming()
