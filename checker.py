import requests
import webbrowser
import time

with open('disavow.txt', 'a+') as disavow:
	disavow_urls = disavow.read().splitlines()
	disavow.write("\n\n#Updated " + time.strftime("%x") )
	

with open('urls.txt', 'r') as urls:
	url_set = urls.read().splitlines()
	urls.close()

with open('whitelist.txt', 'r') as whitelist:
	whitelist_set = whitelist.read().splitlines()
	whitelist.close()

diff = set(url_set)-set(disavow_urls)-set(whitelist_set)

if len(diff) > 0:
	print "Looking at these URLs: %s" % diff

	for url in diff:
		webbrowser.get('macosx').open(url)
		to_add = raw_input('Is %s spam? (y or n)> ' %(url))
		if (to_add == 'y') or (to_add == "Y"):
			print "Added to the disavow file"
			with open('disavow.txt', 'a') as disavow:
				disavow.write("\n" + url)
		else:
			print "Added to the whitelist"
			with open('whitelist.txt', 'a') as whitelist:
				whitelist.write("\n" + url)

	print "All finished"
else:
	print "There are no more URLs to check"