import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import urllib


#import stop words from nltk corpus
english_stop_words=list(stopwords.words('english'))




#create additional stop words for puntuations and others
additional_stop_words=['I','.',',','\'','!','(',')',':',';','?','--','*','Im', 'Ill','\'ll','\'ve','\'s','\'re','The','n\'t','A','could','should','would','can','will','\'I','shall']


#add them together
total_stop_words= english_stop_words + additional_stop_words


#initailize two empty lists for intermediate results 
entities=[]
tree=[]



#write a function to transverse a chunked tree and get key
def traverse(t): 
			try: 
				t.node 
			except AttributeError: 
					return 
			else: 
				if t.node == 'NP':
							  entities.append(t[0]) #add the tuples into a list
				else: 
					for child in t:
						 traverse(child)



def find_entities(string):

	

	map_url="http://maps.googleapis.com/maps/api/staticmap?center=0,0&zoom=1&size=640x640&markers=size:mid%7Ccolor:red"

	print "\n\n\n\t\t\tReading from file"

	print "\n\n\n\t\t\tProcessing"

	#default sentence segmenter
	sentences=nltk.sent_tokenize(string)

	#nltk word tokenize
	sentences=[nltk.word_tokenize(sent) for sent in sentences]

	words=[]


	#remove stop words
	for sent in sentences:
		words.append([word for word in sent if word not in total_stop_words])

	
	#nltk pos tagger
	words=[nltk.pos_tag(word) for word in words]

	#create a chunking pattern for proper nouns only
	entity_pattern="NP:{<NNP>}"


	NPChunker=nltk.RegexpParser(entity_pattern)


	regex_pattern=re.compile("1?-?\(?\d{3}\)?-?\d{3}-?\d{4}")


	print "\n\n\n\t\t\tSearching for phone numbers"


	phone=regex_pattern.findall(string)


	regex_pattern=re.compile("[\w\.-]+@[\w\.-]+")


	print "\n\n\n\t\t\tSearching for emails"


	email=regex_pattern.findall(string)


	print "\n\n\n\t\t\tSearching for dates"


	regex_pattern=re.compile('\d\d\s(?:January|Febrary|March|April|May|June|July|August|September|October|November|December)\s\d{4}')


	dates=regex_pattern.findall(string)


	


	#find all proper nouns using our chunker
	for single in words:

		#returns a treee with proper nouns
		tree=NPChunker.parse(single)

		#traverse our tree 
		traverse(tree)





	print "\n\n\n\t\t\tPhone Numbers"

	if len(phone) == 0:
		print "\n\n\n\t\t\tNo phone numbers found"

	else:
		for x in phone:
			print "\n\t\t\t{}".format(x)


	print "\n\n\n\t\t\tEmail Addresses"

	if len(email) == 0:
		print "\n\n\n\t\t\tNo emails found"

	else:
		for x in email:
			print "\n\t\t\t{}".format(x)
	

	print "\n\n\n\t\t\tDates"


	if len(dates) == 0:
		print "\n\n\n\t\t\tNo dates found"

	else:
		for x in dates:
			print "\n\t\t\t{}".format(x)



	print "\n\n\n\t\t\tPersons, Locations and other Entities"


	
	keys=[]

	#extract keys from all tuples in the list
	for entity in entities:
			keys.append(entity[0])


	#remove duplicates
	result=set(keys)

	location_list=list(result)

	url=map_url

	for place in location_list:
		url=url+"%7C"+place+","



	print "\n"

	for value in result:
		
		print "\n\t\t\t{}".format(value)
		


	
	
	#map the locations and save the file
	urllib.urlretrieve(url, "locations.jpg")


	return





	