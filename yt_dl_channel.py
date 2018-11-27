from __future__ import unicode_literals
import youtube_dl
import argparse

f_separate="bestvideo[ext=mp4][height=1080][height>=720],bestaudio[ext=m4a][abr<192]"
#otmpl="F:\yt2018\%%(uploader)s_%%(uploader_id)s\%%(channel)s_%%(channel_id)s\%%(id)s_%%(title)s_%%(upload_date)s_%%(height)s_%%(abr)s_%%(format_id)s.%%(ext)s"
otmpl="F:\yt2018\%(uploader)s_%(uploader_id)s\%(channel)s_%(channel_id)s\%(id)s_%(title)s_%(upload_date)s_%(height)s_%(abr)s_%(format_id)s.%(ext)s"
# Instantiate the parser
parser = argparse.ArgumentParser(description='Optional app description')

# url to process
parser.add_argument('--url', type=str, required=True, help='A required url argument')

# output template 
#parser.add_argument('--otmpl', type=str, required=True,
#                    help='output template')

## format specs
#parser.add_argument('--fspec', type=str, required=True,
#                    help='format specs')

# Switch
#parser.add_argument('--switch', action='store_true', help='A boolean switch')

args = parser.parse_args()

print("Video url:")
print(args.url)
#print(args.views)
#print(args.trange)
#print(args.switch)

#count number of hits from channle given filters

ydl_opts = {
    'format': f_separate,
    'outtmpl': otmpl,
    'writethumbnail':True,
    'writeinfojson':True,
    'nooverwrites':True,
    'ignoreerrors':True,
    #'progress_hooks': [my_hook],
    #'daterange': args.trange,
    #'simulate': True,
    'forcetitle':True,
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
