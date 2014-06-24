import nltk
import re
from os import path
import wordcloud
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords


#import stop words from nltk corpus
english_stop_words=list(stopwords.words('english'))


#get current directory
d = path.dirname(__file__)

#create additional stop words for puntuations and others
additional_stop_words=['I','.',',','\'','!','(',')',':',';','?','--','*','\'ll','\'ve','\'s','\'re','The','n\'t','A','could','should','would','can','will','\'I','shall']


#add them together
total_stop_words= english_stop_words + additional_stop_words



def freq_words(string):


	print "\n\n\n\t\t\tReading from file"

	#tokenize on white spaces
	raw_word_list=word_tokenize(string)

	#remove stop words
	processed_word_list=[word for word in raw_word_list if word not in total_stop_words]

	#create an nltk text object
	text_obj=nltk.Text(processed_word_list)

	print "\n\n\n\t\t\tProcessing"

	#Call the frequency distribution method and store the words and  corresponding frequencies in a dictionary
	fd=FreqDist(text_obj)

	
	#convert the dictionary to a list of tuples conatining key-value pairs
	result=fd.items()
	

	#select the 100 most frequent words. If number of words in the result is less than 100, adjust accordingly
	if len(result) < 100:
		result_length=len(result)
		chosen_words=result[: result_length/2]
	else:
		chosen_words=result[:100]
	
	print "\n\n\n\t\t\tDrawing cloud"


	#specify the canvas measurement
	elements = wordcloud.fit_words(chosen_words, width=500, height=500)


	#draw the cloud
	wordcloud.draw(elements, path.join(d, 'frequent_words.png'), width=500, height=500,
        scale=2)


	print "\n\n\n\t\t\tWord cloud generated in frequent_words.png file"
	

	return
	
