from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob


#create training and test data. 
train=[
		('Its just a job. Grass grows, birds fly, waves pound the sand. I beat people up.', 'Positive'),
		('Time is swift, it races by; opportunities are born and die.', 'Positive'),
		('You are my best friend.', 'Positive'),
		('His son is in the first grade.', 'Positive'),
		('I often go to the movies on Sunday afternoon.', 'Positive'),
		('When you have shot one bird flying you have shot all birds flying. They are all different and they fly in different ways but the sensation is the same and the last one is as good as the first','Positive'),
		('War will exist until that distant day when the conscientious objector enjoys the same reputation and prestige that the warrior does today','Positive'),
		('My guests are not arriving now.','Negative'),
		('Jennie has no money.','Negative'),
		('Janetta doesnt miss her mom.','Negative'),
		('I rarely go to the gym after work.','Negative'),
		('Nobody gets the day off.','Negative'),
		('Paul did not call me yesterday.','Negative'),
		('Jamilee never went to the grocery store.','Negative'),
		
	]


test= [
		('We have two children, a girl and a boy','Positive'),
		('Ernie has a brother and a sister.', 'Positive'),
		('The kids do part of their homework at school', 'Positive'),
		('Tammy does her homework in the evening.', 'Positive'),
		('Her daughter goes to kindergarten.', 'Positive'),
		('Gina did not laugh when she saw the huge pile of laundry.','Negative'),
		('I went home to New Jersey, but I couldnt sleep. The next day I couldnt eat. For a week or more I couldnt eat anything at all.','Negative'),
		('I am not unhappy in this remembrance of journalistic things past. There is more than one reason for this, and for these present animadversions. For nobody stole anybodys files, nobody contrived any leaks from a grand jury .','Negative'),
		('They dont care a fig for liberty, equality, fraternity, or any of our values still less for their King and Country. The be-all and end-all of their existence is to have a good time','Negative'),
		('"You are so splendid, Mr. Herriton, that I cant bear to see you wasted. I cant bear--she has not been good to you your mother', 'Negative')

]



def find_sentiment(string):

	#train the classifier
	cl = NaiveBayesClassifier(train)

	#load the classifier
	blob = TextBlob(string, classifier=cl)


	print "\n\n\n\t\t\t{}".format(blob.classify())

	return