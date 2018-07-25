# -*- coding: utf-8 -*-
"""
Created on Fri May 18 14:52:02 2018

@author: Ksenia
"""

model = {}

# DEPENDENT VARIABLE (8)
## count activation level for each video
import time
import datetime

dates = []
for i in blockers:
    s = blockers[i]['snippet']['publishedAt'][0:10]
    date = time.mktime(datetime.datetime.strptime(s, "%Y-%m-%d").timetuple())
    dates.append(date)
for i in blockers:
    s = blockers[i]['snippet']['publishedAt'][0:10]
    date = time.mktime(datetime.datetime.strptime(s, "%Y-%m-%d").timetuple())
    minDate = min(dates)
    maxDate = max(dates)
    blockers[i]['activatedStatus'] = (date-minDate)/(maxDate-minDate)
for i in hypecamp:
    s = hypecamp[i]['snippet']['publishedAt'][0:10]
    date = time.mktime(datetime.datetime.strptime(s, "%Y-%m-%d").timetuple())
    dates.append(date)
for i in hypecamp:
    s = hypecamp[i]['snippet']['publishedAt'][0:10]
    date = time.mktime(datetime.datetime.strptime(s, "%Y-%m-%d").timetuple())
    minDate = min(dates)
    maxDate = max(dates)
    hypecamp[i]['activatedStatus'] = (date-minDate)/(maxDate-minDate)
for i in lizzka:
    s = lizzka[i]['snippet']['publishedAt'][0:10]
    date = time.mktime(datetime.datetime.strptime(s, "%Y-%m-%d").timetuple())
    dates.append(date)
for i in lizzka:
    s = lizzka[i]['snippet']['publishedAt'][0:10]
    date = time.mktime(datetime.datetime.strptime(s, "%Y-%m-%d").timetuple())
    minDate = min(dates)
    maxDate = max(dates)
    lizzka[i]['activatedStatus'] = (date-minDate)/(maxDate-minDate)
for i in rostar:
    s = rostar[i]['snippet']['publishedAt'][0:10]
    date = time.mktime(datetime.datetime.strptime(s, "%Y-%m-%d").timetuple())
    dates.append(date)
for i in rostar:
    s = rostar[i]['snippet']['publishedAt'][0:10]
    date = time.mktime(datetime.datetime.strptime(s, "%Y-%m-%d").timetuple())
    minDate = min(dates)
    maxDate = max(dates)
    rostar[i]['activatedStatus'] = (date-minDate)/(maxDate-minDate)
for i in veet1:
    s = veet1[i]['snippet']['publishedAt'][0:10]
    date = time.mktime(datetime.datetime.strptime(s, "%Y-%m-%d").timetuple())
    dates.append(date)
for i in veet1:
    s = veet1[i]['snippet']['publishedAt'][0:10]
    date = time.mktime(datetime.datetime.strptime(s, "%Y-%m-%d").timetuple())
    minDate = min(dates)
    maxDate = max(dates)
    veet1[i]['activatedStatus'] = (date-minDate)/(maxDate-minDate)
for i in veet2:
    s = veet2[i]['snippet']['publishedAt'][0:10]
    date = time.mktime(datetime.datetime.strptime(s, "%Y-%m-%d").timetuple())
    dates.append(date)
for i in veet2:
    s = veet2[i]['snippet']['publishedAt'][0:10]
    date = time.mktime(datetime.datetime.strptime(s, "%Y-%m-%d").timetuple())
    minDate = min(dates)
    maxDate = max(dates)
    veet2[i]['activatedStatus'] = (date-minDate)/(maxDate-minDate)
for i in versus:
    s = versus[i]['snippet']['publishedAt'][0:10]
    date = time.mktime(datetime.datetime.strptime(s, "%Y-%m-%d").timetuple())
    dates.append(date)
for i in versus:
    s = versus[i]['snippet']['publishedAt'][0:10]
    date = time.mktime(datetime.datetime.strptime(s, "%Y-%m-%d").timetuple())
    minDate = min(dates)
    maxDate = max(dates)
    versus[i]['activatedStatus'] = (date-minDate)/(maxDate-minDate)
for i in klinsky:
    s = klinsky[i]['snippet']['publishedAt'][0:10]
    date = time.mktime(datetime.datetime.strptime(s, "%Y-%m-%d").timetuple())
    dates.append(date)
for i in klinsky:
    s = klinsky[i]['snippet']['publishedAt'][0:10]
    date = time.mktime(datetime.datetime.strptime(s, "%Y-%m-%d").timetuple())
    minDate = min(dates)
    maxDate = max(dates)
    klinsky[i]['activatedStatus'] = (date-minDate)/(maxDate-minDate)
    
blockersTitle = {}
colaTitle = []
hypecampTitle = {}
klinskyTitle = {}
lizzkaTitle = {}
veet1Title = {}
veet2Title = {}
rostarTitle = {}
versusTitle = {}
for i in blockers:
    name = blockers[i]['snippet']['channelTitle']
    status = blockers[i]['activatedStatus']
    if name in blockersTitle.keys():
        pass
    else:
        blockersTitle[name] = status
        
for i in cola:
    name = cola[i]['snippet']['channelTitle']
    if name in colaTitle:
        pass
    else:
        colaTitle.append(name)

for i in hypecamp:
    name = hypecamp[i]['snippet']['channelTitle']
    status = hypecamp[i]['activatedStatus']
    if name in hypecampTitle.keys():
        pass
    else:
        hypecampTitle[name] = status
        
for i in klinsky:
    name = klinsky[i]['snippet']['channelTitle']
    status = klinsky[i]['activatedStatus']
    if name in klinskyTitle.keys():
        pass
    else:
        klinskyTitle[name] = status
        
for i in lizzka:
    name = lizzka[i]['snippet']['channelTitle']
    status = lizzka[i]['activatedStatus']
    if name in lizzkaTitle.keys():
        pass
    else:
        lizzkaTitle[name] = status
        
for i in rostar:
    name = rostar[i]['snippet']['channelTitle']
    status = rostar[i]['activatedStatus']
    if name in rostarTitle.keys():
        pass
    else:
        rostarTitle[name] = status
        
