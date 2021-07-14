import requests
import re
def try_request(url):
	headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
	}
	r = requests.get(url=url,headers=headers)
	if(r.status_code ==200):
		print_data(r.text)
	else:
		return '请求失败'
def print_data(data_form):
		print(flag(data_form))
		print(view_version(data_form))
		print(view_disablefunction(data_form))
		print(view_openbasedir(data_form))
		print(session_serialize(data_form))
		print(session_path(data_form))
def view_version(page):
	version_id = re.findall('<h1 class="p">(.*)</h1>',page)
	return "".join(version_id)
def view_disablefunction(page):
	null = '<i>no value</i></td><td class="v"><i>no value</i>'
	disable_functionlist=re.findall('<td class="e">disable_functions</td><td class="v">(.*)</td></tr>',page)
	#print(disable_functionlist)
	if(null in disable_functionlist):
		return 'disable_functions: 空'
	else:
		disable_functionlist[0] = re.sub(('</td><td class="v">(.*)'),'',''.join(disable_functionlist))
		return 'disable_functions: '+disable_functionlist[0]

def view_openbasedir(page):
	null = '<i>no value</i></td><td class="v"><i>no value</i>'
	openbasedir_id = re.findall('<td class="e">open_basedir</td><td class="v">(.*)</td>',page)
	if(null in openbasedir_id):
		return 'open_basedir: 空'
	else:
		openbasedir_id = re.sub(('</td><td class="v">(.*)'),'',''.join(openbasedir_id))
		return 'open_basedir: '+str(openbasedir_id)
def session_serialize(page):
	session_serialize = re.findall('<td class="e">session.serialize_handler</td><td class="v">(.*)</td></tr>',page)
	session_serialize = re.sub(('</td><td class="v">(.*)'),'',''.join(session_serialize))
	return 'session_serialize_handler: '+str(session_serialize)

def session_path(page):
	sessionsave_path = re.findall('<td class="e">session.save_path</td><td class="v">(.*)</td></tr>',page)
	sessionsave_path = re.sub(('</td><td class="v">(.*)'),'',''.join(sessionsave_path))
	if('<i>no value</i>' in sessionsave_path):
		return 'session.save_path: 空'
	else:
		return 'session.save_path: '+str(sessionsave_path)

def flag(page):
	find_flag = re.findall('ctfhub{.*',page)
	if(len(find_flag)==0):
		return 'flag: Not found flag!'
	else:
		return find_flag[0]