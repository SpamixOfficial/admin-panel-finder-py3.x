from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import argparse

parser = argparse.ArgumentParser(
					prog='admin_panel_finder',
					description='Find admin panels of webpages (Make sure to use a proxy or the firewall might block you!)',
					epilog='Original made by GitHub User "bdblackhat", Current Version is by GitHub User "SpamixOfficial"')
parser.add_argument("page", help="The webpage you want to search (ex : example.com or www.example.com )")
args = parser.parse_args()

nums = 0

def findAdmin(link=args.page):
	global nums
	f = open("link.txt","r")
	print("\n\nAvailable links : \n")
	while True:
		nums += 1
		print(nums)
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = f"http://{link}/{sub_link}"
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print(f"OK => {req_link}")

findAdmin()
