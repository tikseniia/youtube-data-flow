# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 13:45:04 2018

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
CLIENT_SECRETS_FILE = "C:\Users\Ksenia\Documents\Python Scripts\diploma\client_secret.json"

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


def search_list_related_videos(client, **kwargs):
  # See full sample for function
  kwargs = remove_empty_kwargs(**kwargs)

  response = client.search().list(
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


def subscriptions_list_by_channel_id(client, **kwargs):
  # See full sample for function
  kwargs = remove_empty_kwargs(**kwargs)

  response = client.subscriptions().list(
    **kwargs
  ).execute()

  return response


def merge_two_dicts(x, y):
    z = x.copy()
    z.update(y)
    return z


if __name__ == '__main__':
  # When running locally, disable OAuthlib's HTTPs verification. When
  # running in production *do not* leave this option enabled.
  os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
  client = get_authenticated_service()
  
  arr = videos_list_most_popular(client,
    part='id,snippet,contentDetails,statistics',
    chart='mostPopular',
    regionCode='RU',
    videoCategoryId='',
    maxResults=50)
  
  related = []
  
  for i in range(0, 50):
      ID = arr['items'][i]['id']
      r = search_list_related_videos(client,
        part='snippet',
        relatedToVideoId=ID,
        type='video',
        maxResults=50)
      related.append(r)
      
   related1 = []
   
   for i in range(0, 50):
       for j in range(0, len(related[i]['items'])):
           ID = related[i]['items'][j]['id']['videoId']
           r = search_list_related_videos(client,
            part='snippet',
            relatedToVideoId=ID,
            type='video',
            maxResults=50)
           related1.append(r)
           

    channels = {}
    for i in range(0, len(arr['items'])):
        key = arr['items'][i]['snippet']['channelId']
        value = {'id': arr['items'][i]['snippet']['channelId'],
               'name': arr['items'][i]['snippet']['channelTitle']}
        channels[key] = value
        
    for i in range(0, len(arr['items'])):
       for j in range(0, len(related[i]['items'])):
           key = related[i]['items'][j]['snippet']['channelId']
           value = {'id': related[i]['items'][j]['snippet']['channelId'],
               'name': related[i]['items'][j]['snippet']['channelTitle']}
           channels[key] = value
           
    for i in range(0, len(arr['items'])):
       for j in range(0, len(related[i]['items'])):
           for k in range(0, len(related1[j]['items'])):
               key = related1[j]['items'][k]['snippet']['channelId']
               value = {'id': related1[j]['items'][k]['snippet']['channelId'],
               'name': related1[j]['items'][k]['snippet']['channelTitle']}
           channels[key] = value
           
           
    # SEARCH FOR CHANNEL ATTRS & FILTER BY FOLLOWERS
    for i in channels:
        c = channels_list_by_id(client,
            part='snippet,contentDetails,statistics',
            id=i)
        channels[i]['views'] = c['items'][0]['statistics']['viewCount']
        channels[i]['videos'] = c['items'][0]['statistics']['viewCount']
        channels[i]['subscribers'] = c['items'][0]['statistics']['subscriberCount']
        
    channelsPruned = {k: v for k, v in channels.iteritems() if int(v['subscribers']) > 50000}


    # SUBSCRIPTIONS FOR CHANNELS
    for i in channelsPruned:
        try:
            c = subscriptions_list_by_channel_id(client,
                part='snippet,contentDetails',
                channelId=i)
            channelsPruned[i]['related'] = []
            for j in range(0, len(c['items'])):
                channelsPruned[i]['related'].append(c['items'][j]['snippet']['resourceId']['channelId'])
                print(c['items'][j]['snippet']['resourceId']['channelId'])
        except:
            channelsPruned[i]['related'] = []
            
            
    # DATA COLLECTION FOR RELATED CHANNELS
    relatedChannels = {}
    for i in channelsPruned:
        for j in channelsPruned[i]['related']:
            c = channels_list_by_id(client,
                part='snippet,contentDetails,statistics',
                id=j)
            relatedChannels[j] = {}
            relatedChannels[j]['id'] = j
            relatedChannels[j]['name'] = c['items'][0]['snippet']['localized']['title']
            relatedChannels[j]['views'] = c['items'][0]['statistics']['viewCount']
            relatedChannels[j]['videos'] = c['items'][0]['statistics']['videoCount']
            relatedChannels[j]['subscribers'] = c['items'][0]['statistics']['subscriberCount']
            
            
    for i in relatedChannels:
        try:
            c = subscriptions_list_by_channel_id(client,
                part='snippet,contentDetails',
                channelId=i)
            relatedChannels[i]['related'] = []
            for j in range(0, len(c['items'])):
                relatedChannels[i]['related'].append(c['items'][j]['snippet']['resourceId']['channelId'])
                print(c['items'][j]['snippet']['resourceId']['channelId'])
        except:
            relatedChannels[i]['related'] = []
            
            
    allChannels = merge_two_dicts(channelsPruned, relatedChannels)
