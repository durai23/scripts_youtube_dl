from __future__ import unicode_literals
import youtube_dl
from youtube_dl.utils import DateRange
import argparse
# import pandas as pd
import os
from datetime import datetime

# bestfmrt="best"
# oldfrmt="bestvideo[ext=mp4][height=1080][height>=720],bestaudio[ext=m4a][abr<192]"
# cygpath="/cygdrive/y/yt2018/%(playlist_id)s_%(playlist_title)s/%(id)s_%(title)s_%(upload_date)s_%(height)s_%(abr)s_%(format_id)s.%(ext)s"
# # need to chagne below paths to remove channel id and uplaoder id
# winpath2="Y:\yt2018\%%(playlist_id)s_%%(playlist_title)s\%%(id)s_%%(title)s_%%(upload_date)s_%%(height)s_%%(abr)s_%%(format_id)s.%%(ext)s"
# winpath="Y:\yt2018\%(playlist_id)s_%(playlist_title)s\%(id)s_%(title)s_%(upload_date)s_%(height)s_%(abr)s_%(format_id)s.%(ext)s"
# winpath_csv="Y:\yt2018\%(playlist_id)s_%(playlist_title)s\%(playlist_id)s_%(playlist_title)s.csv"
# vmpath="/home/durai/shared_yt2018/%(playlist_id)s_%(playlist_title)s/%(id)s_%(title)s_%(upload_date)s_%(height)s_%(abr)s_%(format_id)s.%(ext)s"

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
parser.add_argument('--fmat', type=str, default="best", help='format in ytdl format')
# output location
parser.add_argument('--oloc', type=str, default="", help='output location')
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



ydl_opts = {
    'simulate': args.sim,
    'forcetitle':args.ttl,
    # 'min_views': args.views,
    # 'outtmpl':args.oloc,
    # 'daterange' : DateRange(args.tfrom,args.ttill),
    # 'writethumbnail':True,
    # 'writeinfojson':True,
    # 'format': args.fmat,
    'ignoreerrors':args.i,
    'nooverwrites':args.w,
    'verbose':True,
    # 'quiet':args.q,
    # 'proxy':"195.154.222.26:15003",
    'proxy':"195.154.222.228:15004",
    'sleep_interval':10,
    #'logger': MyLogger(),
    #'progress_hooks': [my_hook],
}

def print_missing_keys(d,cl):
	missing_count=0
	for i in cl:
		# print "##### fetching "+i
		try:
			if i=='protocol':
				# print d['height']
				print str(d[i])
			print i+" = "+str(d[i])
		except:
			print "****** failed "+i+" trying next"
			missing_count+=1
	return missing_count


with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(args.url, download=True)

channel_flag=True
# print info_dict
#view_rate=
try:
        print "$$$$$$$$$$$$$$ it is channel or playlist with "+str(len(info_dict['entries']))+" videos"
except KeyError:
        print "$$$$$$$$$$$$$$ it is SINGLE video"
        channel_flag=False

cols=['upload_date', 'protocol', 'extractor', 'chapters', 'height', 'quality', 'playlist_index', 'view_count', 'playlist', 'title', 'dislike_count', 'playlist_id', 'uploader_url', 'subtitles', 'season_number', 'annotations', 'filesize', 'display_id', 'automatic_captions', 'format', 'requested_subtitles', 'start_time', 'tbr', 'downloader_options', 'uploader', 'uploader_id', 'categories', 'thumbnails', 'artist', 'extractor_key', 'vcodec', 'channel_id', 'is_live', 'end_time', 'webpage_url', 'playlist_uploader_id', 'acodec', 'n_entries', 'age_limit', 'creator', 'series', 'format_note', 'like_count', 'duration', 'id', 'average_rating', 'fps', 'channel_url', 'thumbnail', 'webpage_url_basename', 'description', 'tags', 'track', 'playlist_uploader', 'format_id', 'episode_number', 'playlist_title', 'license', 'alt_title', 'url', 'http_headers', 'player_url', 'ext', 'width']
cols_with_formats=['upload_date', 'protocol', 'extractor', 'chapters', 'height', 'quality', 'playlist_index', 'view_count', 'playlist', 'title', 'dislike_count', 'playlist_id', 'uploader_url', 'subtitles', 'season_number', 'annotations', 'filesize', 'display_id', 'automatic_captions', 'format', 'requested_subtitles', 'start_time', 'tbr', 'downloader_options', 'uploader', 'uploader_id', 'categories', 'thumbnails', 'artist', 'extractor_key', 'vcodec', 'channel_id', 'is_live', 'end_time', 'webpage_url', 'formats', 'playlist_uploader_id', 'acodec', 'n_entries', 'age_limit', 'creator', 'series', 'format_note', 'like_count', 'duration', 'id', 'average_rating', 'fps', 'channel_url', 'thumbnail', 'webpage_url_basename', 'description', 'tags', 'track', 'playlist_uploader', 'format_id', 'episode_number', 'playlist_title', 'license', 'alt_title', 'url', 'http_headers', 'player_url', 'ext', 'width']

#compute views/day metric
if channel_flag:
    # print "it is CHANNEL"
    # out_csv=os.path.join("C:",os.sep,"cygwin64","home","synapse","channel_selection_by_vpd.csv")

	for j in range(len(info_dict['entries'])):
		print "keys missing = "+str(print_missing_keys(info_dict['entries'][j],cols))+ " out of "+str(len(cols))+" keys"

	# print info_dict['entries'][j]
else:
	print "keys missing = "+str(print_missing_keys(info_dict,cols))+ " out of "+str(len(cols))+" keys"
	print "&&&&&&&&&&&&&&& printing contents of info dict"
	# print info_dict
	# for key, value in info_dict.items():
	# 	print (key, value)
	




#elif args.vpd_only:
#        print_title_vpd(info_dict)
#else:
#        # print_title_vpd(info_dict)
#        print_title_vpd(info_dict)
#        # add_to_df(info_dict,vpd_threshold)




	