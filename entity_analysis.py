import re


def find_entities(string):

	

	print "\n\n\n\t\t\tReading from file"

	print "\n\n\n\t\t\tProcessing"

	pattern=re.compile("1?-?\(?\d{3}\)?-?\d{3}-?\d{4}")


	print "\n\n\n\t\t\tSearching for phone numbers"


	phone=pattern.findall(string)


	pattern=re.compile("[\w\.-]+@[\w\.-]+")


	print "\n\n\n\t\t\tSearching for emails"


	email=pattern.findall(string)


	print "\n\n\n\t\t\tSearching for dates"


	pattern=re.compile('\d\d\s(?:January|Febrary|March|April|May|June|July|August|September|October|November|December)\s\d{4}')


	dates=pattern.findall(string)


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

	return