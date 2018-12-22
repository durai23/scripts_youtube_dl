# MAKE WITH PROXY VERION
# THIS ONE HAS NO PROXY DUE TO FSL
from __future__ import unicode_literals
import youtube_dl
# from youtube_dl.utils import DateRange
import argparse
import pandas as pd
import os
import re
import glob
# from datetime import datetime
# Instantiate the parser

#CHANGE to eagate backup
synapse_path="/cygdrive/m/yt2018/%(id)s_%(title)s_%(playlist_id)s_%(playlist_title)s_%(upload_date)s_%(height)s_%(abr)s_%(format_id)s.%(ext)s"
cygpath="/cygdrive/y/yt2018/%(playlist_id)s_%(playlist_title)s/%(id)s_%(title)s_%(upload_date)s_%(height)s_%(abr)s_%(format_id)s.%(ext)s"
# need to chagne below paths to remove channel id and uplaoder id
winpath2="Y:\yt2018\%%(playlist_id)s_%%(playlist_title)s\%%(id)s_%%(title)s_%%(upload_date)s_%%(height)s_%%(abr)s_%%(format_id)s.%%(ext)s"
winpath="M:\yt2018\%(id)s_%(title)s_%(playlist_id)s_%(playlist_title)s_%(upload_date)s_%(height)s_%(abr)s_%(format_id)s.%(ext)s"
vmpath="/home/durai/shared_yt2018/%(playlist_id)s_%(playlist_title)s/%(id)s_%(title)s_%(upload_date)s_%(height)s_%(abr)s_%(format_id)s.%(ext)s"


origfrmat="bestvideo[ext=mp4][height=1080][height>=720],bestaudio[ext=m4a][abr<192]"
bestfrmat="best"
bestfrmat2="bestvideo[ext=mp4][height=1080][height>=720],bestaudio[ext=m4a][abr<192]"
defrmat2="best[ext=mp4][height<=1080][height>=720]"
defrmat="best[ext=mp4][height<=1080][height>=720]"
wrstfrmat="worstvideo[ext=mp4][height=1080][height>=720],worstaudio[ext=m4a][abr<192]"
#add ext =mp4 if needed
bestvid="bestvideo[height<=1080]"
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

# 3min gateways OLD
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

# 3min gateways NEW

# 195.154.255.118:15003
# 195.154.222.228:15003
# 195.154.252.58:15003
# 195.154.222.26:15003
# 195.154.255.118:15004
# 195.154.222.228:15004
# 195.154.252.58:15004
# 195.154.222.26:15004

