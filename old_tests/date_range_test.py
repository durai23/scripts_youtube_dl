from __future__ import unicode_literals
import youtube_dl
from youtube_dl.utils import DateRange
import argparse
import pandas as pd

# Instantiate the parser
parser = argparse.ArgumentParser(description='supply url compulsroy')

# url to process
# 20170614 upload date
parser.add_argument('--url', type=str, default="zVYa0abkdkE",
                    help='A required url argument')
# print title
parser.add_argument('--ttl', type=bool, default=True, help='bool print title')
# date range
parser.add_argument('--tfrom', type=str, default="20060101",
                    help='date range in ytdl format')
# date range
parser.add_argument('--ttill', type=str, default="20190101",
                    help='date range in ytdl format')
# simulate 
parser.add_argument('--sim', type=bool, default=True,
                    help='bool simulate')
# quiet
parser.add_argument('--q', type=bool, default=False, help='bool do not overwrite')


# Switch
#parser.add_argument('--switch', action='store_true', help='A boolean switch')

args = parser.parse_args()
print args.__dict__
print "parsed date"
# print("Video url:")
# print(args.url)
# print("simulate:")
# print(args.sim)
# print("print title:")
# print(args.ttl)
# print("views filter:")
# print(args.views)
# print("output path:")
# print(args.oloc)
# print("upload date range:")
# print(DateRange(args.trange))
# print("bool thumbnail:")
# print(args.thumb)
# print("bool metadata:")
# print(args.meta)
# print("file name format:")
# print(args.fmat)
# print("ignore errors:")
# print(args.i)
# print("don't overwrite:")
# print(args.w)
# print("quiet:")
# print(args.q)

#count number of hits from channle given filters
ydl_opts = {
    'simulate': args.sim,
    'forcetitle':args.ttl,
    #'min_views': args.views,
    #'outtmpl':args.oloc,
    'daterange' : DateRange(args.tfrom,args.ttill),
    #'writethumbnail':args.thumb,
    #'writeinfojson':args.meta,
    #'format': args.fmat,
    #'ignoreerrors':args.i,
    #'nooverwrites':args.w,
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
