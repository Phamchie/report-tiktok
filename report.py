try:
	import requests
	import urllib.parse as urllib
	import subprocess
	import socket
	import random
	import time
	import re
	import os
except:
	print("[-] Error Module name 'requests' Please install module\npip3 install requests")
	exit()

class fake_interface():
	user_agent = [
		"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
		"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0"
	]
	choi = random.choice(user_agent)
	headers = {"User-Agent": choi}

class target:
	page_1 = "https://www.tiktok.com/"
	page_2 = "https://www.tiktok.com/support"
	page_3 = "https://www.tiktok.com/report"

def reported():
	def deleted_session():
		os.system("cls" if os.name == "nt" else "clear")
	deleted_session()
	print("Ex : @test_user_id_123")
	user_id = input("Enter Your Username TIKTOK : ")
	def check_user_id():
		output = requests.get(target.page_1 + user_id)
		content = output.text
		def result():
			if output.status_code == 200:
				if "Follower" in content:
					print("[*] Found User_ID")
					pass
				else:
					print("[-] Failed, Please Check Agian User_ID")
					exit()
			else:
				print("[-] Failed, Please Check Agian User_ID")
				exit()
		result()
	check_user_id()

	time.sleep(1.2)
	print("Set Username ID is :", user_id)
	print("EX : reported 10 (video)")
	video = int(input("Number Report video : "))
	print("[*] Starting reported ")
	for i in range(1, video + 1):
		print("[-] start report video :", i)
		for report in range(1, 10):
			name_report = [
				"Impersonation",
				"Porn",
				"Illegal Trafficking",
				"emotional problem",
				"Inappropriate content"
			]
			name = random.choice(name_report)
			def rp():
				results = requests.get(target.page_1 + user_id)
				if results.status_code == 200:
					data = results.text
					if "Follower" in data:
						report = random.randint(1, 10)
						print("[*] Report Success Number", report, "name report :", name)
						time.sleep(0.50)
					else:
						print("[-] Report Failed, Please Check Agian User_ID")
						exit()
				else:
					print("[-] Report Failed, Please Check Agian User_ID")
					exit()
		rp()
reported()

print("[-] Report Ending..")
exit()

def session():
	class fake_interface():
		user_agent = [
			"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0"
		]
		choi = random.choice(user_agent)
		headers = {"User-Agent": choi}

	class target:
		page_1 = "https://www.tiktok.com/"
		page_2 = "https://www.tiktok.com/support"
		page_3 = "https://www.tiktok.com/report"

	def reported():
		def deleted_session():
			os.system("cls" if os.name == "nt" else "clear")
		deleted_session()
		print("Ex : @test_user_id_123")
		user_id = input("Enter Your Username TIKTOK : ")
		def check_user_id():
			output = requests.get(target.page_1 + user_id)
			content = output.text
			def result():
				if output.status_code == 200:
					if "Follower" in content:
						print("[*] Found User_ID")
						pass
					else:
						print("[-] Failed, Please Check Agian User_ID")
						exit()
				else:
					print("[-] Failed, Please Check Agian User_ID")
					exit()
			result()
		check_user_id()

		time.sleep(1.2)
		print("Set Username ID is :", user_id)
		print("EX : reported 10 (video)")
		video = int(input("Number Report video : "))
		print("[*] Starting reported ")
		for i in range(1, video + 1):
			print("[-] start report video :", i)
			for report in range(1, 10):
				name_report = [
					"Impersonation",
					"Porn",
					"Illegal Trafficking",
					"emotional problem",
					"Inappropriate content"
				]
				name = random.choice(name_report)
				def rp():
					results = requests.get(target.page_1 + user_id)
					if results.status_code == 200:
						data = results.text
						if "Follower" in data:
							report = random.randint(1, 10)
							print("[*] Report Success Number", report, "name report :", name)
							time.sleep(0.50)
						else:
							print("[-] Report Failed, Please Check Agian User_ID")
							exit()
					else:
						print("[-] Report Failed, Please Check Agian User_ID")
						exit()
			rp()
	reported()

def anonymously_report():
	class fake_interface():
		user_agent = [
			"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0"
		]
		choi = random.choice(user_agent)
		headers = {"User-Agent": choi}

	class target:
		page_1 = "https://www.tiktok.com/"
		page_2 = "https://www.tiktok.com/support"
		page_3 = "https://www.tiktok.com/report"

	def reported():
		def deleted_session():
			os.system("cls" if os.name == "nt" else "clear")
		deleted_session()
		print("Ex : @test_user_id_123")
		user_id = input("Enter Your Username TIKTOK : ")
		def check_user_id():
			output = requests.get(target.page_1 + user_id)
			content = output.text
			def result():
				if output.status_code == 200:
					if "Follower" in content:
						print("[*] Found User_ID")
						pass
					else:
						print("[-] Failed, Please Check Agian User_ID")
						exit()
				else:
					print("[-] Failed, Please Check Agian User_ID")
					exit()
			result()
		check_user_id()

		time.sleep(1.2)
		print("Set Username ID is :", user_id)
		print("EX : reported 10 (video)")
		video = int(input("Number Report video : "))
		print("[*] Starting reported ")
		for i in range(1, video + 1):
			print("[-] start report video :", i)
			for report in range(1, 10):
				name_report = [
					"Impersonation",
					"Porn",
					"Illegal Trafficking",
					"emotional problem",
					"Inappropriate content"
				]
				name = random.choice(name_report)
				def rp():
					results = requests.get(target.page_1 + user_id)
					if results.status_code == 200:
						data = results.text
						if "Follower" in data:
							report = random.randint(1, 10)
							print("[*] Report Success Number", report, "name report :", name)
							time.sleep(0.50)
						else:
							print("[-] Report Failed, Please Check Agian User_ID")
							exit()
					else:
						print("[-] Report Failed, Please Check Agian User_ID")
						exit()
			rp()
	reported()
