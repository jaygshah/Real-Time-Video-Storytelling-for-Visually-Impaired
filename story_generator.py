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
tagged_sentence = sentence_maker.from_keyword_list(['presentation', 'public speaking', 'politics', 'orator', 'speaker', 'audience', 'city council', 'conversation','lecture', 'official', 'speech'])
# tagged_sentence = sentence_maker.from_keyword_list(message.data)
sentence_tools = SentenceTools()
output = sentence_tools.detokenize_tagged(tagged_sentence)
print(output)

# from randomsentence.grammar_check import GrammarCorrector
# corrector = GrammarCorrector()
# print(corrector.correct(output))
# # 'A sentence with an error in the Hitchhiker’s Guide to the Galaxy'



# from randomsentence.randomsentence import RandomSentence
# from randomsentence.sentence_tools import SentenceTools
# random_sentence = RandomSentence()
# tagged_sentence = random_sentence.get_tagged_sent()
# print(tagged_sentence)
# sentence_tools = SentenceTools()
# print(sentence_tools.detokenize_tagged(tagged_sentence))


with open("story.txt", "w") as text_file:
    text_file.write(output)