#! usr/bin/python
import sys

try:

	#accept file name from command-line argument
	f=open(sys.argv[1]) 

	#read as raw string
	raw_string=f.read()  

	#remove all non ascii characters
	processed_string="".join(i for i in raw_string if ord(i)<128)    


	#display menu for text mining operations
	print "\n\n\n\t\t\tWelcome to Text Mining Application"
	print "\n\n\n\t\t\t0.Frequency Analysis"
	print "\n\t\t\t1.Language Detection"
	print "\n\t\t\t2.Entity Analysis"
	print "\n\t\t\t3.Sentiment Analysis"
	print "\n\t\t\t4.Text Classification"
	print "\n\t\t\t5.Search occurences of a word"
	print "\n\t\t\t6.Exit"


	choice=input("\n\t\t\tType your choice: ")

	while(choice < 7 ):



		if choice == 0:
			import word_frequency
			word_frequency.freq_words(processed_string)
		elif choice == 1:
			import language_detection
			language_detection.find_lang(processed_string)
		elif choice == 2:
			import entity_analysis
			entity_analysis.find_entities(processed_string)
		elif choice == 3:
			import sentiment_analysis
			sentiment_analysis.find_sentiment(processed_string)
		elif choice == 4:
			import text_classification
			text_classification.find_topic(processed_string)
		elif choice == 5:
			import word_occurence
			item=raw_input("\n\n\n\t\t\tEnter query term: ")
			word_occurence.find_word(processed_string, item)
		elif choice == 6:
			break
		else:
			print "\n\n\n\t\t\tEnter choice[1-6]:"

		choice=input("\n\n\n\t\t\tType your choice: ")


except IOError:
	print"\n\n\n\t\t\tCant find file or read from file"

