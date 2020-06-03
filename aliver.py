import requests as req 
import argparse
from termcolor import colored

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


parser = argparse.ArgumentParser()
parser.add_argument('-u', help='target url', dest='url')
parser.add_argument('-urls', help='file containing target urls', dest='url_file')
args = parser.parse_args()

url = args.url
url_file = args.url_file



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

if url_file:
	file = open(url_file, "r")
	for line in file:
		word = line.strip()   
		try:
		    get_response = req.get("https://" + word)
		    Response = word
		    print(colored("[+] Url Alive     -->",'green'),Response)
		    f= open("alive.txt","a+")
		    f.write(str(Response))
		    f.write("\n")
		    f.close()
		    

		except req.exceptions.ConnectionError:
		    print(colored("[-] Url Not Alive -->",'red'),Response)
		    pass
		





