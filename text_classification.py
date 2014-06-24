from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob


#create training and test data
train=[
		('Wawrinka avoids another first round exit', 'Sports'),
		('Neymar inspires Brazil, Dutch storm on at World Cup', 'Sports'),
		('Rain halts play on fifth day of England v Sri Lanka test', 'Sports'),
		('Boycott says out-of-form Cook could quit as captain', 'Sports'),
		('Neymar scores 100th goal of World Cup in Brazils 100th game', 'Sports'),
		('Rupee snaps two-day fall as shares gain', 'Business'),
		('BSE Sensex gains over 300 points; oil, airline stocks up', 'Business'),
		('Aviation minister says has asked states to cut jet fuel tax', 'Business'),
		('Reliance Comm likely to launch up to $500 million share sale' , 'Business'),
		('Futures point to flat open, consumer data awaited', 'Business'),
		('Finance minister says time for action to fix economy', 'Business'),
		('Parsvnath to raise more than $167.5 million by divesting land assets', 'Business'),
		('Asian shares push ahead on hopeful signs for global growth', 'Business'),
		('Wall Street ends flat after six-day rally energy rises', 'Business'),
		('Shares slip on gloomy euro zone data, dollar eases', 'Business'),
		('Gold steadies below two-month high; weaker shares', 'Business'),
		('Biden Consults Turkey, Bahrain Leaders on Iraq', 'Politics'),
		('IRS Head Says No Obstruction of Congress in Probe', 'Politics'),
		('Mississippi Voters Deciding Tough GOP Senate Race', 'Politics'),
		('US: Looking at All Options in Immigration Surge', 'Politics'),
		('White House Condemns Egypt Sentencing Reporters', 'Politics'),
		('US Gets Legal Protections for Forces in Iraq', 'Politics'),
		('Racial Politics Churn Miss. GOP Senate Runoff', 'Politics'),
		('Diplomats call on Tony Blair to quit as Middle East peace envoy over Iraq legacy', 'Politics'),
		('Benghazi attack suspect Ahmed Abu Khatallah captured by US forces in secret raid','Politics'),
		('G7 summit: World leaders call on Vladimir Putin to engage with Ukraines new government and stem separatist violence','Politics'),
		('US declares cyber war on China: Chinese military hackers charged with trying to steal secrets from companies including nuclear energy firm','Politics'),
		('Syria conflict: Suspicions of possible undeclared chemical agents voiced at UN','Politics'),
		('Thailands military coup: Come on, get happy','Politics'),
		('China, Japan manufacturing returns to growth, but exports still weak', 'Business'),
		('Upbeat China PMI boosts Asian equities', 'Business'),
		('Metal shares gain as China factory activity quickens', 'Business'),
		('Car industry struggles to solve air bag explosions despite mass recalls', 'Business'),
		('Millennials Seen Surging as Homeowners in U.S.: Mortgages', 'Business')

]




test=[
		('Azarenka enjoys first win after six months of injury woes', 'Sports'),
		('Portugals Last-Second Draw Is Most-Watched Soccer Game in U.S', 'Sports'),
		('Mexico Beats Croatia 3-1 to Advance in World Cup With Brazil', 'Sports'),
		('Netherlands Tied 0-0 With Chile in World Cup Match', 'Sports'),
		('World Stocks Struggle After Wall St Rally Pauses', 'Business'),
		('Tribal politics in New York: Herd mentality','Politics'),
		('Colombia presidential election: Four more years', 'Politics'),
		('Foreign policy: Iraq is not going to be a perfect place', 'Politics'),
		('German Business Optimism Slips Amid Ukraine', 'Business'),
		('Rates on US Treasury Bills Drop at Weekly Auction', 'Business'),
		('Figures on Government Spending and Debt', 'Business'),
		('Oracle Buying Micros Systems for About $5.3B', 'Business'),
		('Wisconsin Energy Buying Integrys for $5.8 Billion', 'Business'),
		('Oil Falls as Market Eyes Situation in Iraq', 'Business')

]

def find_topic(string):

	
	#train the classifier
	cl = NaiveBayesClassifier(train)

	#load the classifier
	blob = TextBlob(string, classifier=cl)

	print "\n\n\n\t\t\t{}".format(blob.classify())

	return