for i in veet1:
    name = veet1[i]['snippet']['channelTitle']
    status = veet1[i]['activatedStatus']
    if name in veet1Title.keys():
        pass
    else:
        veet1Title[name] = status
        
for i in veet2:
    name = veet2[i]['snippet']['channelTitle']
    status = veet2[i]['activatedStatus']
    if name in veet2Title.keys():
        pass
    else:
        veet2Title[name] = status
        
for i in versus:
    name = versus[i]['snippet']['channelTitle']
    status = versus[i]['activatedStatus']
    if name in versusTitle.keys():
        pass
    else:
        versusTitle[name] = status
        
for i in clustered:
    name = clustered[i]['name']
    if name in blockersTitle:
        clustered[i]['blockers'] = blockersTitle[name]
        clustered[i]['blockersCat'] = int(10*blockersTitle[name])+1
    else:
        clustered[i]['blockers'] = 0
        clustered[i]['blockersCat'] = 0
    
    if name in colaTitle:
        clustered[i]['cola'] = 1
    else:
        clustered[i]['cola'] = 0
        
    if name in hypecampTitle:
        clustered[i]['hypecamp'] = hypecampTitle[name]
        clustered[i]['hypecampCat'] = int(10*hypecampTitle[name])+1
    else:
        clustered[i]['hypecamp'] = 0
        clustered[i]['hypecampCat'] = 0
        
    if name in klinskyTitle:
        clustered[i]['klinsky'] = klinskyTitle[name]
        clustered[i]['klinskyCat'] = int(10*klinskyTitle[name])+1
    else:
        clustered[i]['klinsky'] = 0
        clustered[i]['klinskyCat'] = 0
        
    if name in lizzkaTitle:
        clustered[i]['lizzka'] = lizzkaTitle[name]
        clustered[i]['lizzkaCat'] = int(10*lizzkaTitle[name])+1
    else:
        clustered[i]['lizzka'] = 0
        clustered[i]['lizzkaCat'] = 0
        
    if name in rostarTitle:
        clustered[i]['rostar'] = rostarTitle[name]
        clustered[i]['rostarCat'] = int(10*rostarTitle[name])+1
    else:
        clustered[i]['rostar'] = 0
        clustered[i]['rostarCat'] = 0
        
    if name in veet1Title:
        clustered[i]['veet1'] = veet1Title[name]
        clustered[i]['veet1Cat'] = int(10*veet1Title[name])+1
    else:
        clustered[i]['veet1'] = 0
        clustered[i]['veet1Cat'] = 0
        
    if name in veet2Title:
        clustered[i]['veet2'] = veet2Title[name]
        clustered[i]['veet2Cat'] = int(10*veet2Title[name])+1
    else:
        clustered[i]['veet2'] = 0
        clustered[i]['veet2Cat'] = 0
        
    if name in versusTitle:
        clustered[i]['versus'] = versusTitle[name]
        clustered[i]['versusCat'] = int(10*versusTitle[name])+1
    else:
        clustered[i]['versus'] = 0
        clustered[i]['versusCat'] = 0
        
        
activated = []
for i in allChannels:
    number = allChannels[i]['versus'] + allChannels[i]['veet1'] + allChannels[i]['veet2'] + allChannels[i]['rostar'] + allChannels[i]['lizzka'] + allChannels[i]['hypecamp'] + allChannels[i]['cola'] + allChannels[i]['blockers']
    activated.append(number)
    
print(min(activated))
print(max(activated))
print(sum(activated)/len(activated))

import time
import datetime
versus_dates = data['versus_dates']
for date in versus_dates:
    s = date
    time.mktime(datetime.datetime.strptime(s, "%d/%m/%Y").timetuple())

# MESSAGE
import os

import google.oauth2.credentials

import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret.
CLIENT_SECRETS_FILE = "client_secret.json"

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account and requires requests to use an SSL connection.
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

def get_authenticated_service():
  flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
  credentials = flow.run_console()
  return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)

def print_response(response):
  print(response)

# Build a resource based on a list of properties given as key-value pairs.
# Leave properties with empty values out of the inserted resource.
def build_resource(properties):
  resource = {}
  for p in properties:
    # Given a key like "snippet.title", split into "snippet" and "title", where
    # "snippet" will be an object and "title" will be a property in that object.
    prop_array = p.split('.')
    ref = resource
    for pa in range(0, len(prop_array)):
      is_array = False
      key = prop_array[pa]

      # For properties that have array values, convert a name like
      # "snippet.tags[]" to snippet.tags, and set a flag to handle
      # the value as an array.
      if key[-2:] == '[]':
        key = key[0:len(key)-2:]
        is_array = True

      if pa == (len(prop_array) - 1):
        # Leave properties without values out of inserted resource.
        if properties[p]:
          if is_array:
            ref[key] = properties[p].split(',')
          else:
            ref[key] = properties[p]
      elif key not in ref:
        # For example, the property is "snippet.title", but the resource does
        # not yet have a "snippet" object. Create the snippet object here.
        # Setting "ref = ref[key]" means that in the next time through the
        # "for pa in range ..." loop, we will be setting a property in the
        # resource's "snippet" object.
        ref[key] = {}
        ref = ref[key]
      else:
        # For example, the property is "snippet.description", and the resource
        # already has a "snippet" object.
        ref = ref[key]
  return resource

# Remove keyword arguments that are not set
def remove_empty_kwargs(**kwargs):
  good_kwargs = {}
  if kwargs is not None:
    for key, value in kwargs.iteritems():
      if value:
        good_kwargs[key] = value
  return good_kwargs

def videos_list_by_id(client, **kwargs):
  # See full sample for function
  kwargs = remove_empty_kwargs(**kwargs)

  response = client.videos().list(
    **kwargs
  ).execute()

  return response

def channels_list_by_id(client, **kwargs):
  # See full sample for function
  kwargs = remove_empty_kwargs(**kwargs)

  response = client.channels().list(
    **kwargs
  ).execute()

  return response


