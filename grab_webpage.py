import requests
from HTMLParser import HTMLParser
import webbrowser
import time

#This script assumes two things:
#1. That you have put your disavow file in disavow.txt (in the same directory)
#2. That you will hold a continually updated whitelist in whitelist.txt

#grab a URL from a list of URLs
with open('urls.txt') as f:
	for url in f:

		#import webbrowser and run 'print webbrowser.browser' to find your browser 
		#replace 'macosx' if you'd like to use another browser

		##Check to see if the URL is already in the whois
		with open('disavow.txt', 'w') as disavow:
			#add a comment about when the file is updated to the disavow
			#disavow.write("\n\n#Updated " + time.strftime("%x") )

				#if the URL is already in the disavow ->
				if url in disavow.read():	
					#print that it exists, removing the newline
					print "%s exists" % url.rstrip()
				else:	
					#otherwise, open it in the browser
					webbrowser.get('macosx').open(url)
					#ask the user if they'd like to add it
					to_add =raw_input("Would you like to add this? y or n?> ")
					#run this loop if they want to add it
					if to_add.lower() == 'y':
						#open the disavow file and add the URL
						disavow_file = open('disavow.txt', 'w')
						disavow_file.write(url)
					else:
						#otheriwse add it to the whitelist
						print "OK, added to whitelist"
						whitelist = open('whitelist.txt', 'w')
						whitelist.write("\n" + url)
		
print "All finished"