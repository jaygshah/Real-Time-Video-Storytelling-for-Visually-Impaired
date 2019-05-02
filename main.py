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
    # tagged_sentence = sentence_maker.from_keyword_list(['kitchen', 'floor', 'human', 'cooking'])
    
    ###############################################
    
    # labels = request.args.get('labels')
    # if labels == None or len(labels) == None:
    #     return 'empty query parameters'
    # labels = labels.split(",")
    ###############################################

    labels = request.args.get('labels')
    labels = labels.split(",")
    path = request.args.get('video_file_path')
    if path == None or len(path) == None or labels == None or len(labels) == None:
        return 'empty query parameters'
    
    # tags = parms[0].split(",")
    ###############################################


    sentence_maker = SentenceMaker()
    tagged_sentence = sentence_maker.from_keyword_list(labels)
    sentence_tools = SentenceTools()
    output = sentence_tools.detokenize_tagged(tagged_sentence)
    logging.info(output)

    print(output)
    # output = jsonify(output)

    ref = db.reference(path)
    ref.set(output)
    # ref.push({
    #     'mac-address': mcadd,
    #     'file-name': filename,
    #     'sentence': output,
    # })

    return output

@app.errorhandler(500)  
def server_error(e):
    print(e)
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