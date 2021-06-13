import urllib.request as urlreq
import json

weatherUrl = ''
weatherjson = {}


def getlocation(jsonobject):#按参数jsonobject中指定方式获取经纬度
	#TODO：读取csv定位、输入经纬度、使用设备定位

	# try:
	# 	if(jsonobject['locationmode'] == 'city'):
			
	# except KeyError:
	# 	print('请检查settings.json是否正确（可前往Github repo下载默认值）')

	return '119.166485,36.654448'#待todo完成后会返回定位的经纬度，现在这个是山东省潍坊市坊子区的位置

def settingload() :#读取settings.json并拼接请求URL
	#文件读取
	setfile = open('.\\settings.json',mode='r')
	setjson = json.loads(setfile.read())

	try:
		token = setjson['token']
		location = getlocation(setjson)
		unit = setjson['unit']
		unitexcept = setjson['unitexcept']
	except KeyError:
		print('请检查settings.json是否正确（可前往Github repo下载默认值）')

	



def getWeather():#请求天气信息
	global weatherjson
	weatherUrlRespond = urlreq.urlopen(weatherUrl)
	weatherjson= json.loads(weatherUrlRespond.read())

def typer() :#对获取的信息进行格式化
	res = ''
	
	return weatherjson

#######################################################################################


#判断是否成功获取天气并输出 TODO：在这里判断是否成功并不合理，待重构
if (weatherjson['status'] == 'ok') :   
	print(typer())
else:
	print("ERROR!\n"+weatherjson['error'])