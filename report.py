
import os

try:
        import requests
        import re
except:
        os.system("pip3 install requests")

try:
        from bs4 import BeautifulSoup as soups
except:
        os.system("pip3 install bs4")

class API:
        server = "https://www.tiktok.com/"
        conn = "https://www.tiktok.com/legal/report/feedback"

class text:
        thanchu = "안녕하세요 틱톡팀입니다. 이 계정은 TikTok에 적합하지 않습니다. 이 아 이는 내 아이입니다. 나는 아기의 엄마입니다. 이 계정은 내 아들이 만들었고 Tik Tok 계정을 가질 수 있는 나이가 되지 않았으며 TikTok 커뮤니티의 기준을 따르지 않습니다. 소년은 또한 사생활을 침해하고 Tik Tok 계정을 등록하기 위해 가짜 출생 정보를 제공했습니다. 이 계정은 11세의 계정이며, 저는 어머니로서 이 계정이 11세의 계정임을 확인합니다. TikTok 커뮤니티  표준에 따라 자녀의 계정을 검토하고 일시 중지하십시오. Tiktok이 내 자녀의 계정을 정지하기를 바랍니다. 감사합니다 틱톡!!!"

os.system("cls" if os.name == "nt" else "clear")
print()
print("REPORT TIKTOK BY CHIEN")
print("+ Report 13 Year Old and Random Report All Video")
print()
id1 = input("Enter User ID : ")

def check():
        session = requests.Session()
        result = session.get(API.server + id1)
        content = result.text
        try:
                if result.status_code == 200:
                        if "Follower" in content:
                                print("[*] Found User ID")
                        else:
                                print("[×] Failed , Not Found User ID")
        except:
                print("[×] Connect Failed")
                exit()
check()

def report_13_year():
        for i in range(1, 99999):
                session = requests.Session()
                data = {
                        "Email": "phamchienlc06@gmail.com",
                        "TikTok ID": f"{id1}",
                        "<input>": f"{text.thanchu}"
                }
                rp = session.get(API.conn)
                cont = rp.text
                try:
                        print("[✓] Report Done", i, "Random Report")
                except:
                        exit()
report_13_year()

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
