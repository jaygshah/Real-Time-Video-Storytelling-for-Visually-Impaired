'''
##########################################################################
PUB SUB SERVER SUBSCRIBER
##########################################################################
import os
from google.cloud import pubsub_v1

subscriber = pubsub_v1.SubscriberClient()
topic_name = 'projects/{project_id}/topics/{topic}'.format(
    project_id=os.getenv('GOOGLE_CLOUD_PROJECT'),
    topic='RTVSTS',  # Real-Time-Video-Story-Telling-Service
)
subscription_name = 'projects/{project_id}/subscriptions/{sub}'.format(
    project_id=os.getenv('GOOGLE_CLOUD_PROJECT'),
    sub='RTVSTS-SUB',  # Real-Time-Video-Story-Telling-Service_Subscription
)
subscriber.create_subscription(
    name=subscription_name, topic=topic_name)

def callback(message):
    print(message.data)
    message.ack()

future = subscriber.subscribe(subscription_name, callback)
##########################################################################
##########################################################################
'''
from randomsentence.sentence_maker import SentenceMaker
from randomsentence.sentence_tools import SentenceTools
sentence_maker = SentenceMaker()
tagged_sentence = sentence_maker.from_keyword_list(['kitchen', 'floor', 'human', 'cooking'])
# tagged_sentence = sentence_maker.from_keyword_list(message.data)
sentence_tools = SentenceTools()
output = sentence_tools.detokenize_tagged(tagged_sentence)
print(output)
# from randomsentence.grammar_check import GrammarCorrector
# corrector = GrammarCorrector()
# print(corrector.correct(output))
# A sentence with an error in the Hitchhiker’s Guide to the Galaxy'

# from randomsentence.randomsentence import RandomSentence
# from randomsentence.sentence_tools import SentenceTools
# random_sentence = RandomSentence()
# tagged_sentence = random_sentence.get_tagged_sent()
# print(tagged_sentence)
# sentence_tools = SentenceTools()
# print(sentence_tools.detokenize_tagged(tagged_sentence))

from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return output


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]





# import webapp2


# class MainPage(webapp2.RequestHandler):
#     def get(self):
#         self.response.headers['Content-Type'] = 'text/plain'
#         self.response.write(output)


# app = webapp2.WSGIApplication([
#     ('/', MainPage),
# ], debug=True)

with open("story.txt", "w") as text_file:
    text_file.write(output)