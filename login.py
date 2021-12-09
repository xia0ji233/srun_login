import requests
import time
import re
from urllib.parse import quote
from encryption.srun_md5 import *
from encryption.srun_sha1 import *
from encryption.srun_base64 import *
from encryption.srun_xencode import *
header={
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36'
}
init_url="http://10.110.74.91"
get_challenge_api="http://10.110.74.91/cgi-bin/get_challenge"

srun_portal_api="http://10.110.74.91/cgi-bin/srun_portal"
n = '200'
type = '1'
ac_id='4'
enc = "srun_bx1"
def get_chksum():
	chkstr = token+username
	chkstr += token+hmd5
	chkstr += token+ac_id
	chkstr += token+ip
	chkstr += token+n
	chkstr += token+type
	chkstr += token+i
	return chkstr
def get_info():
	info_temp={
		"username":username,
		"password":password,
		"ip":ip,
		"acid":ac_id,
		"enc_ver":enc
	}
	i=re.sub("'",'"',str(info_temp))
	i=re.sub(" ",'',i)
	return i
def init_getip():
	global ip
	init_res=requests.get(init_url,headers=header)
	ip=re.search('ip     : "(.*?)"',init_res.text).group(1)
	print("ip:",ip)
def get_token():
	# print("获取token")
	global token
	get_challenge_params={
		"callback": "jQuery112406608265734960486_"+str(int(time.time()*1000)),
		"username":username,
		"ip":ip,
		"_":int(time.time()*1000),
	}
	get_challenge_res=requests.get(get_challenge_api,params=get_challenge_params,headers=header)
	token=re.search('"challenge":"(.*?)"',get_challenge_res.text).group(1)
	print("token:"+token)
def do_complex_work():
	global i,hmd5,chksum
	i=get_info()
	i="{SRBX1}"+get_base64(get_xencode(i,token))
	hmd5=get_md5(password,token)
	chksum=get_sha1(get_chksum())
	print("encode done!")
def login():
	srun_portal_params={
	'callback': 'jQuery11240645308969735664_'+str(int(time.time()*1000)),
	'action':'login',
	'username':username,
	'password':'{MD5}'+hmd5,
	'ac_id':ac_id,
	'ip':ip,
	'chksum':chksum,
	'info':i,
	'n':n,
	'type':type,
	'os':'windows+10',
	'name':'windows',
	'double_stack':0,
	'_':int(time.time()*1000)
	}
	#print(srun_portal_params)
	srun_portal_res=requests.get(srun_portal_api,params=srun_portal_params,headers=header)

	if 'ok' in srun_portal_res.text:
		print('登陆成功')
	else:
		error_msg=eval(re.search('\((.*?)\)',srun_portal_res.text).group(1))
		#输出错误信息
		print('error_type:'+error_msg['error'])
		print(error_msg['error_msg'])


if __name__ == '__main__':
	global username,password
	username=""#一卡通号加上@运营商地址
	password=""#密码
	init_getip()
	get_token()
	do_complex_work()
	login()
