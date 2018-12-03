# FLOW
SOLVED
views_channel_filter is teh defualt for argparse block

***************************************************************************************************************************************
12/2

TODONOW
	solve custom date range 
		use FOOTPRINT
			set search large number of results and adjust settings so no bounce

	set yt to make speardsheet out of bbcnews

	which IP to add to storm proxies - imenb or fzj wingate? LATTER OBV
		get settings from control panel


youtube list SOURCES
	diigo
		list
			SOLVED
	list
		SOLVED
	celebrity
		scrapebox
			list
				SOLVED
		youtube channels hopping
			sort by most viewd pick random celebs
				diigo
					FAST
						SOLVED

	channel harvesting
		ytd with proxy
			NOT POSSIBLE FOR CNN, FOX etc taking days
				switch to scrapebox FOOTPRINT
					solved
			POSSIBLE
				trevor - test with vpd = 5000
					https://www.youtube.com/channel/UCwWhs_6x42TyRM4Wstoq8HA
				colbert - test with vpd = 4000
					https://www.youtube.com/channel/UCMtFAi84ehTSYSE9XoHefig



		scrapebox without custom date range
			not satisfcatory
		scrapebox with date range
			TODO


HTML
	# ,"viewCount":"$VIEWCOUNT"
	look for above term and you get viewcount from html
FOOTPRINT
	site:youtube.com "Unsubscribe from CNN?"

***************************************************************************************************************************************
# TODO
# 	buy premium proxies and solve custom date range

TODO
	video views&date criteria
		scrapebox
			views not working
				scrape bing by date range AND sort by likes
					then supply this to youtube-dl to downlaod
						scrapbox can crawl fast over date rnage
						same thign  in youtube-dl is serial
		youtube-dl
			trying to parse dict and compute view/day
				done
					validated using channel with 10 vids
					https://www.youtube.com/channel/UCzkLUqHN9Ov0fwbh2QF0sGQ
							took 14 seconds
								calculates accurately
									but does it differ from popularitu

		eg of high view video
			https://www.youtube.com/watch?v=uGxr1VQ2dPI
				56560 vpd


		TODO
			how to get video meta data


TODO
	5meta_data.py is the standard for argparse
		copy paste into other sccirpsts


Get 5% OFF Monthly Discount Code "5OFFSTORM"
HOME
ROTATING PROXIES 
DEDICATED PROXIES 
COMPARE PACKAGES
LOGIN


# Combine two DataFrame objects with identical columns.

# >>> df1 = pd.DataFrame([['a', 1], ['b', 2]],
# ...                    columns=['letter', 'number'])
# >>> df1
#   letter  number
# 0      a       1
# 1      b       2
# >>> df2 = pd.DataFrame([['c', 3], ['d', 4]],
# ...                    columns=['letter', 'number'])
# >>> df2
#   letter  number
# 0      c       3
# 1      d       4
# >>> pd.concat([df1, df2])
#   letter  number
# 0      a       1
# 1      b       2
# 0      c       3
# 1      d       4
# Combine DataFrame objects with overlapping columns and return everything. Columns outside the intersection will be filled with NaN values.

# >>> df3 = pd.DataFrame([['c', 3, 'cat'], ['d', 4, 'dog']],
# ...                    columns=['letter', 'number', 'animal'])
# >>> df3
#   letter  number animal
# 0      c       3    cat
# 1      d       4    dog
# >>> pd.concat([df1, df3])
#   animal letter  number
# 0    NaN      a       1
# 1    NaN      b       2
# 0    cat      c       3
# 1    dog      d       4


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
			# write code to convert csv to ist of IDS and output template by tag
# scrapebox output
#     manually created csv with KEYWORDS
#         have to then youse youtube-dl to filter videos by views, date etc
#         or use scrapebox to filter by date - crat custom engine
# channels
#     auto named CHANNEL_ID

# custom lists
#     just name custom list
		  code to convert to IDs

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
