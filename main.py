# [START gae_flex_quickstart]
import logging

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate('video-storytelling-37f0c-firebase-adminsdk-skn9g-fd959c41fa.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://jayoutput.firebaseio.com/'
})

from flask import Flask
from flask import request
from flask import jsonify
from randomsentence.sentence_maker import SentenceMaker
from randomsentence.sentence_tools import SentenceTools

app = Flask(__name__)

@app.route('/')
def hello():    
    sentence_maker = SentenceMaker()
    # tagged_sentence = sentence_maker.from_keyword_list(['kitchen', 'floor', 'human', 'cooking'])
    labels = request.args.get('labels')

    if labels == None or len(labels) == None:
        return 'empty query parameters'
    # parms = labels.split(">")
    labels = labels.split(",")
    # tags = parms[0].split(",")
    # macadd = parms[1]
    # filename = parms[2]
    # tagged_sentence = sentence_maker.from_keyword_list(request.args.get('labels'))

    tagged_sentence = sentence_maker.from_keyword_list(labels)
    # # tagged_sentence = sentence_maker.from_keyword_list(message.data)
    sentence_tools = SentenceTools()
    output = sentence_tools.detokenize_tagged(tagged_sentence)
    logging.info(output)
    print(output)
    # output = jsonify(output)

    ref = db.reference('/')
    ref.push({
        # 'macadd': 'macadd',
        # 'filename': filename,
        'sentence': output,
    })

    return output

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_flex_quickstart]