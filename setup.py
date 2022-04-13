#######################################################################################################

# IMPORTS #
from fileinput import filename
from unittest import result
from attr import attr
import requests
from bs4 import BeautifulSoup
from datetime import date
import shutil
import tweepy
import json
from TwitterApi import *

#######################################################################################################

# VARIABLES #
current_date = date.today().strftime('%d/%m/%Y')
url_meteo = 'http://www.cartesfrance.fr/meteo/'
url_sun = 'http://calendriersolaire.com/calendrier'
file_source = '/tmp/' #Via AWS Lambda

#######################################################################################################

# CONNECTION API TWITTER #
auth = tweepy.OAuth1UserHandler(
    api['api_key'], 
    api['api_key_secret'],
    api['access_token'], 
    api['access_token_secret']
)
api = tweepy.API(auth)
#######################################################################################################