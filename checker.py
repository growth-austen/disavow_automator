import requests
import webbrowser
import time

#pulls in the disavow file
with open('disavow.txt', 'a+') as disavow:
	disavow_urls = disavow.read().splitlines()
	#adds a comment to the disavow file that you're updating it today
	disavow.write("\n\n#Updated " + time.strftime("%x") )
	
#pulls in your URLs
with open('urls.txt', 'r') as urls:
	url_set = urls.read().splitlines()
	urls.close()

#pulls in your whitelist
with open('whitelist.txt', 'r') as whitelist:
	whitelist_set = whitelist.read().splitlines()
	whitelist.close()

#removes the URLs that are already in the whitelist or the disavow file
diff = set(url_set)-set(disavow_urls)-set(whitelist_set)

#checks to see if there are any URLs remaining after removing the whitelist and disavow
if len(diff) > 0:
	print "Looking at these URLs: %s" % diff

	for url in diff:
		#opens the URL in the browser
		#import webbrowser and run 'print webbrowser.browser' to find your browser 
		#replace 'macosx' if you'd like to use another browser
		webbrowser.get('macosx').open(url)
		#prompts you - is this URL spam?
		to_add = raw_input('Is %s spam? (y or n)> ' %(url))
		#if it is, add it to the disavow
		if (to_add.lower() == "y"):
			print "Added to the disavow file"
			with open('disavow.txt', 'a') as disavow:
				disavow.write("\n" + url)
		else:
			#if not, add it to the whitelist
			print "Added to the whitelist"
			with open('whitelist.txt', 'a') as whitelist:
				whitelist.write("\n" + url)

	print "All finished"
else:
	print "There are no more URLs to check"