if __name__ == '__main__':
    # When running locally, disable OAuthlib's HTTPs verification. When
    # running in production *do not* leave this option enabled.
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    client = get_authenticated_service()
  
    meta = {}
    meta['blockers'] = {}
    # length of title and description
    meta['blockers']['id'] = 'emF_t_rIHcE'
    meta['blockers']['title'] = blockers['emF_t_rIHcE']['snippet']['title']
    meta['blockers']['desc'] = blockers['emF_t_rIHcE']['snippet']['description']
    meta['blockers']['lendesc'] = len(meta['blockers']['desc'])
    meta['blockers']['lentitle'] = len(meta['blockers']['title'])
    ## % capital letters in title
    meta['blockers']['uppercase'] = sum(1 for c in meta['blockers']['title'] if c.isupper())
    ## number of http
    meta['blockers']['http'] = meta['blockers']['desc'].count('http')
    ## ad status
    meta['blockers']['ad'] = 0
    ## statistics  
    c = videos_list_by_id(client,
    part='statistics',
    id='emF_t_rIHcE')
      
    meta['blockers']['comment'] = c['items'][0]['statistics']['commentCount']
    meta['blockers']['dislike'] = c['items'][0]['statistics']['dislikeCount']
    meta['blockers']['like'] = c['items'][0]['statistics']['likeCount']
    meta['blockers']['view'] = c['items'][0]['statistics']['viewCount']
    
    meta['hypecamp'] = {}
    # length of title and description
    meta['hypecamp']['id'] = 'CFGkP4bJM18'
    meta['hypecamp']['title'] = hypecamp['CFGkP4bJM18']['snippet']['title']
    meta['hypecamp']['desc'] = hypecamp['CFGkP4bJM18']['snippet']['description']
    meta['hypecamp']['lendesc'] = len(meta['hypecamp']['desc'])
    meta['hypecamp']['lentitle'] = len(meta['hypecamp']['title'])
    ## % capital letters in title
    meta['hypecamp']['uppercase'] = sum(1 for c in meta['hypecamp']['title'] if c.isupper())
    ## number of http
    meta['hypecamp']['http'] = meta['hypecamp']['desc'].count('http')
    ## ad status
    meta['hypecamp']['ad'] = 0
    ## statistics  
    c = videos_list_by_id(client,
    part='statistics',
    id='CFGkP4bJM18')
      
    meta['hypecamp']['comment'] = 0
    meta['hypecamp']['dislike'] = c['items'][0]['statistics']['dislikeCount']
    meta['hypecamp']['like'] = c['items'][0]['statistics']['likeCount']
    meta['hypecamp']['view'] = c['items'][0]['statistics']['viewCount']
    
    meta['klinsky'] = {}
    # length of title and description
    meta['klinsky']['id'] = 'mHeZd-DNnPQ'
    meta['klinsky']['title'] = klinsky['mHeZd-DNnPQ']['snippet']['title']
    meta['klinsky']['desc'] = klinsky['mHeZd-DNnPQ']['snippet']['description']
    meta['klinsky']['lendesc'] = len(meta['klinsky']['desc'])
    meta['klinsky']['lentitle'] = len(meta['klinsky']['title'])
    ## % capital letters in title
    meta['klinsky']['uppercase'] = sum(1 for c in meta['klinsky']['title'] if c.isupper())
    ## number of http
    meta['klinsky']['http'] = meta['klinsky']['desc'].count('http')
    ## ad status
    meta['klinsky']['ad'] = 1
    ## statistics  
    c = videos_list_by_id(client,
    part='statistics',
    id='mHeZd-DNnPQ')
      
    meta['klinsky']['comment'] = c['items'][0]['statistics']['commentCount']
    meta['klinsky']['dislike'] = c['items'][0]['statistics']['dislikeCount']
    meta['klinsky']['like'] = c['items'][0]['statistics']['likeCount']
    meta['klinsky']['view'] = c['items'][0]['statistics']['viewCount']
    
    meta['lizzka'] = {}
    # length of title and description
    meta['lizzka']['id'] = 'JFDGuvN5tMA'
    meta['lizzka']['title'] = lizzka['JFDGuvN5tMA']['snippet']['title']
    meta['lizzka']['desc'] = lizzka['JFDGuvN5tMA']['snippet']['description']
    meta['lizzka']['lendesc'] = len(meta['lizzka']['desc'])
    meta['lizzka']['lentitle'] = len(meta['lizzka']['title'])
    ## % capital letters in title
    meta['lizzka']['uppercase'] = sum(1 for c in meta['lizzka']['title'] if c.isupper())
    ## number of http
    meta['lizzka']['http'] = meta['lizzka']['desc'].count('http')
    ## ad status
    meta['lizzka']['ad'] = 0
    ## statistics  
    c = videos_list_by_id(client,
    part='statistics',
    id='JFDGuvN5tMA')
      
    meta['lizzka']['comment'] = c['items'][0]['statistics']['commentCount']
    meta['lizzka']['dislike'] = c['items'][0]['statistics']['dislikeCount']
    meta['lizzka']['like'] = c['items'][0]['statistics']['likeCount']
    meta['lizzka']['view'] = c['items'][0]['statistics']['viewCount']
    
    meta['rostar'] = {}
    # length of title and description
    meta['rostar']['id'] = 'JfWA0kJqDl4'
    meta['rostar']['title'] = rostar['JfWA0kJqDl4']['snippet']['title']
    meta['rostar']['desc'] = rostar['JfWA0kJqDl4']['snippet']['description']
    meta['rostar']['lendesc'] = len(meta['rostar']['desc'])
    meta['rostar']['lentitle'] = len(meta['rostar']['title'])
    ## % capital letters in title
    meta['rostar']['uppercase'] = sum(1 for c in meta['rostar']['title'] if c.isupper())
    ## number of http
    meta['rostar']['http'] = meta['rostar']['desc'].count('http')
    ## ad status
    meta['rostar']['ad'] = 0
    ## statistics  
    c = videos_list_by_id(client,
    part='statistics',
    id='JfWA0kJqDl4')
      
    meta['rostar']['comment'] = c['items'][0]['statistics']['commentCount']
    meta['rostar']['dislike'] = c['items'][0]['statistics']['dislikeCount']
    meta['rostar']['like'] = c['items'][0]['statistics']['likeCount']
    meta['rostar']['view'] = c['items'][0]['statistics']['viewCount']
      
    meta['veet1'] = {}
    # length of title and description
    meta['veet1']['id'] = 'ugMaWo8q2dY'
    meta['veet1']['title'] = veet1['ugMaWo8q2dY']['snippet']['title']
    meta['veet1']['desc'] = veet1['ugMaWo8q2dY']['snippet']['description']
    meta['veet1']['lendesc'] = len(meta['veet1']['desc'])
    meta['veet1']['lentitle'] = len(meta['veet1']['title'])
    ## % capital letters in title
    meta['veet1']['uppercase'] = sum(1 for c in meta['veet1']['title'] if c.isupper())
    ## number of http
    meta['veet1']['http'] = meta['veet1']['desc'].count('http')
    ## ad status
    meta['veet1']['ad'] = 1
    ## statistics  
    c = videos_list_by_id(client,
    part='statistics',
    id='ugMaWo8q2dY')
      
    meta['veet1']['comment'] = c['items'][0]['statistics']['commentCount']
    meta['veet1']['dislike'] = c['items'][0]['statistics']['dislikeCount']
    meta['veet1']['like'] = c['items'][0]['statistics']['likeCount']
    meta['veet1']['view'] = c['items'][0]['statistics']['viewCount']
    
    meta['veet2'] = {}
    # length of title and description
    meta['veet2']['id'] = 'zWQ4_PBBNfE'
    meta['veet2']['title'] = veet2['zWQ4_PBBNfE']['snippet']['title']
    meta['veet2']['desc'] = veet2['zWQ4_PBBNfE']['snippet']['description']
    meta['veet2']['lendesc'] = len(meta['veet2']['desc'])
    meta['veet2']['lentitle'] = len(meta['veet2']['title'])
    ## % capital letters in title
    meta['veet2']['uppercase'] = sum(1 for c in meta['veet2']['title'] if c.isupper())
    ## number of http
    meta['veet2']['http'] = meta['veet2']['desc'].count('http')
    ## ad status
    meta['veet2']['ad'] = 1
    ## statistics  
    c = videos_list_by_id(client,
    part='statistics',
    id='zWQ4_PBBNfE')
      
    meta['veet2']['comment'] = c['items'][0]['statistics']['commentCount']
    meta['veet2']['dislike'] = c['items'][0]['statistics']['dislikeCount']
    meta['veet2']['like'] = c['items'][0]['statistics']['likeCount']
    meta['veet2']['view'] = c['items'][0]['statistics']['viewCount']
    
    meta['versus'] = {}
    # length of title and description
    meta['versus']['id'] = 'v4rvTMBCJD0'
    meta['versus']['title'] = versus['v4rvTMBCJD0']['snippet']['title']
    meta['versus']['desc'] = versus['v4rvTMBCJD0']['snippet']['description']
    meta['versus']['lendesc'] = len(meta['versus']['desc'])
    meta['versus']['lentitle'] = len(meta['versus']['title'])
    ## % capital letters in title
    meta['versus']['uppercase'] = sum(1 for c in meta['versus']['title'] if c.isupper())
    ## number of http
    meta['versus']['http'] = meta['versus']['desc'].count('http') + meta['versus']['desc'].count('https')
    ## ad status
    meta['versus']['ad'] = 0
    ## statistics  
    c = videos_list_by_id(client,
    part='statistics',
    id='v4rvTMBCJD0')
      
    meta['versus']['comment'] = c['items'][0]['statistics']['commentCount']
    meta['versus']['dislike'] = c['items'][0]['statistics']['dislikeCount']
    meta['versus']['like'] = c['items'][0]['statistics']['likeCount']
    meta['versus']['view'] = c['items'][0]['statistics']['viewCount']
    
