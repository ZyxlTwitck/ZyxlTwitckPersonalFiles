try:
    import requests, ctypes, time, os, threading, platform, colorama, math, phonenumbers
    from colorama import Fore
    from test import number
except ImportError:
    input ("If you not install the requirements.txt -- Will not work! [ *Press enter to start* ]:")

ascii_text = """
 ________      ___    ___      ________      ___    ___ ___    ___ ________  ___          
|\   __  \    |\  \  /  /|    |\_____  \    |\  \  /  /|\  \  /  /|\   __  \|\  \         
\ \  \|\ /_   \ \  \/  / /     \|___/  /|   \ \  \/  / | \  \/  / | \  \|\  \ \  \        
 \ \   __  \   \ \    / /          /  / /    \ \    / / \ \    / / \ \   __  \ \  \       
  \ \  \|\  \   \/  /  /          /  /_/__    \/  /  /   /     \/   \ \  \ \  \ \  \_____  
   \ \_______\__/  / /           |\________\__/  / /    /  /\   \    \ \__\ \__\ \_______|
    \|_______|\___/ /             \|_______|\___/ /    /__/ /\ __\    \|__|\|__|\|_______|
             \|___|/                       \|___|/     |__|/ \|__|                        
  """

print (" ")
print ("Wait some time to Load the Program!")
print (" ")


# def progress_bar1 #
def progress_bar1( progress,total,color=colorama.Fore.YELLOW ):
    percent = 100 * (progress / float (total))
    bar = '█' * int (percent) + '-' * (100 - int (percent))
    print (color + f"\r|{bar}| {percent:.2f}%",end="\r")
    if progress == total:
        print (colorama.Fore.GREEN + f"\r|{bar}| {percent:.2f}%",end="\r")


# def progress_bar2 #
#def progress_bar2( progress,total,color=colorama.Fore.YELLOW ):
    #percent = 150 * (progress / float (total))
    #bar = '█' * int (percent) + '-' * (150 - int (percent))
    #print (color + f"\r|{bar}| {percent:.2f}%",end="\r")
    #if progress == total:
        #print (colorama.Fore.GREEN + f"\r|{bar}| {percent:.2f}%",end="\r")


numbers1 = [x * 5 for x in range (3000,3500)]
results1 = []

#numbers2 = {x * 5 for x in range (3000,3500)}
#results2 = []

# progress_bar1 #
progress_bar1 (0,len (numbers1))
for i,x in enumerate (numbers1):
    results1.append (math.factorial (x))
    progress_bar1 (i + 1,len (numbers1))

# progress_bar2 #
#progress_bar2 (0,len (numbers2))
#for i,x in enumerate (numbers2):
    #results2.append (math.factorial (x))
    #progress_bar2 (i + 1,len (numbers2))

print (colorama.Fore.RESET)

if platform.system () == "Windows":
    clear = "cls"
else:
    clear = "clear"
time.sleep (5)

# Getting location with phone number! #

#phone = input("Do you wanna get your location with number?: ")

#if phone == "yes":
   #from phonenumbers import geocoder
   #ch_nmber = phonenumbers.parse(number, "CH")
   #print(geocoder.description_for_number(ch_nmber, "en"))

   #from phonenumbers import carrier
   #service_nmber = phonenumbers.parse(number, "R0")
   #print(carrier.name_for_number(service_nmber, "en"))
#else:
    #print ("Okay you don't wonna get your location with number. Okay let's start Mine!")

#time.sleep(5)

# Starting the Miner! #

class miner:

    def __init__( self ):
        self.lock = threading.Lock ()
        self.checking = True
        self.usernames = []
        self.unavailable = 0
        self.available = 0
        self.counter = 0


    def update_title( self ):
        remaining = len (self.usernames) - (self.available + self.unavailable)
        ctypes.windll.kernel32.SetConsoleTitleW (
            f"BitCoin Acc/Id Checker | Available: {self.available} | Unavailable: {self.unavailable} | Checked: {(self.available + self.unavailable)} | Remaining: {remaining} | Developed by @Zyxal-dev on Github")

    def safe_print( self,arg ):
        self.lock.acquire ()
        print (arg)
        self.lock.release ()

    def print_console( self,status,arg,color=Fore.RED ):
        self.safe_print (f"     {Fore.RED}[{color}{status}{Fore.RED}] {arg}")

    def check_username( self,username ):
        if username.isdigit ():
            self.unavailable += 1
            self.print_console ("Unavailable",username)
            return
        with requests.Session () as session:
            headers = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US",
                "content-type": "application/json"
            }
            r = session.head ("https://www.bitcoinminer.com/@{}".format (username),headers=headers)
            if r.status_code == 200:
                self.unavailable += 1
                self.print_console ("Unavailable",username)
                time.sleep(3)
            elif r.status_code == 404:
                self.available += 0.001
                self.print_console ("Cheking Bitcoins acc/id",username,Fore.GREEN)
                with open ("Available.txt","a") as f:
                    f.write (username + "\n")
            self.update_title ()
        # Search unvailable username_code #
            self.unavailable += 10
            if r.status_code == 200:
                time.sleep(2)
                self.unavailable -= 4
            with open ("Unavailable.txt", "a") as f:
                f.write(username + "\n")
            self.update_title()

    def load_usernames( self ):
        if not os.path.exists ("usernames.txt"):
            self.print_console ("Console","File usernames.txt not found")
            time.sleep (10)
            os._exit (0)
        with open ("usernames.txt","r",encoding="UTF-8") as f:
            for line in f.readlines ():
                line = line.replace ("\n","")
                self.usernames.append (line)
        if not len (self.usernames):
            self.print_console ("Console","No usernames loaded in proxies.txt")
            time.sleep (10)
            os._exit(0)

    def main(self):
        os.system (clear)
        if clear == "cls":
            ctypes.windll.kernel32.SetConsoleTitleW ("BitCoin Miner Checker | Developed by @Zyxal-dev on Github")
        print (Fore.RED + ascii_text)
        self.load_usernames ()
        threads = int (input (f"       {Fore.YELLOW}[{Fore.RED}Console{Fore.YELLOW}] Threads: "))
        print ()
        if threads >= 5:  # To prevent ratelimits
            threads = 5  # if threads >= 5 then = 5

        def thread_starter():
            self.check_username (self.usernames[self.counter])

        while self.checking:
            if threading.active_count () <= threads:
                try:
                    threading.Thread (target=thread_starter).start ()
                    self.counter += 1
                except:
                    pass
                if len (self.usernames) <= self.counter:
                    self.checking = None


object = miner()
object.main()
input()