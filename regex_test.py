import re
import glob
import os


dl_folder='/home/arasan/imenb/regex_test'

plid='PLUoFIzNiYRRu_ekJTBxcNi8tH_IRibsnd'
idd='8FTDWY8SIX0'
updt='20170515'

fpassno=0

viddrgx=idd+r'.*'+updt+r'_\d{3,4}_NA_.*[^(g|n)]$'
# auddrgx=idd+r'.*'+plid+r'.*'+updt+r'_NA_\d{2,3}_'
auddrgx=idd+r'.*'+'_ytd2018audioeggplantcapsicumvelacheryundhiu'
thumbbrgx=idd+r'.*'+updt+r'_\d{3,4}_NA_.*jpg$'
metaargx=idd+r'.*'+updt+r'_\d{3,4}_NA_.*json$'

for k in viddrgx,auddrgx,thumbbrgx,metaargx:
	res = [f for f in os.listdir(dl_folder) if re.search(k, f)]
    # for f in os.listdir(dl_folder):
    	# res=re.search(k,f)
	if 0<len(res)<=1:
		fpassno+=1
		print "success for  "+str(k)
    
if fpassno==4:
    print "all 4 dled" 
else:
    print "FAIL"