# MESSAGE AUTHOR
## statistics
    id = blockers[meta['blockers']['id']]['snippet']['channelId']
    c = channels_list_by_id(client,
                part='snippet,statistics',
                id=id)
    meta['blockers']['channelId'] = id
    meta['blockers']['channelViews'] = c['items'][0]['statistics']['viewCount']
    meta['blockers']['channelVideo'] = c['items'][0]['statistics']['videoCount']
    meta['blockers']['channelSubs'] = c['items'][0]['statistics']['subscriberCount']
    
    id = hypecamp[meta['hypecamp']['id']]['snippet']['channelId']
    c = channels_list_by_id(client,
                part='snippet,statistics',
                id=id)
    meta['hypecamp']['channelId'] = id
    meta['hypecamp']['channelViews'] = c['items'][0]['statistics']['viewCount']
    meta['hypecamp']['channelVideo'] = c['items'][0]['statistics']['videoCount']
    meta['hypecamp']['channelSubs'] = c['items'][0]['statistics']['subscriberCount']
    
    id = klinsky[meta['klinsky']['id']]['snippet']['channelId']
    c = channels_list_by_id(client,
                part='snippet,statistics',
                id=id)
    meta['klinsky']['channelId'] = id
    meta['klinsky']['channelViews'] = c['items'][0]['statistics']['viewCount']
    meta['klinsky']['channelVideo'] = c['items'][0]['statistics']['videoCount']
    meta['klinsky']['channelSubs'] = c['items'][0]['statistics']['subscriberCount']
    
    id = lizzka[meta['lizzka']['id']]['snippet']['channelId']
    c = channels_list_by_id(client,
                part='snippet,statistics',
                id=id)
    meta['lizzka']['channelId'] = id
    meta['lizzka']['channelViews'] = c['items'][0]['statistics']['viewCount']
    meta['lizzka']['channelVideo'] = c['items'][0]['statistics']['videoCount']
    meta['lizzka']['channelSubs'] = c['items'][0]['statistics']['subscriberCount']
    
    id = rostar[meta['rostar']['id']]['snippet']['channelId']
    c = channels_list_by_id(client,
                part='snippet,statistics',
                id=id)
    meta['rostar']['channelId'] = id
    meta['rostar']['channelViews'] = c['items'][0]['statistics']['viewCount']
    meta['rostar']['channelVideo'] = c['items'][0]['statistics']['videoCount']
    meta['rostar']['channelSubs'] = c['items'][0]['statistics']['subscriberCount']
    
    id = veet1[meta['veet1']['id']]['snippet']['channelId']
    c = channels_list_by_id(client,
                part='snippet,statistics',
                id=id)
    meta['veet1']['channelId'] = id
    meta['veet1']['channelViews'] = c['items'][0]['statistics']['viewCount']
    meta['veet1']['channelVideo'] = c['items'][0]['statistics']['videoCount']
    meta['veet1']['channelSubs'] = c['items'][0]['statistics']['subscriberCount']
    
    id = veet2[meta['veet2']['id']]['snippet']['channelId']
    c = channels_list_by_id(client,
                part='snippet,statistics',
                id=id)
    meta['veet2']['channelId'] = id
    meta['veet2']['channelViews'] = c['items'][0]['statistics']['viewCount']
    meta['veet2']['channelVideo'] = c['items'][0]['statistics']['videoCount']
    meta['veet2']['channelSubs'] = c['items'][0]['statistics']['subscriberCount']
    
    id = versus[meta['versus']['id']]['snippet']['channelId']
    c = channels_list_by_id(client,
                part='snippet,statistics',
                id=id)
    meta['versus']['channelId'] = id
    meta['versus']['channelViews'] = c['items'][0]['statistics']['viewCount']
    meta['versus']['channelVideo'] = c['items'][0]['statistics']['videoCount']
    meta['versus']['channelSubs'] = c['items'][0]['statistics']['subscriberCount']
    
