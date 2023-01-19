from builtins import object

try:
    import requests,ctypes,time,os,threading,platform,tqdm
    from colorama import Fore
    from time import sleep
    from tqdm import tqdm
    from alive_progress import alive_bar
except ImportError:
    input ("Error while importing modules. Please install the modules in requirements.txt")

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
print ("""
                                        |||||||||||||||||||||||||||||||||||||||
                                        | Wait some time to Load the Program! |
                                        |||||||||||||||||||||||||||||||||||||||
    """)
print (" ")

with alive_bar(1000, force_tty=True) as bar:
    for i in range(1000):
        time.sleep(.005)
        bar()
print("")
with alive_bar(1500, force_tty=True) as bar:
    for i in range(1500):
        time.sleep(.007)
        bar()
print('All packages was installed!')

time.sleep(2)

if platform.system() == "Windows":
    clear = "cls"
else:
    clear = "clear"


class usernames:

    def __init__(self):
        self.lock = threading.Lock ()
        self.checking = True
        self.usernames = []
        self.unavailable = 0
        self.available = 0
        self.counter = 0

    def update_title( self ):
        remaining = len (self.usernames) - (self.available + self.unavailable)
        ctypes.windll.kernel32.SetConsoleTitleW(
            f"BitCoin Miner Checker | Available: {self.available} | Unavailable: {self.unavailable} | Checked: {(self.available + self.unavailable)} | Remaining: {remaining} | Developed by @Zyxal-dev on Github")

    def safe_print(self,arg):
        self.lock.acquire()
        print (arg)
        self.lock.release()

    def print_console(self,status,arg,color=Fore.RED):
        self.safe_print (f"       {Fore.RED}[{color}{status}{Fore.RED}] {arg}")

    def check_username(self,username):
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
            elif r.status_code == 404:
                self.available += 0.001
                self.print_console ("Checking Bitcoins acc/id",username,Fore.GREEN)
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

    def load_usernames(self):
        if not os.path.exists ("usernames.txt"):
            self.print_console ("Console","File bitcoin.txt not found")
            time.sleep(10)
            os._exit(0)
        with open("usernames.txt","r",encoding="UTF-8") as f:
            for line in f.readlines():
                line = line.replace("\n","")
                self.usernames.append(line)
            if not len(self.usernames):
                self.print_console("Console","No username loaded in proxies.txt")
                time.sleep(10)
                os._exit(0)

    def main(self):
        os.system(clear)
        if clear == "cls":
            ctypes.windll.kernel32.SetConsoleTitleW("BitCoin Miner Checker | Developed by @Zyxal-dev on Github")
        print(Fore.RED + ascii_text)
        self.load_usernames()
        threads = int (input(f"       {Fore.YELLOW}[{Fore.RED}Console{Fore.YELLOW}] Threads: "))
        print()
        if threads >= 5:  # To prevent ratelimits
            threads = 5

        def thread_starter():
            self.check_username (self.usernames[self.counter])

        while self.checking:
            if threading.active_count() <= threads:
                try:
                    threading.Thread(target=thread_starter).start ()
                    self.counter += 1
                except:
                    pass
                if len(self.usernames) <= self.counter:
                    self.checking = None


object = usernames()
object.main()
input()