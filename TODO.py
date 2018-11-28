FLOW
find videos
    channels
        top down
            list all channels poi
                but first need to make channels work
                    if channels dont work need to rely on scrapebox
                    	go to csv
                        	if scrapebox also does not work use Jdownloader etc
    csv
        scrapebox
            top down
        diigo
            no top down
                do LAST because keeps getting updated or make it so no duplicates    
        google sheets
            no top down
    single url
        hybrid

TODO
	scrapebox
		buy premium proxies and solve custom date range

TODO
	video views&date criteria
		scrapebox
			views not working
				scrape bing by date range AND sort by likes
					then supply this to youtube-dl to downlaod
						scrapbox can crawl fast over date rnage
						same thign  in youtube-dl is serial

		TODO
			how to get video meta data


TODO
	5meta_data.py is the standard for argparse
		copy paste into other sccirpsts





# TODO
# LOGGING 
# VALIDATING
# CLEAN UP
#log video as downloaded completely and in csv
    #check for presence of mp4, m4a, jpg
    #delete jpg and json without 1080 in name
    #log uploader_id,video_id,json_path,video_path,aud_path,thumbanil_path,duraion,quality,upload_date,views,tags

# SOURCES
# diigo csv
#     auto created csv with TAGS
#         RENAME tags to creat folder hierarchy
# scrapebox output
#     manually created csv with KEYWORDS
#         have to then youse youtube-dl to filter videos by views, date etc
#         or use scrapebox to filter by date - crat custom engine
# channels
#     auto named CHANNEL_ID
# custom lists
#     just name custom list

#tagging 
#decided to make hierrarchical folders for tags

#conditional passign of defualt outtmpl whether channel or single video
#use case for how to extract most interesting videos from say cnn or fox

#SOLVED
# to test if channel filter by views works
#minimum functionality of  susccesful wondows bat file replicated



# TODO
# hack to get youtube id by using curl -s?????

# TODO
# argparse  error

# TODO
# scrapebox 
#     first how to get relevant ie views+date content
#         search for hwo to haravest youtube urls by views
# jdownloader can dl entire channle


timecmd.bat python time_print_title.py --url https://www.youtube.com/channel/UCT3v6vL2H5HK4loLMc8pmCw

two command propmts
powercmd
ordinary-cmd