## author cluster
    with open("new2.json") as data_file:
        clustered=json.load(data_file, encoding="windows-1251")
        
    for i in clustered:
        name = u'УСПЕШНАЯ ГРУППА'
        if clustered[i]['id'] == meta['blockers']['channelId']:
            print(1)
            meta['blockers']['wc'] = clustered[i]['wc']
            meta['blockers']['eb'] = clustered[i]['eb']
            meta['blockers']['le'] = clustered[i]['le']
            meta['blockers']['shortest'] = clustered[i]['shortest']
            meta['blockers']['pagerank'] = clustered[i]['pagerank']
            
    for i in clustered:
        name = u'лиззка'
        if clustered[i]['id'] == meta['lizzka']['channelId']:
            print(1)
            meta['lizzka']['wc'] = clustered[i]['wc']
            meta['lizzka']['eb'] = clustered[i]['eb']
            meta['lizzka']['le'] = clustered[i]['le']
            meta['lizzka']['shortest'] = clustered[i]['shortest']
            meta['lizzka']['pagerank'] = clustered[i]['pagerank']
            
    for i in clustered:
        name = u'Клинское'
        if clustered[i]['id'] == meta['klinsky']['channelId']:
            print(1)
            meta['klinsky']['wc'] = clustered[i]['wc']
            meta['klinsky']['eb'] = clustered[i]['eb']
            meta['klinsky']['le'] = clustered[i]['le']
            meta['klinsky']['shortest'] = clustered[i]['shortest']
            meta['klinsky']['pagerank'] = clustered[i]['pagerank']
    
    for i in clustered:
        name = u'HYPE CAMP'
        if clustered[i]['id'] == meta['hypecamp']['channelId']:
            print(1)
            meta['hypecamp']['wc'] = clustered[i]['wc']
            meta['hypecamp']['eb'] = clustered[i]['eb']
            meta['hypecamp']['le'] = clustered[i]['le']
            meta['hypecamp']['shortest'] = clustered[i]['shortest']
            meta['hypecamp']['pagerank'] = clustered[i]['pagerank']
            
    for i in clustered:
        name = u'Maryana Ro'
        if clustered[i]['id'] == meta['rostar']['channelId']:
            print(1)
            meta['rostar']['wc'] = clustered[i]['wc']
            meta['rostar']['eb'] = clustered[i]['eb']
            meta['rostar']['le'] = clustered[i]['le']
            meta['veet1']['wc'] = clustered[i]['wc']
            meta['veet1']['eb'] = clustered[i]['eb']
            meta['veet1']['le'] = clustered[i]['le']
            meta['veet2']['wc'] = clustered[i]['wc']
            meta['veet2']['eb'] = clustered[i]['eb']
            meta['veet2']['le'] = clustered[i]['le']
            meta['rostar']['shortest'] = clustered[i]['shortest']
            meta['rostar']['pagerank'] = clustered[i]['pagerank']
            meta['veet1']['shortest'] = clustered[i]['shortest']
            meta['veet1']['pagerank'] = clustered[i]['pagerank']
            meta['veet2']['shortest'] = clustered[i]['shortest']
            meta['veet2']['pagerank'] = clustered[i]['pagerank']
            
    for i in clustered:
        name = u'versusbattleru'
        if clustered[i]['id'] == meta['versus']['channelId']:
            print(1)
            meta['versus']['wc'] = clustered[i]['wc']
            meta['versus']['eb'] = clustered[i]['eb']
            meta['versus']['le'] = clustered[i]['le']
            meta['versus']['shortest'] = clustered[i]['shortest']
            meta['versus']['pagerank'] = clustered[i]['pagerank']
            
