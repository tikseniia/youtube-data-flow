# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 12:08:45 2018

@author: Ksenia
"""

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

def videos_list_most_popular(client, **kwargs):
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


def playlist_items_list_by_playlist_id(client, **kwargs):
  # See full sample for function
  kwargs = remove_empty_kwargs(**kwargs)

  response = client.playlistItems().list(
    **kwargs
  ).execute()

  return response


def videos_list_by_id(client, **kwargs):
  # See full sample for function
  kwargs = remove_empty_kwargs(**kwargs)

  response = client.videos().list(
    **kwargs
  ).execute()

  return response


# IMPLEMENTATION
  
if __name__ == '__main__':
  # When running locally, disable OAuthlib's HTTPs verification. When
  # running in production *do not* leave this option enabled.
  os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
  client = get_authenticated_service()

    uChannels = likedChannels
    names = []
    todel = []
    for i in allChannels:
        name = allChannels[i]['name']
        if name in names:
            todel.append(i)
        else:
            names.append(name)
            
    for i in todel:
        del uChannels[i]

    start = False
    for i in uChannels:
        if i == 'UC1gRSCxTJIFa-vS2hr1NGoA':
            start = True
        
        if start:
            c = channels_list_by_id(client,
                part='snippet,contentDetails,statistics',
                id=i)
            try:
                uChannels[i]['likes'] = c['items'][0]['contentDetails']['relatedPlaylists']['likes']
                
                uChannels[i]['playlist'] = []
                end = 0
                nextPage = ''
                while end == 0:
                    p = playlist_items_list_by_playlist_id(client,
                                part='snippet,contentDetails',
                                maxResults=50,
                                playlistId=uChannels[i]['likes'], pageToken=nextPage)
                    
                    
                    for j in range(0, len(p['items'])):
                        v = p['items'][j]['contentDetails']['videoId']
                        print(v)
                        uChannels[i]['playlist'].append(v)
                        
                        
                    try:
                        nextPage = p['nextPageToken']
                    except:
                        end = 1
                        nextPage = ''
            except:
                pass
        
        
    for i in uChannels:
        try:
            print(uChannels[i]['playlist'])
        except:
            uChannels[i]['playlist'] = []
      
    start = False
    for i in uChannels:
        if i == 'UCCBQj8B4jPsUl6DJTTPmKkQ':
            start = True
        
        if start:
            uChannels[i]['playlistAuthorsId'] = []
            uChannels[i]['playlistAuthors'] = []
            for j in uChannels[i]['playlist']:
                v = videos_list_by_id(client,
                       part='snippet',
                       id=j)
                if len(v['items']) > 0:
                    try:
                        if v['items'][0]['snippet']['channelTitle'] in uChannels[i]['playlistAuthors']:
                            pass
                        else:
                            uChannels[i]['playlistAuthors'].append(v['items'][0]['snippet']['channelTitle'])
                            uChannels[i]['playlistAuthorsId'].append(v['items'][0]['snippet']['channelId'])
                            print(v['items'][0]['snippet']['channelTitle'])
                    except:
                        pass
           
            
    #ADD LIKED (FROM PLAYLIST) CHANNELS TO COMMON DS
    
    likedChannels = {}
    names = []
    start = False
    
    for i in uChannels:
        if i == 'UCZ7bIDLWElnJa0-lPHUSyQg':
            start = True
            
        if start:
            for j in uChannels[i]['playlistAuthorsId']:
                c = channels_list_by_id(client,
                part='snippet,contentDetails,statistics',
                id=j)
                
                if len(c['items']) != 0:
                    if c['items'][0]['snippet']['localized']['title'] in names:
                        pass
                    else:
                        names.append(c['items'][0]['snippet']['localized']['title'])
                    
                        likedChannels[j] = {}
                        likedChannels[j]['id'] = j
                        likedChannels[j]['name'] = c['items'][0]['snippet']['localized']['title']
                        likedChannels[j]['views'] = c['items'][0]['statistics']['viewCount']
                        likedChannels[j]['videos'] = c['items'][0]['statistics']['videoCount']
                        likedChannels[j]['subscribers'] = c['items'][0]['statistics']['subscriberCount']
                        
                        print likedChannels[j]['name']
                else:
                    print len(c['items'])
            
