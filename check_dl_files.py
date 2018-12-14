import glob
import os
import re


# def check_dl_files(plid):
# 	#check wheher file with id or playlist_id exists
dl_folder=os.path.join("M:",os.sep,"yt2018")
# 	dl_folder_wildcard=os.path.join(dl_folder,"*",plid,"*")
# 	# print glob.glob(dl_folder+'*'+plid+'*')
# 	if 0<len(glob.glob(dl_folder+'\\'+plid+'*.jpg'))<=1:
# 		jpg_flag=True
#     if 0<len(glob.glob(dl_folder+'\\'+plid+'*.mp4'))<=1:
#     elif 0<len(glob.glob(dl_folder+'\\'+plid+'*.webm'))<=1:
#      and \
# 	   0<len(glob.glob(dl_folder+'\\'+plid+'*.jpg'))<=1




idd='4URfrF5_avE'
plid='PLUoFIzNiYRRsA2CTRYhTHKnlcFeGyTcuQ'
thumbb='4URfrF5_avE_Robert De Niro Has a Pretty Big Boat_PLUoFIzNiYRRsA2CTRYhTHKnlcFeGyTcuQ_Deniro_20160823_1080_NA_137.jpg'
metaa="4URfrF5_avE_Robert De Niro Has a Pretty Big Boat_PLUoFIzNiYRRsA2CTRYhTHKnlcFeGyTcuQ_Deniro_20160823_1080_NA_137.info.json"
vidd="4URfrF5_avE_Robert De Niro Has a Pretty Big Boat_PLUoFIzNiYRRsA2CTRYhTHKnlcFeGyTcuQ_Deniro_20160823_1080_NA_137.mp4"
audd="4URfrF5_avE_Robert De Niro Has a Pretty Big Boat_PLUoFIzNiYRRsA2CTRYhTHKnlcFeGyTcuQ_Deniro_20160823_NA_128_140.m4a"

updt=r'\d{8}'
viddrgx=idd+r'.*'+plid+r'.*'+updt+r'_\d{3,4}_NA_.*[^(g|n)]$'
auddrgx=idd+r'.*'+plid+r'.*'+updt+r'_NA_\d{2,3}_'
thumbbrgx=idd+r'.*'+plid+r'.*'+updt+r'_\d{3,4}_NA_.*jpg$'
metaargx=idd+r'.*'+plid+r'.*'+updt+r'_\d{3,4}_NA_.*json$'
fmtcd=r'\d{2,3}'

jpg_regex = re.escape(idd)+r'_.*_'+re.escape(plid)+r'_.*_'+updt+'_NA_\d*.jpg'
jpg_regex1 = r'^'+idd+r'jpg$'
# print re.search(viddrgx,vidd).group()
# if re.search(auddrgx,audd):
# 	print "audio downloaded success"	
# if re.search(thumbbrgx,thumbb):
# 	print "thumb downloaded success"
if re.search(viddrgx,thumbb):
	print "thumb downloaded success"
# print re.match(jpg_regex1,thumbb).group()
for k in viddrgx,auddrgx,thumbbrgx,metaargx:
    res = [f for f in os.listdir(dl_folder) if re.search(k, f)]
    print str(len(res))+' for '+res[0]

# res = [f for f in os.listdir(dl_folder) if re.search(auddrgx, f)]
# print type(res)
# print res
# for f in res:
#     print f
