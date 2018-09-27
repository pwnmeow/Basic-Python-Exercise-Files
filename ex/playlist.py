playlist = {
	'song':[
		{'songName':"song1",'singer':"ss",'duration':5.6},
		{'songName':"song2",'singer':"ss",'duration':5.6},
		{'songName':"song3",'singer':"ss",'duration':5.6},
		{'songName':"song4",'singer':"ss",'duration':5.6},
		{'songName':"song5",'singer':"ss",'duration':5.6}
		],
	'author':"colt",
	'title':"bus ride"
}
total = 0
for song in playlist['song']:
	total += song['duration']
print(total)