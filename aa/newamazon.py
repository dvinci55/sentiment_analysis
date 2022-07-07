#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Written as part of https://www.scrapehero.com/how-to-scrape-amazon-product-reviews-using-python/		
from lxml import html  
import json
import requests
import json,re
from dateutil import parser as dateparser
from time import sleep
import sys
import csv
from textblob import TextBlob

def ParseReviews(asin):
	
			print(1)
			amazon_url  = 'http://www.amazon.com/dp/'+asin+'/#customerReviews'
			print(amazon_url)
			# Add some recent user agent to prevent amazon from blocking the request 
			# Find some chrome user agent strings  here https://udger.com/resources/ua-list/browser-detail?browser=Chrome
			headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
			print(2)
			page = requests.get(amazon_url,headers = headers)
			page_response = page.text

			parser = html.fromstring(page_response)
			#XPATH_REVIEW_SECTION_1 = '//h2//text()'
			XPATH_REVIEW_HEADER = './/a[@data-hook="review-title"]//text()'
			reviews = parser.xpath(XPATH_REVIEW_HEADER)
			print(reviews)
			dataa={
						'reviews':reviews
					}
			return dataa	
			return(dataa)
			
def ReadAsin():
	#Add your own ASINs here 
	AsinList = [str(sys.argv[1])]
	extracted_data = []
	for asin in AsinList:
		print "Downloading and processing page http://www.amazon.com/dp/"+asin
		extracted_data.append(ParseReviews(asin))
		sleep(5)
	f=open('data.json','w')
	json.dump(extracted_data,f,indent=4)
	f.seek(0)
	with open('data.json') as data_file:    
   		data = json.load(data_file)
	print(data)
	data1=TextBlob(clean_tweet(str(data)))
	print(data1)
	with open('amazonnewupdated2.txt', 'w') as my_file:
    		my_file.write(str(data1))

	with open('amazonnewupdated2.txt', 'r') as my_file:
	    text = my_file.read()
	    text = text.replace("u reviews u", " ")
	    text = text.replace(" u ", "\n")
	

	# If you wish to save the updates back into a cleaned up file
	with open('my_file_clean.txt', 'w') as my_file:
	    my_file.write(text)

	with open('my_file_clean.txt') as infile, open('output.txt', 'w') as outfile:
    		for line in infile:
        		if not line.strip(): continue  # skip the empty line
        		outfile.write(line) 



def clean_tweet(data):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \\t])|(\w+:\/\/\S+)", " ", data).split())

		
	
if __name__ == '__main__':
	ReadAsin()
