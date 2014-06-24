import nltk
from nltk.tokenize import word_tokenize

def find_word(string, item):

	#tokenize on white spaces
	word_list=word_tokenize(string)	

	#create a nltk text object
	text_obj=nltk.Text(word_list)

	#find all occurences of the word
	text_obj.concordance(item)


	return