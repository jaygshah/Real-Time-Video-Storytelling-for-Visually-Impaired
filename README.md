We propose to build an end-to-end cloud-based service that would be providing real-time audio descriptions of videos streamed via a device. It will consist of video uploads, analysis, and audio story-telling delivery to users on demand. Application of this is to help visually-impaired people perceive their surroundings and make it more accessible.

Description
We will make use of Google's automatic video tagging capabilities (using Cloud Vision API), Text-to-Speech API along with our custom story generation & analysis pipeline. With the generated tags, we would be extending this application by using powerful semantic data extraction of NLTK so that the videos can be described in real-time and a story-like manner. Audio descriptions would be describing key visual scenes, such as the actions and activities of objects detected within certain surroundings.

Challenges
We would be generating meaningful and semantically accurate sentences from the tags generated from videos in real-time using module designed on own using NLTK in Google App Engine.  

