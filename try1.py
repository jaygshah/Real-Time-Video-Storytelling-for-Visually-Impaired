from randomsentence.sentence_maker import SentenceMaker
from randomsentence.sentence_tools import SentenceTools
sentence_maker = SentenceMaker()
tagged_sentence = sentence_maker.from_keyword_list(['boy', 'park', 'grass', 'play'])
print(tagged_sentence)
sentence_tools = SentenceTools()
print(sentence_tools.detokenize_tagged(tagged_sentence))



# from randomsentence import GrammarCorrector
# corrector = GrammarCorrector()
# print(corrector.correct('A sentence with a error in the Hitchhiker’s Guide tot he Galaxy'))
# # 'A sentence with an error in the Hitchhiker’s Guide to the Galaxy'



# from randomsentence.randomsentence import RandomSentence
# from randomsentence.sentence_tools import SentenceTools
# random_sentence = RandomSentence()
# tagged_sentence = random_sentence.get_tagged_sent()
# print(tagged_sentence)
# sentence_tools = SentenceTools()
# print(sentence_tools.detokenize_tagged(tagged_sentence))