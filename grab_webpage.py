import requests
from HTMLParser import HTMLParser
import webbrowser

#grab a URL from a list of URLs
with open('urls.txt') as f:
	for url in f:
		##OPTION ONE - PRINT HTML TO THE TERMINAL
		##grab the information from the url
		#r = requests.get(line)
		##print it to the screen
		#content = r.content
		#stripped = content.sub('<[^<]+?>', '', text)
		#print stripped
		##wait for user to hit enter
		#raw_input("Press enter to continue")

		##OPTION TWO - OPEN THE PAGE IN A BROWSER
		#import webbrowser and run 'print webbrowser.browser' to find your browser - will replace 'macosx'
		webbrowser.get('macosx').open(url)
		raw_input("Press enter to continue")
print "All finished"




# import requests

# #grab a URL from a list of URLs
# with open('urls.txt') as f:
# 	for line in f:
# 		#grab the information from the url
# 		r = requests.get(line)
# 		#print it to the screen
# 		print r.content
# 		#wait for user to hit enter
# 		raw_input("Press enter to continue")
# print "All finished"