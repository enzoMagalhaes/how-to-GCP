
from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()
topic_name = 'projects/innate-octagon-371318/topics/gcp-course-topic1'
msg = bytes("this message was delivered from python!",'utf-8')

publisher.publish(topic_name,msg)
