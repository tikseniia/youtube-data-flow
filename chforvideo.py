# -*- coding: utf-8 -*-
"""
Created on Sat May 12 14:04:59 2018

@author: Ksenia
"""

import pickle
import tarfile
# open a .spydata file
filename = 'messages.spydata'
tar = tarfile.open(filename, "r")
# extract all pickled files to the current working directory
tar.extractall()
extracted_files = tar.getnames()
for f in extracted_files:
    if f.endswith('.pickle'):
         with open(f, 'rb') as fdesc:
             data = pickle.loads(fdesc.read())
             
veet1 = data['veet1']
veet2 = data['veet2']
versus = data['versus']
klinsky = data['klinsky']
blockers = data['blockers']
rostar = data['rostar']
hypecamp= data['hypecamp']
cola = data['cola']
lizzka = data['lizzka']

allTitles = []
for i in allChannels:
    allTitles.append(allChannels[i]['name'])
for i in uChannels:
    if uChannels[i]['name'] in allTitles:
        pass
    else:
        try:
            print len(uChannels[i]['playlistAuthors'])
            allTitles.append(uChannels[i]['name'])
        except:
            pass
        
toLoadId = []
toLoadTitle = []
for i in blockers:
    name = blockers[i]['snippet']['channelTitle']
    id = blockers[i]['snippet']['channelId']
    if name in allTitles:
        pass
    else:
        toLoadId.append(id)
        toLoadTitle.append(name)
        
for i in cola:
    name = cola[i]['snippet']['channelTitle']
    id = cola[i]['snippet']['channelId']
    if name in allTitles:
        pass
    else:
        if name in toLoadTitle:
            pass
        else:
            toLoadId.append(id)
            toLoadTitle.append(name)
            
for i in hypecamp:
    name = hypecamp[i]['snippet']['channelTitle']
    id = hypecamp[i]['snippet']['channelId']
    if name in allTitles:
        pass
    else:
        if name in toLoadTitle:
            pass
        else:
            toLoadId.append(id)
            toLoadTitle.append(name)
            
for i in klinsky:
    name = klinsky[i]['snippet']['channelTitle']
    id = klinsky[i]['snippet']['channelId']
    if name in allTitles:
        pass
    else:
        if name in toLoadTitle:
            pass
        else:
            toLoadId.append(id)
            toLoadTitle.append(name)
            
for i in lizzka:
    name = lizzka[i]['snippet']['channelTitle']
    id = lizzka[i]['snippet']['channelId']
    if name in allTitles:
        pass
    else:
        if name in toLoadTitle:
            pass
        else:
            toLoadId.append(id)
            toLoadTitle.append(name)
            
for i in rostar:
    name = rostar[i]['snippet']['channelTitle']
    id = rostar[i]['snippet']['channelId']
    if name in allTitles:
        pass
    else:
        if name in toLoadTitle:
            pass
        else:
            toLoadId.append(id)
            toLoadTitle.append(name)
            
for i in veet1:
    name = veet1[i]['snippet']['channelTitle']
    id = veet1[i]['snippet']['channelId']
    if name in allTitles:
        pass
    else:
        if name in toLoadTitle:
            pass
        else:
            toLoadId.append(id)
            toLoadTitle.append(name)
            
for i in veet2:
    name = veet2[i]['snippet']['channelTitle']
    id = veet2[i]['snippet']['channelId']
    if name in allTitles:
        pass
    else:
        if name in toLoadTitle:
            pass
        else:
            toLoadId.append(id)
            toLoadTitle.append(name)
            
for i in versus:
    name = versus[i]['snippet']['channelTitle']
    id = versus[i]['snippet']['channelId']
    if name in allTitles:
        pass
    else:
        if name in toLoadTitle:
            pass
        else:
            toLoadId.append(id)
            toLoadTitle.append(name)
    
if __name__ == '__main__':
    # When running locally, disable OAuthlib's HTTPs verification. When
    # running in production *do not* leave this option enabled.
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    client = get_authenticated_service()
        
    iChannels = {}
    names = []
    for j in toLoadId:
       c = channels_list_by_id(client,
                               part='snippet,contentDetails,statistics',
                               id=j)
       if len(c['items']) != 0:
           if c['items'][0]['snippet']['localized']['title'] in names:
               pass
           else:
               names.append(c['items'][0]['snippet']['localized']['title'])
                        
               iChannels[j] = {}
               iChannels[j]['id'] = j
               iChannels[j]['name'] = c['items'][0]['snippet']['localized']['title']
               iChannels[j]['views'] = c['items'][0]['statistics']['viewCount']
               iChannels[j]['videos'] = c['items'][0]['statistics']['videoCount']
               iChannels[j]['subscribers'] = c['items'][0]['statistics']['subscriberCount']
                            
               print iChannels[j]['name']
               
               try:
                    iChannels[j]['likes'] = c['items'][0]['contentDetails']['relatedPlaylists']['likes']
                    
                    iChannels[j]['playlist'] = []
                    end = 0
                    nextPage = ''
                    while end == 0:
                        p = playlist_items_list_by_playlist_id(client,
                                    part='snippet,contentDetails',
                                    maxResults=50,
                                    playlistId=iChannels[j]['likes'], pageToken=nextPage)
                        
                        
                        for i in range(0, len(p['items'])):
                            v = p['items'][i]['contentDetails']['videoId']
                            print(v)
                            iChannels[j]['playlist'].append(v)
                            
                            
                        try:
                            nextPage = p['nextPageToken']
                        except:
                            end = 1
                            nextPage = ''
               except:
                   pass
       else:
            print len(c['items'])
            
    for i in iChannels:
        try:
            print(iChannels[i]['playlist'])
        except:
            iChannels[i]['playlist'] = []
      
    start = False
    for i in iChannels:   
        if i == 'UCAyCo_hIuUPaFey8ofdK2Wg':
            start = True
        if start:
            iChannels[i]['playlistAuthorsId'] = []
            iChannels[i]['playlistAuthors'] = []
            for j in iChannels[i]['playlist']:
                v = videos_list_by_id(client,
                       part='snippet',
                       id=j)
                if len(v['items']) > 0:
                    try:
                        if v['items'][0]['snippet']['channelTitle'] in iChannels[i]['playlistAuthors']:
                            pass
                        else:
                            iChannels[i]['playlistAuthors'].append(v['items'][0]['snippet']['channelTitle'])
                            iChannels[i]['playlistAuthorsId'].append(v['items'][0]['snippet']['channelId'])
                            print(v['items'][0]['snippet']['channelTitle'])
                    except:
                        pass
        

