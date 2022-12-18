import requests
from banner import BANNER

from colorama import Fore, Style, Back, init
init()

class userFidner:
    def __init__(self) -> None:
        print(BANNER + Fore.CYAN)
        self.args = input("\n[→] Username: ")

    def Finder(self):
        file = open(f"cache\{self.args}.txt", "w")

            ###################
            ##               ##
            ##   INSTAGRAM   ##
            ## ↓           ↓ ##
            ###################

        check_Instagram = f"https://www.instagram.com/{self.args}/"
    
        try:
            response = requests.head(check_Instagram)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Instagram: account found! " + check_Instagram)
            file.write("Instagram: " + check_Instagram + "\n")
            if response.status_code == 404:
                print(Fore.YELLOW + "[-] Instagram: account not found!")
            if response.status_code == 301:
                print(Fore.YELLOW + "[d] Instagram: account deleted!")
            if response.status_code == 403:
                print(Fore.RED + "[x] Instagram: access is denied!")

        except requests.ConnectionError:
            print(Fore.RED + "[e] Instagram: an error has occurred!")

            ##################
            ##              ##
            ##   FACEBOOK   ##
            ## ↓          ↓ ##
            ##################
    
        check_Facebook = f"https://www.facebook.com/{self.args}/"

        try:
            response = requests.head(check_Facebook)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Facebook: account found! " + check_Facebook)
                file.write("Facebook: " + check_Facebook + "\n")
            if response.status_code == 404:
                print(Fore.YELLOW + "[-] Facebook: account not found!")
            if response.status_code == 301:
                print(Fore.YELLOW + "[d] Facebook: account deleted!")
            if response.status_code == 403:
                print(Fore.RED + "[x] Facebook: access is denied!")

        except requests.ConnectionError:
            print(Fore.RED + "[e] Facebook: an error has occurred!")

            ###################
            ##               ##
            ##    YOUTUBE    ##
            ## ↓           ↓ ##
            ###################

        check_Youtube = f"https://www.youtube.com/{self.args}/"

        try:
            response = requests.head(check_Youtube)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] YouTube: account found! " + check_Youtube)
                file.write("YouTube: " + check_Youtube + "\n")
            if response.status_code == 404:
                print(Fore.YELLOW + "[-] YouTube: account not found!")
            if response.status_code == 301:
                print(Fore.YELLOW + "[d] YouTube: account deleted!")
            if response.status_code == 403:
                print(Fore.RED + "[x] YouTube: access is denied!")

        except requests.ConnectionError:
            print(Fore.RED + "[e] YouTube: an error has occurred!")

            ##################
            ##              ##
            ##    TWITCH    ##
            ## ↓          ↓ ##
            ##################

        check_Twitch = f"https://www.twitch.tv/{self.args}/"

        try:
            response = requests.head(check_Twitch)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Twitch: account found! " + check_Twitch)
                file.write("Twitch: " + check_Twitch + "\n")
            if response.status_code == 404:
                print(Fore.YELLOW + "[-] Twitch: account not found!")
            if response.status_code == 301:
                print(Fore.YELLOW + "[d] Twitch: account deleted!")
            if response.status_code == 403:
                print(Fore.RED + "[x] Twitch: access is denied!")

        except requests.ConnectionError:
            print(Fore.RED + "[e] Twitch: an error has occurred!")

            ###################
            ##               ##
            ##    TWITTER    ##
            ## ↓           ↓ ##
            ###################

        check_Twitter = f"https://twitter.com/{self.args}/"

        try:
            response = requests.head(check_Twitter)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Twitter: account found! " + check_Twitter)
                file.write("Twitter: " + check_Twitter + "\n")
            if response.status_code == 404:
                print(Fore.YELLOW + "[-] Twitter: account not found!")
            if response.status_code == 301:
                print(Fore.YELLOW + "[d] Twitter: account deleted!")
            if response.status_code == 403:
                print(Fore.RED + "[x] Twitter: access is denied!")

        except requests.ConnectionError:
            print(Fore.RED + "[e] Twitter: an error has occurred!")

            ##################
            ##              ##
            ##    REDDIT    ##
            ## ↓          ↓ ##
            ##################

        check_Reddit = f"https://www.reddit.com/user/{self.args}/"

        try:
            response = requests.head(check_Reddit)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Reddit: account found! " + check_Reddit)
                file.write("Reddit: " + check_Reddit + "\n")
            if response.status_code == 502 or 404:
                print(Fore.YELLOW + "[-] Reddit: account not found!")
            if response.status_code == 301:
                print(Fore.YELLOW + "[d] Reddit: account deleted!")
            if response.status_code == 403:
                print(Fore.RED + "[x] Reddit: access is denied!")

        except requests.ConnectionError:
            print(Fore.RED + "[e] Reddit: an error has occurred!")

            ###################
            ##               ##
            ##   PINTEREST   ##
            ## ↓           ↓ ##
            ###################

        check_Pinterest = f"https://www.pinterest.ca/{self.args}/"

        try:
            response = requests.head(check_Pinterest)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Pinterest: account found! " + check_Pinterest)
                file.write("Pinterest: " + check_Pinterest + "\n")
            if response.status_code == 404:
                print(Fore.YELLOW + "[-] Pinterest: account not found!")
            if response.status_code == 301:
                print(Fore.YELLOW + "[d] Pinterest: account deleted!")
            if response.status_code == 403:
                print(Fore.RED + "[x] Pinterest: access is denied!")

        except requests.ConnectionError:
            print(Fore.RED + "[e] Pinterest: an error has occurred!")

            ####################
            ##                ##
            ##  ОДНОКЛАСНИКИ  ##
            ## ↓            ↓ ##
            ####################

        check_ok = f"https://ok.ru/{self.args}/"

        try:
            response = requests.head(check_ok)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Однокласники: account found! " + check_ok)
                file.write("Однокласники: " + check_ok + "\n")
            if response.status_code == 404:
                print(Fore.YELLOW + "[-] Однокласники: account not found!")
            if response.status_code == 301:
                print(Fore.YELLOW + "[d] Однокласники: account deleted!")
            if response.status_code == 403:
                print(Fore.RED + "[x] Однокласники: access is denied!")

        except requests.ConnectionError:
            print(Fore.RED + "[e] Однокласники: an error has occurred!")

            ##################
            ##              ##
            ##  DEVIANTART  ##
            ## ↓          ↓ ##
            ##################

        check_Deviantart = f"https://www.deviantart.com/{self.args}/"
        
        try:
            response = requests.head(check_Deviantart)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Deviantart: account found! " + check_Deviantart)
                file.write("Deviantart: " + check_Deviantart + "\n")
            if response.status_code == 404:
                print(Fore.YELLOW + "[-] Deviantart: account not found!")
            if response.status_code == 301:
                print(Fore.YELLOW + "[d] Deviantart: account deleted!")
            if response.status_code == 403:
                print(Fore.RED + "[x] Deviantart: access is denied!")

        except requests.ConnectionError:
            print(Fore.RED + "[e] Deviantart: an error has occurred!")

            ##################
            ##              ##
            ##    GITHUB    ##
            ## ↓          ↓ ##
            ##################

        check_Github = f"https://github.com/{self.args}/"

        try:
            response = requests.head(check_Github)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Github: account found! " + check_Github)
                file.write("Github: " + check_Github + "\n")
            if response.status_code == 404:
                print(Fore.YELLOW + "[-] Github: account not found!")
            if response.status_code == 301:
                print(Fore.YELLOW + "[d] Github: account deleted!")
            if response.status_code == 403:
                print(Fore.RED + "[x] Github: access is denied!")
        
        except requests.ConnectionError:
            print(Fore.RED + "[e] Github: an error has occurred!")

            ###################
            ##               ##
            ##   WORDPRESS   ##
            ## ↓           ↓ ##
            ###################

        check_Wordpress = f"https://{self.args}.wordpress.com/"

        try:
            response = requests.head(check_Wordpress)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Wordpress: account found! " + check_Wordpress)
                file.write("Wordpress: " + check_Wordpress + "\n")
            if response.status_code == 404:
                print(Fore.YELLOW + "[-] Wordpress: account not found!")
            if response.status_code == 301:
                print(Fore.YELLOW + "[d] Wordpress: account deleted!")
            if response.status_code == 403:
                print(Fore.RED + "[x] Wordpress: access is denied!")

        except requests.ConnectionError:
            print(Fore.RED + "[e] Wordpress: an error has occurred!")

            ##################
            ##              ##
            ##    FLICKR    ##
            ## ↓          ↓ ##
            ##################

        check_Flickr = f"https://www.flickr.com/photos/{self.args}/"

        try:
            response = requests.head(check_Flickr)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Flickr: account found! " + check_Flickr)
                file.write("Flickr: " + check_Flickr + "\n")
            if response.status_code == 404:
                print(Fore.YELLOW + "[-] Flickr: account not found!")
            if response.status_code == 301:
                print(Fore.YELLOW + "[d] Flickr: account deleted!")
            if response.status_code == 403:
                print(Fore.RED + "[x] Flickr: access is denied!")

        except requests.ConnectionError:
            print(Fore.RED + "[e] Flickr: an error has occurred!")

            ##################
            ##              ##
            ##  SOUNDCLOUD  ##
            ## ↓          ↓ ##
            ##################

        check_Soundcloud = f"https://soundcloud.com/{self.args}/"

        try:
            response = requests.head(check_Soundcloud)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Soundcloud: account found! " + check_Soundcloud)
                file.write("Soundcloud: " + check_Soundcloud + "\n")
            if response.status_code == 404:
                print(Fore.YELLOW + "[-] Soundcloud: account not found!")
            if response.status_code == 301:
                print(Fore.YELLOW + "[d] Soundcloud: account deleted!")
            if response.status_code == 403:
                print(Fore.RED + "[x] Soundcloud: access is denied!")

        except requests.ConnectionError:
            print(Fore.RED + "[e] Soundcloud: an error has occurred!")

            #################
            ##             ##
            ##   PATREON   ##
            ## ↓         ↓ ##
            #################

        check_Patreon = f"https://www.patreon.com/{self.args}/"

        try:
            response = requests.head(check_Patreon)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Patreon: account found! " + check_Patreon)
                file.write("Patreon: " + check_Patreon + "\n")
            if response.status_code == 404:
                print(Fore.YELLOW + "[-] Patreon: account not found!")
            if response.status_code == 301:
                print(Fore.YELLOW + "[d] Patreon: account deleted!")
            if response.status_code == 403:
                print(Fore.RED + "[x] Patreon: access is denied!")

        except requests.ConnectionError:
            print(Fore.RED + "[e] Patreon: an error has occurred!")

            #################
            ##             ##
            ##    IFTTT    ##
            ## ↓         ↓ ##
            #################

        check_Ifttt = f"https://www.ifttt.com/p/{self.args}/"

        try:
            response = requests.head(check_Ifttt)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Ifttt: account found! " + check_Ifttt)
                file.write("Ifttt: " + check_Ifttt + "\n")
            if response.status_code == 404:
                print(Fore.YELLOW + "[-] Ifttt: account not found!")
            if response.status_code == 301:
                print(Fore.YELLOW + "[d] Ifttt: account deleted!")
            if response.status_code == 403:
                print(Fore.RED + "[x] Ifttt: access is denied!")

        except requests.ConnectionError:
            print(Fore.RED + "[e] Ifttt: an error has occurred!")

            ################
            ##            ##
            ##    EBAY    ##
            ## ↓        ↓ ##
            ################

        check_Ebay = f"https://www.ebay.com/usr/{self.args}/"

        try:
            response = requests.head(check_Ebay)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Ebay: account found! " + check_Ebay)
                file.write("Ebay: " + check_Ebay + "\n")
            if response.status_code == 404:
                print(Fore.YELLOW + "[-] Ebay: account not found!")
            if response.status_code == 301:
                print(Fore.YELLOW + "[d] Ebay: account deleted!")
            if response.status_code == 403:
                print(Fore.RED + "[x] Ebay: access is denied!")

        except requests.ConnectionError:
            print(Fore.RED + "[e] Ebay: an error has occurred!")

            ################
            ##            ##
            ##  TELEGRAM  ##
            ## ↓        ↓ ##
            ################

        check_Telegram = f"https://t.me/{self.args}/"

        try:
            response = requests.head(check_Telegram)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Telegram: account found! " + check_Telegram)
                file.write("Telegram: " + check_Telegram + "\n")
            if response.status_code == 404:
                print(Fore.YELLOW + "[-] Telegram: account not found!")
            if response.status_code == 301:
                print(Fore.YELLOW + "[d] Telegram: account deleted!")
            if response.status_code == 403:
                print(Fore.RED + "[x] Telegram: access is denied!")

        except requests.ConnectionError:
            print(Fore.RED + "[e] Telegram: an error has occurred!")

            ################
            ##            ##
            ##   REPLIT   ##
            ## ↓        ↓ ##
            ################

        check_Replit = f"https://replit.com/{self.args}/"

        try:
            response = requests.head(check_Replit)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Replit: account found! " + check_Replit)
                file.write("Replit: " + check_Replit + "\n")
            if response.status_code == 404:
                print(Fore.YELLOW + "[-] Replit: account not found!")
            if response.status_code == 301:
                print(Fore.YELLOW + "[d] Replit: account deleted!")
            if response.status_code == 403:
                print(Fore.RED + "[x] Replit: access is denied!")

        except requests.ConnectionError:
            print(Fore.RED + "[e] Replit: an error has occurred!")

            ################
            ##            ##
            ##    HABR    ##
            ## ↓        ↓ ##
            ################

        check_Habr = f"https://qna.habr.com/user/{self.args}/"

        try:
            response = requests.head(check_Habr)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Habr Q&A: account found! " + check_Habr)
                file.write("Habr Q&A: " + check_Habr + "\n")
            if response.status_code == 404:
                print(Fore.YELLOW + "[-] Habr Q&A: account not found!")
            if response.status_code == 301:
                print(Fore.YELLOW + "[d] Habr Q&A: account deleted!")
            if response.status_code == 403:
                print(Fore.RED + "[x] Habr Q&A: access is denied!")

        except requests.ConnectionError:
            print(Fore.RED + "[e] Habr Q&A: an error has occurred!")

            ##################
            ##              ##
            ##   BLOGSPOT   ##
            ## ↓          ↓ ##
            ##################

        check_Blogspot = f"https://{self.args}.blogspot.com/"

        try:
            response = requests.head(check_Blogspot)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Blogspot: account found! " + check_Blogspot)
                file.write("Blogspot: " + check_Blogspot + "\n")
            if response.status_code == 404:
                print(Fore.YELLOW + "[-] Blogspot: account not found!")
            if response.status_code == 301:
                print(Fore.YELLOW + "[d] Blogspot: account deleted!")
            if response.status_code == 403:
                print(Fore.RED + "[x] Blogspot: access is denied!")

        except requests.ConnectionError:
            print(Fore.RED + "[e] Blogspot: an error has occurred!")

            #################
            ##             ##
            ##    TILDA    ##
            ## ↓         ↓ ##
            #################

        check_Tilda = f"http://{self.args}.tilda.ws/"

        try:
            response = requests.head(check_Tilda)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Tilda: account found! " + check_Tilda)
                file.write("Tilda: " + check_Tilda + "\n")
            if response.status_code == 404:
                print(Fore.YELLOW + "[-] Tilda: account not found!")
            if response.status_code == 301:
                print(Fore.YELLOW + "[d] Tilda: account deleted!")
            if response.status_code == 403:
                print(Fore.RED + "[x] Tilda: access is denied!")

        except requests.ConnectionError:
            print(Fore.RED + "[e] Tilda: an error has occurred!")

            ######################
            ##                  ##
            ##  DONATIONALERTS  ##
            ## ↓              ↓ ##
            ######################

        check_Donationalerts = f"https://www.donationalerts.com/r/{self.args}/"

        try:
            response = requests.head(check_Donationalerts)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Donationalerts: account found! " + check_Donationalerts)
                file.write("Donationalerts:" + check_Donationalerts + "\n")
            if response.status_code == 404:
                print(Fore.YELLOW + "[-] Donationalerts: account not found!")
            if response.status_code == 301:
                print(Fore.YELLOW + "[d] Donationalerts: account deleted!")
            if response.status_code == 403:
                print(Fore.RED + "[x] Donationalerts: access is denied!")

        except requests.ConnectionError:
            print(Fore.RED + "[e] Donationalerts: an error has occurred!")

        file.close()

        print(Fore.CYAN + "\n[\] All found accounts are saved:")
        print(Fore.CYAN + f"[\] cache\\{self.args}.txt")

userfidner = userFidner()
userfidner.Finder()
