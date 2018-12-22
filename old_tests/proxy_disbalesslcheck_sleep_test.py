from __future__ import unicode_literals
import youtube_dl
from youtube_dl.utils import DateRange
import argparse
# import pandas as pd
from datetime import datetime
# Instantiate the parser

cygpath="/cygdrive/y/yt2018/%(playlist_id)s_%(playlist_title)s/%(id)s_%(title)s_%(upload_date)s_%(height)s_%(abr)s_%(format_id)s.%(ext)s"
# need to chagne below paths to remove channel id and uplaoder id
winpath2="Y:\yt2018\%%(playlist_id)s_%%(playlist_title)s\%%(id)s_%%(title)s_%%(upload_date)s_%%(height)s_%%(abr)s_%%(format_id)s.%%(ext)s"
winpath="Y:\yt2018\%(playlist_id)s_%(playlist_title)s\%(id)s_%(title)s_%(upload_date)s_%(height)s_%(abr)s_%(format_id)s.%(ext)s"
vmpath="/home/durai/shared_yt2018/%(playlist_id)s_%(playlist_title)s/%(id)s_%(title)s_%(upload_date)s_%(height)s_%(abr)s_%(format_id)s.%(ext)s"

origfrmat="bestvideo[ext=mp4][height=1080][height>=720],bestaudio[ext=m4a][abr<192]"
bestfrmat="best"
bestfrmat2="bestvideo[ext=mp4][height=1080][height>=720],bestaudio[ext=m4a][abr<192]"
defrmat2="best[ext=mp4][height<=1080][height>=720]"
defrmat="best[ext=mp4][height<=1080][height>=720]"
wrstfrmat="worstvideo[ext=mp4][height=1080][height>=720],worstaudio[ext=m4a][abr<192]"
bestvid="bestvideo[height<=1080][ext=mp4]"
bestaud="bestaudio[abr<160]"

parser = argparse.ArgumentParser(description='supply url compulsroy')


# url to process
# n0amE96UjWk
# ffmpeg fail from jlaw playlist
# https://www.youtube.com/watch?v=mjyPpM9AdXo
# jlaw playlist
# https://www.youtube.com/watch?v=Zr8R4y5QFDo&list=PLUoFIzNiYRRuX0ayTQ31XJX1dS23LAKNt
parser.add_argument('--url', type=str, default="https://www.youtube.com/watch?v=mjyPpM9AdXo",
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
parser.add_argument('--fmat', type=str, default=bestfrmat, help='format in ytdl format')
# output location
# win
# default="Y:\yt2018\%%(uploader_id)s_%%(uploader)s\%%(id)s_%%(title)s_%%(upload_date)s_%%(height)s_%%(abr)s_%%(format_id)s.%%(ext)s"
# linux
# default="/home/durai/shared_yt2018/%(uploader_id)s_%(uploader)s/%(id)s_%(title)s_%(upload_date)s_%(height)s_%(abr)s_%(format_id)s.%(ext)s"
parser.add_argument('--oloc', type=str, default=vmpath, help='output location')
# "/home/durai/shared_yt2018/%(playlist_id)s/%(id)s_%(title)s_%(upload_date)s_%(height)s_%(abr)s_%(format_id)s.%(ext)s"
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

# 3min gateways
# 69.30.240.226:15003
# 69.30.197.122:15003
# 142.54.177.226:15003
# 198.204.228.234:15003
# 69.30.240.226:15004
# 69.30.197.122:15004
# 142.54.177.226:15004
# 198.204.228.234:15004
# 195.154.255.118:15003
# 195.154.222.228:15003
# 195.154.252.58:15003
# 195.154.222.26:15003
# 195.154.255.118:15004
# 195.154.222.228:15004
# 195.154.252.58:15004
# 195.154.222.26:15004


#count number of hits from channle given filters
ydl_opts = {
    # 'simulate': args.sim,
    'forcetitle':args.ttl,
    #'min_views': args.views,
    'outtmpl':args.oloc,
    #'daterange' : DateRange(args.tfrom,args.ttill),
    'writethumbnail':True,
    'writeinfojson':True,
    'format': args.fmat,
    'ignoreerrors':args.i,
    'nooverwrites':args.w,
    'verbose':True,
    #'quiet':args.q,
    # 'nocheckcertificate':True,
    # 'proxy':"5.79.73.131:13080",
    'proxy':"195.154.252.58:15003",
    'sleep_interval':10,
    # 'proxy':"",
    #'logger': MyLogger(),
    #'progress_hooks': [my_hook],
    'noplaylist':False,
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



#count number of hits from channle given filters
ydl_opts = {
    # 'simulate': args.sim,
    'forcetitle':args.ttl,
    #'min_views': args.views,
    'outtmpl':args.oloc,
    #'daterange' : DateRange(args.tfrom,args.ttill),
    'writethumbnail':True,
    'writeinfojson':True,
    'format': args.fmat,
    'ignoreerrors':args.i,
    'nooverwrites':args.w,
    'verbose':True,
    #'quiet':args.q,
    # 'nocheckcertificate':True,
    # 'proxy':"5.79.73.131:13080",
    'proxy':"195.154.252.58:15003",
    'sleep_interval':10,
    # 'proxy':"",
    #'logger': MyLogger(),
    #'progress_hooks': [my_hook],
    'noplaylist':False,
}