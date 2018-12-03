from __future__ import unicode_literals
import youtube_dl
from youtube_dl.utils import DateRange
import argparse
import pandas as pd
import os
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
parser.add_argument('--oloc', type=str, default="F:\yt2018\%%(uploader_id)s_%%(uploader)s\%%(id)s_%%(title)s_%%(upload_date)s_%%(height)s_%%(abr)s_%%(format_id)s.%%(ext)s",
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
# verbose
parser.add_argument('--v', type=bool, default=False,
                    help='bool do not overwrite')
# quiet
parser.add_argument('--q', type=bool, default=False, help='bool do not overwrite')
# thumbnail
parser.add_argument('--thumb', type=bool, default=False,
                    help='bool thumbnail')
# json
parser.add_argument('--meta', type=bool, default=False,
                    help='bool json')
# only calc vpd
parser.add_argument('--vpd_only', type=bool, default=False,
                    help='bool json')
# set vpd
parser.add_argument('--vpd', type=int, default=1,
                    help='bool json')
# use proxy
parser.add_argument('--prx', type=str, default="5.79.73.131:13080",
                    help='bool json')


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
print("quiet:")
print(args.q)
print("bool thumbnail:")
print(args.thumb)
print("bool metadata:")
print(args.meta)
print("str proxy:")
print(args.prx)
print("verbose:")
print(args.v)


ydl_opts = {
    'simulate': args.sim,
    # 'forcetitle':args.ttl,
    # 'min_views': args.views,
    # 'outtmpl':args.oloc,
    # 'daterange' : DateRange(args.tfrom,args.ttill),
    # 'writethumbnail':args.thumb,
    # 'writeinfojson':args.meta,
    # 'format': args.fmat,
    # 'ignoreerrors':args.i,
    # 'nooverwrites':args.w,
    'verbose':args.v,
    # 'quiet':args.q,
    #'proxy':args.prx
    #'logger': MyLogger(),
    #'progress_hooks': [my_hook],
}


def print_title_vpd(d):
	print "Title -"+d['title']
	print "Views per day = "+str(views_per_day(d['view_count'],d['upload_date']))

# compute date tiem metric
def views_per_day(vws,udt):
	ytd_date_format='%Y%m%d'
	udt=datetime.strptime(udt,ytd_date_format)
	days_since_upload=(datetime.today()-udt).days
	return vws/days_since_upload

def add_to_df(d,v):
	cols=['upload_date','extractor','height','playlist_index','view_count','playlist','title','dislike_count','width','uploader_url','acodec','display_id','format','uploader','uploader_id','categories','extractor_key','vcodec','channel_id','webpage_url','abr','fps','channel_url','thumbnail','webpage_url_basename','tags','format_id','ext']
	rw=[]
	rw_ind=0
	# construct row
	if int(d['view_count'])>v:
		for i in cols:
			rw.append(d[i])
	
	df1=pd.DataFrame([rw],columns=cols)
	# print "for video "+str(d['title'])
	return df1
	

# based on https://www.youtube.com/watch?v=NnW5EjwtE2U
vpd_threshold=args.vpd


# ydl_opts = {
#     #'daterange' : DateRange('20150730','20150802'),
#     #'daterange' : DateRange('20150730','20150802'),
#     'simulate':True,
#     #'verbose':True,
#     'forcetitle':True,
# }

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(args.url, download=False) 
    #ydl.download(['MqpVnYrNnf0'])

channel_flag=True

#view_rate=
try:
	print len(info_dict['entries'])
except KeyError:
	#print "it is SINGLE video"
	channel_flag=False

#compute views/day metric
if channel_flag:
	print "it is CHANNEL"
	#out_csv=os.path.join("C:",os.sep,"cygwin64","home","synapse","channel_selection_by_vpd.csv")
	out_csv="/home/durai/shared_scripts_youtube_dl/channel_selection_by_vpd.csv"
	# cycle through entries
	cols=['upload_date','extractor','height','playlist_index','view_count','playlist','title','dislike_count','width','uploader_url','acodec','display_id','format','uploader','uploader_id','categories','extractor_key','vcodec','channel_id','webpage_url','abr','fps','channel_url','thumbnail','webpage_url_basename','tags','format_id','ext']
	df=pd.DataFrame(columns=cols)
	for i in info_dict['entries']:
#		if print_title_vpd(i)>vpn_threshold:
		df=df.append(add_to_df(i,vpd_threshold),ignore_index=True)
	df.to_csv(out_csv)
elif args.vpd_only:
	print_title_vpd(info_dict)
else:
	# print_title_vpd(info_dict)
	print_title_vpd(info_dict)
	# add_to_df(info_dict,vpd_threshold)
	

# if not channel_flag:
# 	print "it is SINGLE"



	