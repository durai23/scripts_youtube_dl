from __future__ import unicode_literals
import youtube_dl
from youtube_dl.utils import DateRange

ydl_opts = {
    'daterange' : DateRange('20150730','20150802'),
    #'daterange' : DateRange('20150730','20150802'),
    'simulate':True,
    'verbose':True,
    'forcetitle':True,

}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['MqpVnYrNnf0'])