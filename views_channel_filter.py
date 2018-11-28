from __future__ import unicode_literals
import youtube_dl
from youtube_dl.utils import DateRange
import argparse
import pandas as pd
#TODO
#date range not working
#log video as downloaded completely and in csv
    #check for presence of mp4, m4a, jpg
    #delete jpg and json without 1080 in name
    #log uploader_id,video_id,json_path,video_path,aud_path,thumbanil_path,duraion,quality,upload_date,views,tags

# SOURCES
# diigo csv
#     auto created csv with TAGS
#         RENAME tags to creat folder hierarchy
# scrapebox output
#     manually created csv with KEYWORDS
#         have to then youse youtube-dl to filter videos by views, date etc
#         or use scrapebox to filter by date - crat custom engine
# channels
#     auto named CHANNEL_ID
# custom lists
#     just name custom list

#tagging 
#decided to make hierrarchical folders for tags

#conditional passign of defualt outtmpl whether channel or single video
#use case for how to extract most interesting videos from say cnn or fox

#SOLVED
# to test if channel filter by views works
#minimum functionality of  susccesful wondows bat file replicated

# TODO
# filter by date is not workign due to daterange trivial issues

# TODO
# hack to get youtube id by using curl -s?????

# TODO
# scrapebox 
#     first how to get relevant ie views+date content
#         search for hwo to haravest youtube urls by views
# jdownloader can dl entire channle


# Instantiate the parser
parser = argparse.ArgumentParser(description='supply url compulsroy')

# url to process
parser.add_argument('--url', type=str, required=True,
                    help='A required url argument')
# simulate 
parser.add_argument('--sim', type=bool, default=True,
                    help='bool simulate')
# print title
parser.add_argument('--ttl', type=bool, default=True, help='bool print title')
# number of views
parser.add_argument('--views', type=int, default=1,
                    help='number of views')
# output location
parser.add_argument('--oloc', type=str, default="F:\yt2018\%%(uploader_id)s_%%(uploader)s\%%(id)s_%%(title)s_%%(upload_date)s_%%(height)s_%%(abr)s_%%(format_id)s.%%(ext)s",
                    help='output location')
# date range
################not working now-4years is not interpted righ
parser.add_argument('--trange', type=str, default="now-4years",
                    help='date range in ytdl format')
# thumbnail
parser.add_argument('--thumb', type=bool, default=False,
                    help='bool thumbnail')
# json
parser.add_argument('--meta', type=bool, default=False,
                    help='bool json')
# format
parser.add_argument('--fmat', type=str, default="bestvideo[ext=mp4][height=1080][height>=720],bestaudio[ext=m4a][abr<192]",
                    help='format in ytdl format')
# ignore errors
parser.add_argument('--i', type=bool, default=True,
                    help='bool ignore errors')
# do not overwrite
parser.add_argument('--w', type=bool, default=True,
                    help='bool do not overwrite')
# quiet
parser.add_argument('--q', type=bool, default=False, help='bool do not overwrite')


# Switch
#parser.add_argument('--switch', action='store_true', help='A boolean switch')

args = parser.parse_args()
print args.__dict__

print("Video url:")
print(args.url)
print("simulate:")
print(args.sim)
print("print title:")
print(args.ttl)
print("views filter:")
print(args.views)
print("output path:")
print(args.oloc)
print("upload date range:")
print(DateRange(args.trange))
print("bool thumbnail:")
print(args.thumb)
print("bool metadata:")
print(args.meta)
print("file name format:")
print(args.fmat)
print("ignore errors:")
print(args.i)
print("don't overwrite:")
print(args.w)
print("quiet:")
print(args.q)

#count number of hits from channle given filters
ydl_opts = {
    'simulate': args.sim,
    'forcetitle':args.ttl,
    'min_views': args.views,
    'outtmpl':args.oloc,
    #'daterange': args.trange,
    'writethumbnail':args.thumb,
    'writeinfojson':args.meta,
    'format': args.fmat,
    'ignoreerrors':args.i,
    'nooverwrites':args.w,
    'quiet':args.q
    #'logger': MyLogger(),
    #'progress_hooks': [my_hook],
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([args.url])
#ydl=youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})

#with ydl:
#    result = ydl.extract_info(
#        'http://www.youtube.com/watch?v=BaW_jenozKc',
#        download=False # We just want to extract the info
#    )
#
#if 'entries' in result:
#    # Can be a playlist or a list of videos
#    video = result['entries'][0]
#else:
#    # Just a video
#    video = result
#
#print(video)
#video_url = video['url']
#print(video_url)
