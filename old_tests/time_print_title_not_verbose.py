from __future__ import unicode_literals
import youtube_dl
from youtube_dl.utils import DateRange
import argparse
import pandas as pd

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
parser.add_argument('--w', type=bool, default=True, help='bool do not overwrite')
# quiet
parser.add_argument('--q', type=bool, default=False, help='bool do not overwrite')


# Switch
#parser.add_argument('--switch', action='store_true', help='A boolean switch')

args = parser.parse_args()
# print args.__dict__

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
    'ignoreerrors':args.i,
    'verbose':False
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
