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
parser.add_argument('--url', type=str, required=True,
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
# quiet
parser.add_argument('--q', type=bool, default=False, help='bool do not overwrite')
# thumbnail
parser.add_argument('--thumb', type=bool, default=False,
                    help='bool thumbnail')
# json
parser.add_argument('--meta', type=bool, default=False,
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


def print_title_vpd(d):
	print "Title -"+d['title']
	print "Views per day -"+str(views_per_day(d['view_count'],d['upload_date']))

# compute date tiem metric
def views_per_day(vws,udt):
	ytd_date_format='%Y%m%d'
	udt=datetime.strptime(udt,ytd_date_format)
	days_since_upload=(datetime.today()-udt).days
	return vws/days_since_upload



ydl_opts = {
    #'daterange' : DateRange('20150730','20150802'),
    #'daterange' : DateRange('20150730','20150802'),
    'simulate':True,
    #'verbose':True,
    'forcetitle':True,

}
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
	# cycle through entries
	for i in info_dict['entries']:
		print_title_vpd(i)
else:
	print_title_vpd(info_dict)

# if not channel_flag:
# 	print "it is SINGLE"



	