# WHOLE DATASET
model = {}
for i in clustered:
    key = allChannels[i]['name']+'_blockers'
    model[key] = {}
    model[key]['status'] = clustered[i]['blockers']
    model[key]['statusCat'] = clustered[i]['blockersCat']
    
    model[key]['channelViews'] = clustered[i]['views']
    model[key]['channelVideo'] = clustered[i]['videos']
    model[key]['channelSubs'] = clustered[i]['subscribers']
    model[key]['wc'] = clustered[i]['wc']
    model[key]['eb'] = clustered[i]['eb']
    model[key]['le'] = clustered[i]['le']
    model[key]['shortest'] = clustered[i]['shortest']
    model[key]['pagerank'] = clustered[i]['pagerank']
    
    model[key]['authorWC'] = meta['blockers']['wc']
    model[key]['authorEB'] = meta['blockers']['eb']
    model[key]['authorLE'] = meta['blockers']['le']
    if model[key]['authorWC'] == model[key]['wc']:
        model[key]['wcMatch'] = 1
    else:
        model[key]['wcMatch'] = 0
    if model[key]['authorEB'] == model[key]['eb']:
        model[key]['ebMatch'] = 1
    else:
        model[key]['ebMatch'] = 0
    if model[key]['authorLE'] == model[key]['le']:
        model[key]['leMatch'] = 1
    else:
        model[key]['leMatch'] = 0
    model[key]['authorPath'] = meta['blockers']['shortest']
    model[key]['authorPG'] = meta['blockers']['pagerank'] 
    model[key]['authorViews'] = meta['blockers']['channelViews']  
    model[key]['authorVideo'] = meta['blockers']['channelVideo']  
    model[key]['authorSubs'] = meta['blockers']['channelSubs']      

    model[key]['comment'] = meta['blockers']['comment']
    model[key]['lendesc'] = meta['blockers']['lendesc']         
    model[key]['http'] = meta['blockers']['http']  
    model[key]['ad'] = meta['blockers']['ad']  
    model[key]['lentitle'] = meta['blockers']['lentitle']  
    model[key]['uppercase'] = meta['blockers']['uppercase']  
    model[key]['like'] = meta['blockers']['like']  
    model[key]['dislike'] = meta['blockers']['dislike']  
    model[key]['view'] = meta['blockers']['view']  
    model[key]['perview'] = int(meta['blockers']['view'])/int(meta['blockers']['channelViews'])
    
    
for i in clustered:
    key = allChannels[i]['name']+'_hypecamp'
    model[key] = {}
    model[key]['status'] = clustered[i]['hypecamp']
    model[key]['statusCat'] = clustered[i]['hypecampCat']
    
    model[key]['channelViews'] = clustered[i]['views']
    model[key]['channelVideo'] = clustered[i]['videos']
    model[key]['channelSubs'] = clustered[i]['subscribers']
    model[key]['wc'] = clustered[i]['wc']
    model[key]['eb'] = clustered[i]['eb']
    model[key]['le'] = clustered[i]['le']
    model[key]['shortest'] = clustered[i]['shortest']
    model[key]['pagerank'] = clustered[i]['pagerank']
    
    model[key]['authorWC'] = meta['hypecamp']['wc']
    model[key]['authorEB'] = meta['hypecamp']['eb']
    model[key]['authorLE'] = meta['hypecamp']['le']
    if model[key]['authorWC'] == model[key]['wc']:
        model[key]['wcMatch'] = 1
    else:
        model[key]['wcMatch'] = 0
    if model[key]['authorEB'] == model[key]['eb']:
        model[key]['ebMatch'] = 1
    else:
        model[key]['ebMatch'] = 0
    if model[key]['authorLE'] == model[key]['le']:
        model[key]['leMatch'] = 1
    else:
        model[key]['leMatch'] = 0
    model[key]['authorPath'] = meta['hypecamp']['shortest']
    model[key]['authorPG'] = meta['hypecamp']['pagerank'] 
    model[key]['authorViews'] = meta['hypecamp']['channelViews']  
    model[key]['authorVideo'] = meta['hypecamp']['channelVideo']  
    model[key]['authorSubs'] = meta['hypecamp']['channelSubs']      

    model[key]['comment'] = meta['hypecamp']['comment']
    model[key]['lendesc'] = meta['hypecamp']['lendesc']         
    model[key]['http'] = meta['hypecamp']['http']  
    model[key]['ad'] = meta['hypecamp']['ad']  
    model[key]['lentitle'] = meta['hypecamp']['lentitle']  
    model[key]['uppercase'] = meta['hypecamp']['uppercase']  
    model[key]['like'] = meta['hypecamp']['like']  
    model[key]['dislike'] = meta['hypecamp']['dislike']  
    model[key]['view'] = meta['hypecamp']['view']  
    model[key]['perview'] = int(meta['hypecamp']['view'])/int(meta['hypecamp']['channelViews'])
    
    
for i in clustered:
    key = allChannels[i]['name']+'_lizzka'
    model[key] = {}
    model[key]['status'] = clustered[i]['lizzka']
    model[key]['statusCat'] = clustered[i]['lizzkaCat']
    
    model[key]['channelViews'] = clustered[i]['views']
    model[key]['channelVideo'] = clustered[i]['videos']
    model[key]['channelSubs'] = clustered[i]['subscribers']
    model[key]['wc'] = clustered[i]['wc']
    model[key]['eb'] = clustered[i]['eb']
    model[key]['le'] = clustered[i]['le']
    model[key]['shortest'] = clustered[i]['shortest']
    model[key]['pagerank'] = clustered[i]['pagerank']
    
    model[key]['authorWC'] = meta['lizzka']['wc']
    model[key]['authorEB'] = meta['lizzka']['eb']
    model[key]['authorLE'] = meta['lizzka']['le']
    if model[key]['authorWC'] == model[key]['wc']:
        model[key]['wcMatch'] = 1
    else:
        model[key]['wcMatch'] = 0
    if model[key]['authorEB'] == model[key]['eb']:
        model[key]['ebMatch'] = 1
    else:
        model[key]['ebMatch'] = 0
    if model[key]['authorLE'] == model[key]['le']:
        model[key]['leMatch'] = 1
    else:
        model[key]['leMatch'] = 0
    model[key]['authorPath'] = meta['lizzka']['shortest']
    model[key]['authorPG'] = meta['lizzka']['pagerank'] 
    model[key]['authorViews'] = meta['lizzka']['channelViews']  
    model[key]['authorVideo'] = meta['lizzka']['channelVideo']  
    model[key]['authorSubs'] = meta['lizzka']['channelSubs']      

    model[key]['comment'] = meta['lizzka']['comment']
    model[key]['lendesc'] = meta['lizzka']['lendesc']         
    model[key]['http'] = meta['lizzka']['http']  
    model[key]['ad'] = meta['lizzka']['ad']  
    model[key]['lentitle'] = meta['lizzka']['lentitle']  
    model[key]['uppercase'] = meta['lizzka']['uppercase']  
    model[key]['like'] = meta['lizzka']['like']  
    model[key]['dislike'] = meta['lizzka']['dislike']  
    model[key]['view'] = meta['lizzka']['view']  
    model[key]['perview'] = int(meta['lizzka']['view'])/int(meta['lizzka']['channelViews'])
    

