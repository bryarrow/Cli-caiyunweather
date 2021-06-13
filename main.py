import urllib.request as urlreq
import json

weatherurl = ''

def getlocation(jsonobject):
	# try:
	# 	if(jsonobject['locationmode'] == 'city'):
			
	# except KeyError:
	# 	print('请检查settings.json是否正确（可前往Github repo下载默认值）')
	return '119.166485,36.654448'

def settingload() :
	setfile = open('.\\settings.json',mode='r')
	setjson = json.loads(setfile.read())
	try:
		token = setjson['token']
		location = getlocation(setjson)
	except KeyError:
		print('请检查settings.json是否正确（可前往Github repo下载默认值）')




weatherjson = urlreq.urlopen(weatherurl)

weather = json.loads(weatherjson.read())

def typer() :
	res = ''
	
	return res


if (weather['status'] == 'ok') :   
	print(typer())
else:
	print("ERROR!\n"+weather['error'])