# increase sleep and remove proxy 12/10
ydl_opts = {
    # 'simulate': args.sim,
    'forcetitle':True,
    #'min_views': args.views,
    'outtmpl':winpath,
    #'daterange' : DateRange(args.tfrom,args.ttill),
    # 'writethumbnail':False,
    # 'writeinfojson':False,
    'format': bestaud,
    'ignoreerrors':True,
    'nooverwrites':True,
    'verbose':True,
    #'quiet':args.q,
    # 'nocheckcertificate':True,
    'proxy':"",#195.154.255.118:15004",
    'sleep_interval':10,
    # 'proxy':"",
    #'logger': MyLogger(),
    #'progress_hooks': [my_hook],
    #'noplaylist':False,
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

ydl_opts = {
    # 'simulate': args.sim,
    'forcetitle':True,
    #'min_views': args.views,
    'outtmpl':winpath,
    #'daterange' : DateRange(args.tfrom,args.ttill),
    'writethumbnail':True,
    'writeinfojson':True,
    'format': bestvid,
    'ignoreerrors':True,
    'nooverwrites':True,
    'verbose':True,
    #'quiet':args.q,
    # 'nocheckcertificate':True,
    # 'proxy':"5.79.73.131:13080",
    'proxy':"",#195.154.252.58:15004",
    'sleep_interval':10,
    # 'proxy':"",
    #'logger': MyLogger(),
    #'progress_hooks': [my_hook],
    #'noplaylist':False,
}

def check_dl_files(idd,plid):
    updt=r'\d{8}'
    viddrgx=idd+r'.*'+plid+r'.*'+updt+r'_\d{3,4}_NA_.*[^(g|n)]$'
    auddrgx=idd+r'.*'+plid+r'.*'+updt+r'_NA_\d{2,3}_'
    thumbbrgx=idd+r'.*'+plid+r'.*'+updt+r'_\d{3,4}_NA_.*jpg$'
    metaargx=idd+r'.*'+plid+r'.*'+updt+r'_\d{3,4}_NA_.*json$'
    dl_folder=os.path.join("M:",os.sep,"yt2018")
    fpassno=0
    for k in viddrgx,auddrgx,thumbbrgx,metaargx:
        res = [f for f in os.listdir(dl_folder) if re.search(k, f)]
        if 0<len(res)<=1:
            fpassno+=1
    if fpassno==4:
        return True
    else:
        return False


def add_to_df(d,cl,cll):
        rw=[]
        try:
            print "addding row for video "+str(d['id'])
        except:
            print "bad dict - will enter None" #or NaN is better
        #rw_ind=0
        # construct row
        #if int(d['view_count'])>v:
        # cll=list(cl)
        # cl.remove('allfourdled')

        for i in cll:
            try:
                rw.append(d[i])
            except:
                rw.append('None')
        try:
            if check_dl_files(d['id'],d['playlist_id']):
                rw.append('T')
            else:
                rw.append('F')
        except:
            rw.append('F')

        df1=pd.DataFrame([rw],columns=cl)
        # print "for video "+str(d['title'])
        return df1

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(args.url, download=True)

channel_flag=True

try:
        print "it is channel or playlist with "+str(len(info_dict['entries']))+" videos"
except KeyError:
        #print "it is SINGLE video"
        channel_flag=False

#compute views/day metric
if channel_flag:
    # out_csv=os.path.join("C:",os.sep,"cygwin64","home","synapse","channel_selection_by_vpd.csv")
    # out_csv=os.path.join("M:",os.sep,"yt2018",str(pl_id)+".csv")
    for j in range(len(info_dict['entries'])):
        try:
            pl_id=info_dict['entries'][j]['playlist_id']
            # vid_id=info_dict['entries'][j]['id']
            print "$$$$$$$$$$$$$$$$  playlist id = "+str(pl_id)+" SUCCESSSS $$$$$$$$$$$$"
            break
        except:
            print "$$$$$$$$$$$$$$$$ FAIL  trying next entry" #"+info_dict['entries'][j]['id']+"
    out_csv=os.path.join("M:",os.sep,"yt2018",str(pl_id)+".csv")
    # check_dl_files(pl_id)
    # "/cygdrive/m/yt2018/%(playlist_id)s_%(playlist_title)s.csv"
    #out_csv=os.path.join("C:",os.sep,"cygwin64","home","synapse","playist_test.csv")
    # out_csv=winpath_csv
    #out_csv="/home/durai/shared_scripts_youtube_dl/channel_selection_by_vpd.csv"
    # cycle through entries
    cols=['upload_date', 'extractor', 'height', 'playlist_index', 'view_count', 'playlist', 'title', 'dislike_count', 'playlist_id', 'uploader_url', 'display_id', 'format', 'start_time', 'uploader', 'uploader_id', 'categories', 'artist', 'extractor_key', 'vcodec', 'channel_id', 'end_time', 'webpage_url', 'playlist_uploader_id', 'acodec', 'n_entries', 'age_limit', 'creator', 'like_count', 'duration', 'id', 'average_rating', 'fps', 'channel_url', 'thumbnail', 'webpage_url_basename', 'description', 'tags', 'track', 'playlist_uploader', 'format_id','playlist_title', 'license', 'ext', 'width', 'allfourdled']
    cols_sans_allfourdled=['upload_date', 'extractor', 'height', 'playlist_index', 'view_count', 'playlist', 'title', 'dislike_count', 'playlist_id', 'uploader_url', 'display_id', 'format', 'start_time', 'uploader', 'uploader_id', 'categories', 'artist', 'extractor_key', 'vcodec', 'channel_id', 'end_time', 'webpage_url', 'playlist_uploader_id', 'acodec', 'n_entries', 'age_limit', 'creator', 'like_count', 'duration', 'id', 'average_rating', 'fps', 'channel_url', 'thumbnail', 'webpage_url_basename', 'description', 'tags', 'track', 'playlist_uploader', 'format_id','playlist_title', 'license', 'ext', 'width']
#        cols=['upload_date','extractor','height','playlist_index','view_count','playlist','title','dislike_count','width','uploader_url','acodec','display_id','format','uploader','uploader_id','categories','extractor_key','vcodec','channel_id','webpage_url','channel_url','thumbnail','webpage_url_basename','tags','format_id','ext','id']
    df=pd.DataFrame(columns=cols)
    for i in info_dict['entries']:
#               if print_title_vpd(i)>vpn_threshold:
            df=df.append(add_to_df(i,cols,cols_sans_allfourdled),ignore_index=True)
    df.to_csv(out_csv, encoding='utf-8')
else:
    print "not channel EXITING"
#elif args.vpd_only:
#        print_title_vpd(info_dict)
#else:
#        # print_title_vpd(info_dict)
#        print_title_vpd(info_dict)
#        # add_to_df(info_dict,vpd_threshold)
