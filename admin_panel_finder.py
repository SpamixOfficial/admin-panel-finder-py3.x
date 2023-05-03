#from urllib.request import Request, urlopen
#from urllib.error import URLError, HTTPError
import requests
import argparse
import threading
from tqdm import tqdm

parser = argparse.ArgumentParser(
					prog='admin_panel_finder',
					description='Find admin panels of webpages (Make sure to use a proxy or the firewall might block you!)',
					epilog='Original made by GitHub User "bdblackhat", Current Version is by GitHub User "SpamixOfficial"')
parser.add_argument("page", help="The webpage you want to search (ex : example.com or www.example.com )")
args = parser.parse_args()

nums = 0
fnums = 294

def progress_bar():
    global nums, fnums
    for int in tqdm(range(fnums)):
        olnum = nums
        while True:
            if not nums == olnum:
                break
            continue	

threading.Thread(target=progress_bar).start()

def findAdmin(link=args.page):
	global nums
	nlink = 0
	links = []
	enum = {"200": 0, "404": 0, "403": 0}
	flinks = 0
	f = open("link.txt","r")
	while True:
		nums += 1
		sub_link = f.readline()
		if not sub_link:
			break		
		req_link = f"https://{link}/{sub_link}"
		req = requests.head(req_link)
		if not req.status_code == 200:
			if str(req.status_code) in enum:
				enum[str(req.status_code)] += 1
			if not str(req.status_code) in enum:
				enum[str(req.status_code)] = 1
		elif req.status_code == 200:
			enum["200"] += 1
			links += req_link
	for link in links:
		nlink += 1
	if nlink > 0:
		print("\n\nAvailable links : \n")
		for link in links: 
			print(f"{link}\n")
	elif nlink <= 0:
		print("\n\nNo Available Links")
	for key in enum:
		if key == "200" and not enum[key] == 0:
			print(f"{key} Responses: {enum[key]}")
		elif not enum[key] == 0 and not key == "200":
			print(f"{key} Errors: {enum[key]}")

findAdmin()