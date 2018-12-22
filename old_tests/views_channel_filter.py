from __future__ import unicode_literals
import youtube_dl
from youtube_dl.utils import DateRange
import argparse
import pandas as pd
from datetime import datetime
# Instantiate the parser
parser = argparse.ArgumentParser(description='supply url compulsroy')
# url to process
# n0amE96UjWk
parser.add_argument('--url', type=str, default="https://www.youtube.com/channel/UCzkLUqHN9Ov0fwbh2QF0sGQ",
                    help='A required url argument')
# number of views
parser.add_argument('--views', type=int, default=1,
                    help='number of views')
# date range
################not working now-4years is not interpted righ
parser.add_argument('--tfrom', type=str, default="20060101",
                    help='date range in ytdl format')
parser.add_argument('--ttill', type=str, default="20190101",
                    help='date range in ytdl format')
# format
parser.add_argument('--fmat', type=str, default="bestvideo[ext=mp4][height=1080][height>=720],bestaudio[ext=m4a][abr<192]",
                    help='format in ytdl format')
# output location
# win
# default="Y:\yt2018\%%(uploader_id)s_%%(uploader)s\%%(id)s_%%(title)s_%%(upload_date)s_%%(height)s_%%(abr)s_%%(format_id)s.%%(ext)s"
# linux
# default="/home/durai/shared_yt2018/%(uploader_id)s_%(uploader)s/%(id)s_%(title)s_%(upload_date)s_%(height)s_%(abr)s_%(format_id)s.%(ext)s"
parser.add_argument('--oloc', type=str, default="/home/durai/shared_yt2018/%(channel_id)s_%(playlist_id)s_%(uploader_id)s_%(uploader)s/%(id)s_%(title)s_%(upload_date)s_%(height)s_%(abr)s_%(format_id)s.%(ext)s",
                    help='output location')
# FLAGS
# simulate 
parser.add_argument('--sim', type=bool, default=True,
                    help='bool simulate')
# print title
parser.add_argument('--ttl', type=bool, default=True, help='bool print title')
# ignore errors
parser.add_argument('--i', type=bool, default=True,
                    help='bool ignore errors')
# do not overwrite
parser.add_argument('--w', type=bool, default=True,
                    help='bool do not overwrite')
# do not overwrite
parser.add_argument('--v', type=bool, default=True,
                    help='bool verbose')
# quiet
parser.add_argument('--q', type=bool, default=False, help='bool quiet')
# thumbnail
parser.add_argument('--thumb', type=bool, default=False,
                    help='bool thumbnail')
# json
parser.add_argument('--meta', type=bool, default=False,
                    help='bool json')
# proxies
parser.add_argument('--prx', type=str, default='""',
                    help='bool proxy address')

args = parser.parse_args()
# print args.__dict__

print("Video url:")
print(args.url)
print("views filter:")
print(args.views)
print("upload date range:")
print(DateRange(args.tfrom))
print(DateRange(args.ttill))
print("file name format:")
print(args.fmat)
print("output path:")
print(args.oloc)
print("simulate:")
print(args.sim)
print("print title:")
print(args.ttl)
print("ignore errors:")
print(args.i)
print("don't overwrite:")
print(args.w)
print("verbose:")
print(args.v)
print("quiet:")
print(args.q)
print("bool thumbnail:")
print(args.thumb)
print("bool metadata:")
print(args.meta)
print("proxy:")
print(args.prx)

#count number of hits from channle given filters
ydl_opts = {
    'simulate': args.sim,
    'forcetitle':args.ttl,
    'min_views': args.views,
    'outtmpl':args.oloc,
    'daterange' : DateRange(args.tfrom,args.ttill),
    'writethumbnail':args.thumb,
    'writeinfojson':args.meta,
    'format': args.fmat,
    'ignoreerrors':args.i,
    'nooverwrites':args.w,
    'verbose':args.v,
    'quiet':args.q,
    #'proxy':args.prx
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
