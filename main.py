import requests
from banner import BANNER

from colorama import Fore, Style, Back, init
init()

class userFidner:
    def __init__(self) -> None:
        print(BANNER + Fore.CYAN)
        self.args = input("\n[→] Имя пользователя: ")

    def Finder(self):

        file = open(f"cache\{self.args}.txt", "w")

            ## INSTAGRAM

        check_Instagram = f"https://www.instagram.com/{self.args}/"
    
        try:
            response = requests.head(check_Instagram)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Instagram: аккаунт найден! " + check_Instagram)
            file.write("Instagram: " + check_Instagram + "\n")
            if response.status_code == 404:
                print(Fore.YELLOW + "[-] Instagram: аккаунт не найден!")
            if response.status_code == 301:
                print(Fore.YELLOW + "[d] Instagram: аккаунт удалён!")
            if response.status_code == 403:
                print(Fore.RED + "[x] Instagram: доступ запрещён!")

        except requests.ConnectionError:
            print(Fore.RED + "[e] Instagram: произошла ошибка")

            ## FACEBOOK
    
        check_Facebook = f"https://www.facebook.com/{self.args}/"

        try:
            response = requests.head(check_Facebook)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Facebook: аккаунт найден! " + check_Facebook)
                file.write("Facebook: " + check_Facebook + "\n")
            if response.status_code == 404:
                print(Fore.YELLOW + "[-] Facebook: аккаунт не найден!")
            if response.status_code == 301:
                print(Fore.YELLOW + "[d] Facebook: аккаунт удалён!")
            if response.status_code == 403:
                print(Fore.RED + "[x] Facebook: доступ запрещён!")

        except requests.ConnectionError:
            print(Fore.RED + "[e] Facebook: произошла ошибка")

            ## YOUTUBE

        check_Youtube = f"https://www.youtube.com/{self.args}/"

        try:
            response = requests.head(check_Youtube)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] YouTube: аккаунт найден! " + check_Youtube)
                file.write("YouTube: " + check_Youtube + "\n")
            if response.status_code == 404:
                print(Fore.YELLOW + "[-] YouTube: аккаунт не найден!")
            if response.status_code == 301:
                print(Fore.YELLOW + "[d] YouTube: аккаунт удалён!")
            if response.status_code == 403:
                print(Fore.RED + "[x] YouTube: доступ запрещён!")

        except requests.ConnectionError:
            print(Fore.RED + "[e] YouTube: произошла ошибка")

            ## TWITCH

        check_Twitch = f"https://www.twitch.tv/{self.args}/"

        try:
            response = requests.head(check_Twitch)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Twitch: аккаунт найден! " + check_Twitch)
                file.write("Twitch: " + check_Twitch + "\n")
            if response.status_code == 404:
                print(Fore.YELLOW + "[-] Twitch: аккаунт не найден!")
            if response.status_code == 301:
                print(Fore.YELLOW + "[d] Twitch: аккаунт удалён!")
            if response.status_code == 403:
                print(Fore.RED + "[x] Twitch: доступ запрещён!")

        except requests.ConnectionError:
            print(Fore.RED + "[e] Twitch: произошла ошибка")

            ## TWITTER

        check_Twitter = f"https://twitter.com/{self.args}/"

        try:
            response = requests.head(check_Twitter)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Twitter: аккаунт найден! " + check_Twitter)
                file.write("Twitter: " + check_Twitter + "\n")
            if response.status_code == 404:
                print(Fore.YELLOW + "[-] Twitter: аккаунт не найден!")
            if response.status_code == 301:
                print(Fore.YELLOW + "[d] Twitter: аккаунт удалён!")
            if response.status_code == 403:
                print(Fore.RED + "[x] Twitter: доступ запрещён!")

        except requests.ConnectionError:
            print(Fore.RED + "[e] Twitter: произошла ошибка")

            ## REDDIT

        check_Reddit = f"https://www.reddit.com/user/{self.args}/"

        try:
            response = requests.head(check_Reddit)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Reddit: аккаунт найден! " + check_Reddit)
                file.write("Reddit: " + check_Reddit + "\n")
            if response.status_code == 502 or 404:
                print(Fore.YELLOW + "[-] Reddit: аккаунт не найден!")
            if response.status_code == 301:
                print(Fore.YELLOW + "[d] Reddit: аккаунт удалён!")
            if response.status_code == 403:
                print(Fore.RED + "[x] Reddit: доступ запрещён!")

        except requests.ConnectionError:
            print(Fore.RED + "[e] Reddit: произошла ошибка")

            ## PINTEREST

        check_Pinterest = f"https://www.pinterest.ca/{self.args}/"

        try:
            response = requests.head(check_Pinterest)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Pinterest: аккаунт найден! " + check_Pinterest)
                file.write("Pinterest: " + check_Pinterest + "\n")
            if response.status_code == 404:
                print(Fore.YELLOW + "[-] Pinterest: аккаунт не найден!")
            if response.status_code == 301:
                print(Fore.YELLOW + "[d] Pinterest: аккаунт удалён!")
            if response.status_code == 403:
                print(Fore.RED + "[x] Pinterest: доступ запрещён!")

        except requests.ConnectionError:
            print(Fore.RED + "[e] Pinterest: произошла ошибка")

            ## ОДНОКЛАСНИКИ

        check_ok = f"https://ok.ru/{self.args}/"

        try:
            response = requests.head(check_ok)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Однокласники: аккаунт найден! " + check_ok)
                file.write("Однокласники: " + check_ok + "\n")
            if response.status_code == 404:
                print(Fore.YELLOW + "[-] Однокласники: аккаунт не найден!")
            if response.status_code == 301:
                print(Fore.YELLOW + "[d] Однокласники: аккаунт удалён!")
            if response.status_code == 403:
                print(Fore.RED + "[x] Однокласники: доступ запрещён!")

        except requests.ConnectionError:
            print(Fore.RED + "[e] Однокласники: произошла ошибка")

            ## DEVIANTART

        check_Deviantart = f"https://www.deviantart.com/{self.args}/"
        
        try:
            response = requests.head(check_Deviantart)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Deviantart: аккаунт найден! " + check_Deviantart)
                file.write("Deviantart: " + check_Deviantart + "\n")
            if response.status_code == 404:
                print(Fore.YELLOW + "[-] Deviantart: аккаунт не найден!")
            if response.status_code == 301:
                print(Fore.YELLOW + "[d] Deviantart: аккаунт удалён!")
            if response.status_code == 403:
                print(Fore.RED + "[x] Deviantart: доступ запрещён!")

        except requests.ConnectionError:
            print(Fore.RED + "[e] Deviantart: произошла ошибка")

            ## GITHUB

        check_Github = f"https://github.com/{self.args}/"

        try:
            response = requests.head(check_Github)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Github: аккаунт найден! " + check_Github)
                file.write("Github: " + check_Github + "\n")
            if response.status_code == 404:
                print(Fore.YELLOW + "[-] Github: аккаунт не найден!")
            if response.status_code == 301:
                print(Fore.YELLOW + "[d] Github: аккаунт удалён!")
            if response.status_code == 403:
                print(Fore.RED + "[x] Github: доступ запрещён!")
        
        except requests.ConnectionError:
            print(Fore.RED + "[e] Github: произошла ошибка")

            ## WORDPRESS

        check_Wordpress = f"https://{self.args}.wordpress.com/"

        try:
            response = requests.head(check_Wordpress)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Wordpress: аккаунт найден! " + check_Wordpress)
                file.write("Wordpress: " + check_Wordpress + "\n")
            if response.status_code == 404:
                print(Fore.YELLOW + "[-] Wordpress: аккаунт не найден!")
            if response.status_code == 301:
                print(Fore.YELLOW + "[d] Wordpress: аккаунт удалён!")
            if response.status_code == 403:
                print(Fore.RED + "[x] Wordpress: доступ запрещён!")

        except requests.ConnectionError:
            print(Fore.RED + "[e] Wordpress: произошла ошибка")

            ## FLICKR

        check_Flickr = f"https://www.flickr.com/photos/{self.args}/"

        try:
            response = requests.head(check_Flickr)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Flickr: аккаунт найден! " + check_Flickr)
                file.write("Flickr: " + check_Flickr + "\n")
            if response.status_code == 404:
                print(Fore.YELLOW + "[-] Flickr: аккаунт не найден!")
            if response.status_code == 301:
                print(Fore.YELLOW + "[d] Flickr: аккаунт удалён!")
            if response.status_code == 403:
                print(Fore.RED + "[x] Flickr: доступ запрещён!")

        except requests.ConnectionError:
            print(Fore.RED + "[e] Flickr: произошла ошибка")

            ## SOUNDCLOUD

        check_Soundcloud = f"https://soundcloud.com/{self.args}/"

        try:
            response = requests.head(check_Soundcloud)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Soundcloud: аккаунт найден! " + check_Soundcloud)
                file.write("Soundcloud: " + check_Soundcloud + "\n")
            if response.status_code == 404:
                print(Fore.YELLOW + "[-] Soundcloud: аккаунт не найден!")
            if response.status_code == 301:
                print(Fore.YELLOW + "[d] Soundcloud: аккаунт удалён!")
            if response.status_code == 403:
                print(Fore.RED + "[x] Soundcloud: доступ запрещён!")

        except requests.ConnectionError:
            print(Fore.RED + "[e] Soundcloud: произошла ошибка")

            ## PATREON

        check_Patreon = f"https://www.patreon.com/{self.args}/"

        try:
            response = requests.head(check_Patreon)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Patreon: аккаунт найден! " + check_Patreon)
                file.write("Patreon: " + check_Patreon + "\n")
            if response.status_code == 404:
                print(Fore.YELLOW + "[-] Patreon: аккаунт не найден!")
            if response.status_code == 301:
                print(Fore.YELLOW + "[d] Patreon: аккаунт удалён!")
            if response.status_code == 403:
                print(Fore.RED + "[x] Patreon: доступ запрещён!")

        except requests.ConnectionError:
            print(Fore.RED + "[e] Patreon: произошла ошибка")

            ## IFTTT

        check_Ifttt = f"https://www.ifttt.com/p/{self.args}/"

        try:
            response = requests.head(check_Ifttt)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Ifttt: аккаунт найден! " + check_Ifttt)
                file.write("Ifttt: " + check_Ifttt + "\n")
            if response.status_code == 404:
                print(Fore.YELLOW + "[-] Ifttt: аккаунт не найден!")
            if response.status_code == 301:
                print(Fore.YELLOW + "[d] Ifttt: аккаунт удалён!")
            if response.status_code == 403:
                print(Fore.RED + "[x] Ifttt: доступ запрещён!")

        except requests.ConnectionError:
            print(Fore.RED + "[e] Ifttt: произошла ошибка")

            ## EBAY

        check_Ebay = f"https://www.ebay.com/usr/{self.args}/"

        try:
            response = requests.head(check_Ebay)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Ebay: аккаунт найден! " + check_Ebay)
                file.write("Ebay: " + check_Ebay + "\n")
            if response.status_code == 404:
                print(Fore.YELLOW + "[-] Ebay: аккаунт не найден!")
            if response.status_code == 301:
                print(Fore.YELLOW + "[d] Ebay: аккаунт удалён!")
            if response.status_code == 403:
                print(Fore.RED + "[x] Ebay: доступ запрещён!")

        except requests.ConnectionError:
            print(Fore.RED + "[e] Ebay: произошла ошибка")

            ## TELEGRAM

        check_Telegram = f"https://t.me/{self.args}/"

        try:
            response = requests.head(check_Telegram)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Telegram: аккаунт найден! " + check_Telegram)
                file.write("Telegram: " + check_Telegram + "\n")
            if response.status_code == 404:
                print(Fore.YELLOW + "[-] Telegram: аккаунт не найден!")
            if response.status_code == 301:
                print(Fore.YELLOW + "[d] Telegram: аккаунт удалён!")
            if response.status_code == 403:
                print(Fore.RED + "[x] Telegram: доступ запрещён!")

        except requests.ConnectionError:
            print(Fore.RED + "[e] Telegram: произошла ошибка")

            ## REPLIT

        check_Replit = f"https://replit.com/{self.args}/"

        try:
            response = requests.head(check_Replit)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Replit: аккаунт найден! " + check_Replit)
                file.write("Replit: " + check_Replit + "\n")
            if response.status_code == 404:
                print(Fore.YELLOW + "[-] Replit: аккаунт не найден!")
            if response.status_code == 301:
                print(Fore.YELLOW + "[d] Replit: аккаунт удалён!")
            if response.status_code == 403:
                print(Fore.RED + "[x] Replit: доступ запрещён!")

        except requests.ConnectionError:
            print(Fore.RED + "[e] Replit: произошла ошибка")

            ## HABR

        check_Habr = f"https://qna.habr.com/user/{self.args}/"

        try:
            response = requests.head(check_Habr)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Habr Q&A: аккаунт найден! " + check_Habr)
                file.write("Habr Q&A: " + check_Habr + "\n")
            if response.status_code == 404:
                print(Fore.YELLOW + "[-] Habr Q&A: аккаунт не найден!")
            if response.status_code == 301:
                print(Fore.YELLOW + "[d] Habr Q&A: аккаунт удалён!")
            if response.status_code == 403:
                print(Fore.RED + "[x] Habr Q&A: доступ запрещён!")

        except requests.ConnectionError:
            print(Fore.RED + "[e] Habr Q&A: произошла ошибка")

            ## BLOGSPOT

        check_Blogspot = f"https://{self.args}.blogspot.com/"

        try:
            response = requests.head(check_Blogspot)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Blogspot: аккаунт найден! " + check_Blogspot)
                file.write("Blogspot: " + check_Blogspot + "\n")
            if response.status_code == 404:
                print(Fore.YELLOW + "[-] Blogspot: аккаунт не найден!")
            if response.status_code == 301:
                print(Fore.YELLOW + "[d] Blogspot: аккаунт удалён!")
            if response.status_code == 403:
                print(Fore.RED + "[x] Blogspot: доступ запрещён!")

        except requests.ConnectionError:
            print(Fore.RED + "[e] Blogspot: произошла ошибка")

            ## TILDA

        check_Tilda = f"http://{self.args}.tilda.ws/"

        try:
            response = requests.head(check_Tilda)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Tilda: аккаунт найден! " + check_Tilda)
                file.write("Tilda: " + check_Tilda + "\n")
            if response.status_code == 404:
                print(Fore.YELLOW + "[-] Tilda: аккаунт не найден!")
            if response.status_code == 301:
                print(Fore.YELLOW + "[d] Tilda: аккаунт удалён!")
            if response.status_code == 403:
                print(Fore.RED + "[x] Tilda: доступ запрещён!")

        except requests.ConnectionError:
            print(Fore.RED + "[e] Tilda: произошла ошибка")

            ## DONATIONALERTS

        check_Donationalerts = f"https://www.donationalerts.com/r/{self.args}/"

        try:
            response = requests.head(check_Donationalerts)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Donationalerts: аккаунт найден! " + check_Donationalerts)
                file.write("Donationalerts:" + check_Donationalerts + "\n")
            if response.status_code == 404:
                print(Fore.YELLOW + "[-] Donationalerts: аккаунт не найден!")
            if response.status_code == 301:
                print(Fore.YELLOW + "[d] Donationalerts: аккаунт удалён!")
            if response.status_code == 403:
                print(Fore.RED + "[x] Donationalerts: доступ запрещён!")

        except requests.ConnectionError:
            print(Fore.RED + "[e] Donationalerts: произошла ошибка")

        file.close()

        print(Fore.CYAN + "\n[\] Все найденнные аккаунты сохранены:")
        print(Fore.CYAN + f"[\] cache\\{self.args}.txt")

userfidner = userFidner()
userfidner.Finder()