for i in clustered:
    key = allChannels[i]['name']+'_klinsky'
    model[key] = {}
    model[key]['status'] = clustered[i]['klinsky']
    model[key]['statusCat'] = clustered[i]['klinskyCat']
    
    model[key]['channelViews'] = clustered[i]['views']
    model[key]['channelVideo'] = clustered[i]['videos']
    model[key]['channelSubs'] = clustered[i]['subscribers']
    model[key]['wc'] = clustered[i]['wc']
    model[key]['eb'] = clustered[i]['eb']
    model[key]['le'] = clustered[i]['le']
    model[key]['shortest'] = clustered[i]['shortest']
    model[key]['pagerank'] = clustered[i]['pagerank']
    
    model[key]['authorWC'] = meta['klinsky']['wc']
    model[key]['authorEB'] = meta['klinsky']['eb']
    model[key]['authorLE'] = meta['klinsky']['le']
    if model[key]['authorWC'] == model[key]['wc']:
        model[key]['wcMatch'] = 1
    else:
        model[key]['wcMatch'] = 0
    if model[key]['authorEB'] == model[key]['eb']:
        model[key]['ebMatch'] = 1
    else:
        model[key]['ebMatch'] = 0
    if model[key]['authorLE'] == model[key]['le']:
        model[key]['leMatch'] = 1
    else:
        model[key]['leMatch'] = 0
    model[key]['authorPath'] = meta['klinsky']['shortest']
    model[key]['authorPG'] = meta['klinsky']['pagerank'] 
    model[key]['authorViews'] = meta['klinsky']['channelViews']  
    model[key]['authorVideo'] = meta['klinsky']['channelVideo']  
    model[key]['authorSubs'] = meta['klinsky']['channelSubs']      

    model[key]['comment'] = meta['klinsky']['comment']
    model[key]['lendesc'] = meta['klinsky']['lendesc']         
    model[key]['http'] = meta['klinsky']['http']  
    model[key]['ad'] = meta['klinsky']['ad']  
    model[key]['lentitle'] = meta['klinsky']['lentitle']  
    model[key]['uppercase'] = meta['klinsky']['uppercase']  
    model[key]['like'] = meta['klinsky']['like']  
    model[key]['dislike'] = meta['klinsky']['dislike']  
    model[key]['view'] = meta['klinsky']['view']  
    model[key]['perview'] = int(meta['klinsky']['view'])/int(meta['klinsky']['channelViews'])
    
for i in clustered:
    key = allChannels[i]['name']+'_rostar'
    model[key] = {}
    model[key]['status'] = clustered[i]['rostar']
    model[key]['statusCat'] = clustered[i]['rostarCat']
    
    model[key]['channelViews'] = clustered[i]['views']
    model[key]['channelVideo'] = clustered[i]['videos']
    model[key]['channelSubs'] = clustered[i]['subscribers']
    model[key]['wc'] = clustered[i]['wc']
    model[key]['eb'] = clustered[i]['eb']
    model[key]['le'] = clustered[i]['le']
    model[key]['shortest'] = clustered[i]['shortest']
    model[key]['pagerank'] = clustered[i]['pagerank']
    
    model[key]['authorWC'] = meta['rostar']['wc']
    model[key]['authorEB'] = meta['rostar']['eb']
    model[key]['authorLE'] = meta['rostar']['le']
    if model[key]['authorWC'] == model[key]['wc']:
        model[key]['wcMatch'] = 1
    else:
        model[key]['wcMatch'] = 0
    if model[key]['authorEB'] == model[key]['eb']:
        model[key]['ebMatch'] = 1
    else:
        model[key]['ebMatch'] = 0
    if model[key]['authorLE'] == model[key]['le']:
        model[key]['leMatch'] = 1
    else:
        model[key]['leMatch'] = 0
    model[key]['authorPath'] = meta['rostar']['shortest']
    model[key]['authorPG'] = meta['rostar']['pagerank'] 
    model[key]['authorViews'] = meta['rostar']['channelViews']  
    model[key]['authorVideo'] = meta['rostar']['channelVideo']  
    model[key]['authorSubs'] = meta['rostar']['channelSubs']      

    model[key]['comment'] = meta['rostar']['comment']
    model[key]['lendesc'] = meta['rostar']['lendesc']         
    model[key]['http'] = meta['rostar']['http']  
    model[key]['ad'] = meta['rostar']['ad']  
    model[key]['lentitle'] = meta['rostar']['lentitle']  
    model[key]['uppercase'] = meta['rostar']['uppercase']  
    model[key]['like'] = meta['rostar']['like']  
    model[key]['dislike'] = meta['rostar']['dislike']  
    model[key]['view'] = meta['rostar']['view']  
    model[key]['perview'] = int(meta['rostar']['view'])/int(meta['rostar']['channelViews'])

