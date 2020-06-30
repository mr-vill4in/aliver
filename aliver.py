import requests as req 
import argparse
from termcolor import colored
from urllib.parse import urlparse
from requests.exceptions import ConnectionError
from requests_futures.sessions import FuturesSession

def start():
	print(colored("                   _    _     _____     _______ ____     ",'cyan'))
	print(colored("                  / \  | |   |_ _\ \   / / ____|  _ \    ",'cyan'))
	print(colored("                 / _ \ | |    | | \ \ / /|  _| | |_) |   ",'cyan'))
	print(colored("                / ___ \| |___ | |  \ V / | |___|  _ <    ",'cyan'))
	print(colored("               /_/   \_\_____|___|  \_/  |_____|_| \_\   ",'cyan'))
	print(colored("                                                         ",'cyan'))
	print("")
	print(colored("#====================================================================#", 'yellow'))
	print(colored("#|||||||||||||||||||||| Develop by MR_VILLAIN |||||||||||||||||||||||#", 'yellow'))
	print(colored("######################## Twitter:@K_m_tanvir #########################", 'yellow'))
	print(colored("#--------------------------------------------------------------------#", 'yellow'))
	print(colored("#                     Domain Response Checker V.1.0                  #", 'yellow'))
	print(colored("#====================================================================#", 'yellow'))

def url_0():
	print(colored("#====================================================================#", 'cyan'))
	print(colored("#               Single Domain Response Check Finished                #", 'cyan'))
	print(colored("#====================================================================#", 'cyan'))

def url_1():
	print(colored("#====================================================================#", 'cyan'))
	print(colored("#                Multi Domain Response Check Finished                #", 'cyan'))
	print(colored("#====================================================================#", 'cyan'))

start()

parser = argparse.ArgumentParser()
parser.add_argument('-u', help='target url', dest='url')
parser.add_argument('-urls', help='file containing target urls', dest='url_file')
args = parser.parse_args()

url = args.url
url_file = args.url_file
urls=[]

#wordlist = input("Enter Your wordlist : ")
if url:
	try:
		get_response = req.get("https://" + url)
		Response = url
		print(colored("[+] Url Alive     -->",'green'),Response)
		f= open("link.txt","a+")
		f.write(str(Response))
		f.write("\n")
		f.close()
		    

	except req.exceptions.ConnectionError:
		print(colored("[-] Url Not Alive -->",'red'),Response)
		pass
	url_0()

if url_file:
    file = open(url_file, "r")
    for line in file:
        if not urlparse(line).scheme:
            line = "https://"+line
        urls.append(line.strip())
    with FuturesSession() as session:
        futures = [session.get(url,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6)'}) for url in urls]
        for f,u in zip(futures,urls):
            try:

            	print(colored(" URL Alive    ----> {} : {} ".format(u,f.result().status_code),'green'))
            	response = ('{}'.format(u))
            	f = open('alive.txt','a+')
            	f.write(str(response))
            	f.write('\n')
            	f.close()

		    
            except ConnectionError:
                    print(colored(" URL Not Alive ----> {} ".format(u), 'red'))
        url_1()

