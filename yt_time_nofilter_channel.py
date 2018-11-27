from __future__ import unicode_literals
import youtube_dl
import argparse

# Instantiate the parser
parser = argparse.ArgumentParser(description='supply url compulsroy')

# url to process
parser.add_argument('--url', type=str, required=True,
                    help='A required url argument')

# number of views
parser.add_argument('--views', type=int, default=1,
                    help='number of views')


# date range
#parser.add_argument('--trange', type=str, required=True,
#                    help='date range in ytdl format')

# Switch
#parser.add_argument('--switch', action='store_true', help='A boolean switch')

args = parser.parse_args()

print("Video url:")
print(args.url)
print(args.views)
#print(args.trange)
#print(args.switch)

#count number of hits from channle given filters

ydl_opts = {
    #'format': 'bestaudio/best',
    #'logger': MyLogger(),
    #'progress_hooks': [my_hook],
    #'min_view': args.views,
    #'daterange': args.trange,
    'simulate': True,
    'ignoreerrors':True,
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