for i in clustered:
    key = allChannels[i]['name']+'_veet1'
    model[key] = {}
    model[key]['status'] = clustered[i]['veet1']
    model[key]['statusCat'] = clustered[i]['veet1Cat']
    
    model[key]['channelViews'] = clustered[i]['views']
    model[key]['channelVideo'] = clustered[i]['videos']
    model[key]['channelSubs'] = clustered[i]['subscribers']
    model[key]['wc'] = clustered[i]['wc']
    model[key]['eb'] = clustered[i]['eb']
    model[key]['le'] = clustered[i]['le']
    model[key]['shortest'] = clustered[i]['shortest']
    model[key]['pagerank'] = clustered[i]['pagerank']
    
    model[key]['authorWC'] = meta['veet1']['wc']
    model[key]['authorEB'] = meta['veet1']['eb']
    model[key]['authorLE'] = meta['veet1']['le']
    if model[key]['authorWC'] == model[key]['wc']:
        model[key]['wcMatch'] = 1
    else:
        model[key]['wcMatch'] = 0
    if model[key]['authorEB'] == model[key]['eb']:
        model[key]['ebMatch'] = 1
    else:
        model[key]['ebMatch'] = 0
    if model[key]['authorLE'] == model[key]['le']:
        model[key]['leMatch'] = 1
    else:
        model[key]['leMatch'] = 0
    model[key]['authorPath'] = meta['veet1']['shortest']
    model[key]['authorPG'] = meta['veet1']['pagerank'] 
    model[key]['authorViews'] = meta['veet1']['channelViews']  
    model[key]['authorVideo'] = meta['veet1']['channelVideo']  
    model[key]['authorSubs'] = meta['veet1']['channelSubs']      

    model[key]['comment'] = meta['veet1']['comment']
    model[key]['lendesc'] = meta['veet1']['lendesc']         
    model[key]['http'] = meta['veet1']['http']  
    model[key]['ad'] = meta['veet1']['ad']  
    model[key]['lentitle'] = meta['veet1']['lentitle']  
    model[key]['uppercase'] = meta['veet1']['uppercase']  
    model[key]['like'] = meta['veet1']['like']  
    model[key]['dislike'] = meta['veet1']['dislike']  
    model[key]['view'] = meta['veet1']['view']  
    model[key]['perview'] = int(meta['veet1']['view'])/int(meta['veet1']['channelViews'])

for i in clustered:
    key = allChannels[i]['name']+'_veet2'
    model[key] = {}
    model[key]['status'] = clustered[i]['veet2']
    model[key]['statusCat'] = clustered[i]['veet2Cat']
    
    model[key]['channelViews'] = clustered[i]['views']
    model[key]['channelVideo'] = clustered[i]['videos']
    model[key]['channelSubs'] = clustered[i]['subscribers']
    model[key]['wc'] = clustered[i]['wc']
    model[key]['eb'] = clustered[i]['eb']
    model[key]['le'] = clustered[i]['le']
    model[key]['shortest'] = clustered[i]['shortest']
    model[key]['pagerank'] = clustered[i]['pagerank']
    
    model[key]['authorWC'] = meta['veet2']['wc']
    model[key]['authorEB'] = meta['veet2']['eb']
    model[key]['authorLE'] = meta['veet2']['le']
    if model[key]['authorWC'] == model[key]['wc']:
        model[key]['wcMatch'] = 1
    else:
        model[key]['wcMatch'] = 0
    if model[key]['authorEB'] == model[key]['eb']:
        model[key]['ebMatch'] = 1
    else:
        model[key]['ebMatch'] = 0
    if model[key]['authorLE'] == model[key]['le']:
        model[key]['leMatch'] = 1
    else:
        model[key]['leMatch'] = 0
    model[key]['authorPath'] = meta['veet2']['shortest']
    model[key]['authorPG'] = meta['veet2']['pagerank'] 
    model[key]['authorViews'] = meta['veet2']['channelViews']  
    model[key]['authorVideo'] = meta['veet2']['channelVideo']  
    model[key]['authorSubs'] = meta['veet2']['channelSubs']      

    model[key]['comment'] = meta['veet2']['comment']
    model[key]['lendesc'] = meta['veet2']['lendesc']         
    model[key]['http'] = meta['veet2']['http']  
    model[key]['ad'] = meta['veet2']['ad']  
    model[key]['lentitle'] = meta['veet2']['lentitle']  
    model[key]['uppercase'] = meta['veet2']['uppercase']  
    model[key]['like'] = meta['veet2']['like']  
    model[key]['dislike'] = meta['veet2']['dislike']  
    model[key]['view'] = meta['veet2']['view']  
    model[key]['perview'] = int(meta['veet2']['view'])/int(meta['veet2']['channelViews'])

for i in clustered:
    key = allChannels[i]['name']+'_versus'
    model[key] = {}
    model[key]['status'] = clustered[i]['versus']
    model[key]['statusCat'] = clustered[i]['versusCat']
    
    model[key]['channelViews'] = clustered[i]['views']
    model[key]['channelVideo'] = clustered[i]['videos']
    model[key]['channelSubs'] = clustered[i]['subscribers']
    model[key]['wc'] = clustered[i]['wc']
    model[key]['eb'] = clustered[i]['eb']
    model[key]['le'] = clustered[i]['le']
    model[key]['shortest'] = clustered[i]['shortest']
    model[key]['pagerank'] = clustered[i]['pagerank']
    
    model[key]['authorWC'] = meta['versus']['wc']
    model[key]['authorEB'] = meta['versus']['eb']
    model[key]['authorLE'] = meta['versus']['le']
    if model[key]['authorWC'] == model[key]['wc']:
        model[key]['wcMatch'] = 1
    else:
        model[key]['wcMatch'] = 0
    if model[key]['authorEB'] == model[key]['eb']:
        model[key]['ebMatch'] = 1
    else:
        model[key]['ebMatch'] = 0
    if model[key]['authorLE'] == model[key]['le']:
        model[key]['leMatch'] = 1
    else:
        model[key]['leMatch'] = 0
    model[key]['authorPath'] = meta['versus']['shortest']
    model[key]['authorPG'] = meta['versus']['pagerank'] 
    model[key]['authorViews'] = meta['versus']['channelViews']  
    model[key]['authorVideo'] = meta['versus']['channelVideo']  
    model[key]['authorSubs'] = meta['versus']['channelSubs']      

    model[key]['comment'] = meta['versus']['comment']
    model[key]['lendesc'] = meta['versus']['lendesc']         
    model[key]['http'] = meta['versus']['http']  
    model[key]['ad'] = meta['versus']['ad']  
    model[key]['lentitle'] = meta['versus']['lentitle']  
    model[key]['uppercase'] = meta['versus']['uppercase']  
    model[key]['like'] = meta['versus']['like']  
    model[key]['dislike'] = meta['versus']['dislike']  
    model[key]['view'] = meta['versus']['view']  
    model[key]['perview'] = int(meta['versus']['view'])/int(meta['versus']['channelViews'])
