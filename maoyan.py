import requests
import re
import json
import time


def get_one_page(url):
	headers={
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
	# 'Cookie':'__mta=150369801.1534219634166.1534238145225.1534238968184.14"; uuid_n_v=v1; uuid=859132109F7711E8926E19CBE76AC7D78181421A676C44D3AFA5955D88D74F5E; _csrf=fd86027e38a9290bd488462f7fe47864b035143252bcb7115e85f03d007477f3; _lxsdk_cuid=165369dc0e5c8-06e2a52cd5f9b2-34677909-13c680-165369dc0e559; _lxsdk=859132109F7711E8926E19CBE76AC7D78181421A676C44D3AFA5955D88D74F5E; __mta=150369801.1534219634166.1534222830617.1534222854030.10"; _lxsdk_s=16537b83779-a18-3e9-6c8%7C%7C4'
	'Cookie':'__mta=150369801.1534219634166.1534258044057.1534260192366.20"; uuid_n_v=v1; uuid=859132109F7711E8926E19CBE76AC7D78181421A676C44D3AFA5955D88D74F5E; _csrf=fd86027e38a9290bd488462f7fe47864b035143252bcb7115e85f03d007477f3; _lxsdk_cuid=165369dc0e5c8-06e2a52cd5f9b2-34677909-13c680-165369dc0e559; _lxsdk=859132109F7711E8926E19CBE76AC7D78181421A676C44D3AFA5955D88D74F5E; __mta=150369801.1534219634166.1534222830617.1534222854030.10"; _lxsdk_s=%7C%7C0'
	# 'User_}Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
	}
	response=requests.get(url,headers=headers)
	if response.status_code==200:
		return response.text
	return None

def parse_one_page(html):
		# 
	  # pattern=re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',re.S)
		pattern=re.compile(
			'<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?data-val.*?>(.*?)</a>.*?"star">(.*?)</p>.*?"releasetime">(.*?)</p>.*?"integer">(.*?)</i>.*?"fraction">(.*?)</i></p>',re.S)
		items=re.findall(pattern,html)
		print('____________________')
		print(items)
		print('____________________')
		# a={}
		# for item in items:
		# 	a['index']=item[0]
		# 	a['image']=item[1]
		# 	print(a)

		# while items:
		for item in items:
			yield {'index':item[0],
			'image':item[1],
			'title':item[2].strip(),
			'actor':item[3].strip()[3:],
			'time':item[4].strip()[5:],
			'score':item[5].strip()+item[6].strip()}

def write_to_file(content):
		with open('result.txt','a',encoding='utf-8') as f:
			print(type(json.dumps(content)))
			f.write(json.dumps(content,ensure_ascii=False)+'\n')	

def main(offset):
	url='http://maoyan.com/board/4?offset='+str(offset)
	html=get_one_page(url)
	print(html)
	for a in parse_one_page(html):
		print(a)
		write_to_file(a)

	

if __name__=='__main__':
	for i in range(10):
		main(offset=i*10)
		time.sleep(1)

