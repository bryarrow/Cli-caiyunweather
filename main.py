import urllib.request as urlreq
import json5

weatherUrl = ['https://api.caiyunapp.com/v2.5/']
weatherjson = [{},{},{},{},{},{},{},{},{}]
haveUnitExcept = False
UnitExcept = []


def getlocation(jsonobject):#按参数jsonobject中指定方式获取经纬度
	#TODO：读取csv定位、输入经纬度、使用设备定位

	# try:
	# 	if(jsonobject['locationmode'] == 'city'):
			
	# except KeyError:
	# 	print('请检查settings.json是否正确（可前往Github repo下载默认值）')
	# 	exit(-1)

	return '119.166485,36.654448'#待todo完成后会返回定位的经纬度，现在这个是山东省潍坊市坊子区的位置

def settingload() :#读取settings.json并创建请求URL组
	global weatherUrl
	global haveUnitExcept
	global UnitExcept

	#文件读取
	setfile = open('.\\settings.json',mode='r',encoding='utf-8')
	setjson = json5.loads(setfile.read())

	try:
		token = setjson['token']
		location = getlocation(setjson)
		unit = setjson['unit']
		unitexcept = setjson['unitexcept']
	except KeyError:
		print('请检查settings.json是否正确（可前往Github repo下载默认值）')
		exit(-1)

	if unitexcept != {} :
		weatherUrl[0] = weatherUrl[0]+token+'/'+location+'/weather.json?unit='+unit
		haveUnitExcept = True
		if 'SI' in unitexcept.values():
			weatherUrl.append('https://api.caiyunapp.com/v2.5/'+token+'/'+location+'/weather.json?unit=SI')
		if 'imperial' in unitexcept.values() :
			weatherUrl.append('https://api.caiyunapp.com/v2.5/'+token+'/'+location+'/weather.json?unit=imperial')
		if 'metric:v1' in unitexcept.values() :
			weatherUrl.append('https://api.caiyunapp.com/v2.5/'+token+'/'+location+'/weather.json?unit=metric:v1')
		if 'metric:v2' in unitexcept.values() :
			weatherUrl.append('https://api.caiyunapp.com/v2.5/'+token+'/'+location+'/weather.json?unit=metric:v2')
		if 'default metric' in unitexcept.values() :
			weatherUrl.append('https://api.caiyunapp.com/v2.5/'+token+'/'+location+'/weather.json')

	else:
		if unit == 'default metric' :
			weatherUrl[0] = weatherUrl[0]+token+'/'+location+'/weather.json'
		else:
			weatherUrl[0] = weatherUrl[0]+token+'/'+location+'/weather.json?unit='+unit

	setfile.close()


def getWeather():#请求天气信息
	global weatherjson

	settingload()

	i=0
	for thisURL in weatherUrl:
		weatherUrlRespond = urlreq.urlopen(thisURL)
		weatherjson[i]= json5.loads(weatherUrlRespond.read())
		i+=1
	del(i)

def typer() :#TODO 获取信息并对获取的信息进行格式化
	getWeather()
	
	res = ''
	
	#return res
	return weatherjson

#######################################################################################


#判断是否成功获取天气并输出 TODO：在这里判断是否成功并不合理，待重构
# if (weatherjson['status'] == 'ok') :   
# 	print(typer())
# else:
# 	print("ERROR!\n"+weatherjson['error'])