import sys, threading, time, re, random, os
try:
    import requests
except ImportError:
    print '---------------------------------------------------'
    print '[*] pip install requests'
    print '   [-] you need to install requests Module'
    sys.exit()

class BYpassSeenTelegram(object):
    def __init__(self):
        self.r = '\033[31m'
        self.g = '\033[32m'
        self.y = '\033[33m'
        self.b = '\033[34m'
        self.m = '\033[35m'
        self.c = '\033[36m'
        self.w = '\033[37m'
        self.rr = '\033[39m'
        self.cls()
        self.print_logo()
        self.main()
        self.seen = 0
        self.AllSeens = 0

    def print_logo(self):
        clear = "\x1b[0m"
        colors = [36, 32, 34, 35, 31, 37, 30, 33, 38, 39]

        x = """
                   _____                   _____           _           _   
                  / ____|                 |  __ \         (_)         | |  
                 | (___   ___  ___ _ __   | |__) | __ ___  _  ___  ___| |_ 
                  \___ \ / _ \/ _ \ '_ \  |  ___/ '__/ _ \| |/ _ \/ __| __|
                  ____) |  __/  __/ | | | | |   | | | (_) | |  __/ (__| |_ 
                 |_____/ \___|\___|_| |_| |_|   |_|  \___/| |\___|\___|\__|
                                                         _/ |              
                   Iran-Cyber.Net - github.com/04x      |__/               
                
    """
        for N, line in enumerate(x.split("\n")):
            sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
            time.sleep(0.01)

    def cls(self):
        linux = 'clear'
        windows = 'cls'
        os.system([linux, windows][os.name == 'nt'])

    def Run(self, PROXY, url):
        try:
            sess = requests.session()
            sess.proxies = {'http': PROXY}
            agent = 'Mozilla/5.' + str(1) + ' (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)' \
                                                   ' Chrome/58.' + str(1) + '.3029.110 Safari/537.36'
            headersx = {'User-Agent': agent}
            aa2 = sess.get('http://' + url + '?embed=1', timeout=5, headers=headersx)
            x = aa2.headers.get('Set-Cookie')
            if 'data-view="' in aa2.text.encode('utf-8'):
                headers = {'X-Requested-With': 'XMLHttpRequest',
                           'User-Agent': agent,
                           'Cookie': str(x).split(';')[0]}
                Getviwe = 'http://' + url + '?embed=1&view=' + re.findall('data-view="(.*)">', aa2.text.encode('utf-8'))[0]
                DoneRequest = sess.get(Getviwe, timeout=5, headers=headers)
                if 'true' in DoneRequest.text.encode('utf-8'):
                    pass
                else:
                    pass
            else:
                pass
        except:
            pass

    def main(self):
        try:
            fileproxy = sys.argv[1]
            viweAddress = sys.argv[2]
        except:
            self.cls()
            self.print_logo()
            print self.r + '  ---------------------------------------------------------------------------------------'
            print self.y + '     [-]' + self.c + ' usage :' + self.g \
                  + ' python GoTSeeN.py ListProxy.txt http://t.me/postlink'
            sys.exit()
        if viweAddress.startswith("http://"):
            viweAddress = viweAddress.replace("http://", "")
        elif viweAddress.startswith("https://"):
            viweAddress = viweAddress.replace("https://", "")
        else:
            pass
        with open(fileproxy, 'r') as x:
            prox = x.read().splitlines()

        print self.r + '     [+]' + self.g + ' Total Proxy Loaded! : ' + self.c + str(len(prox))
        thread = []
        try:
            x = requests.get('http://' + viweAddress + '?embed=1', timeout=5)
            GetSeenCount1 = re.findall('class="tgme_widget_message_views">(.*)</span>',
                                      x.text.encode('utf-8'))[0].split('<')[0]
        except:
            self.cls()
            self.print_logo()
            print self.r + '  ---------------------------------------------------------------------------------------'
            print self.y + '     [-]' + self.c + ' Check Internet connection! or Make Sure this url Is Valid!'
            sys.exit()
        time.sleep(1.5)
        print self.r + '     [+]' + self.g + ' Started Seen Proccess! Plase Wait.'
        for proxy in prox:
            t = threading.Thread(target=self.Run, args=(proxy, viweAddress))
            t.start()
            thread.append(t)
            time.sleep(0.02)
        for j in thread:
            j.join()
        try:
            x = requests.get('http://' + viweAddress + '?embed=1', timeout=5)
            GetSeenCount = re.findall('class="tgme_widget_message_views">(.*)</span>',
                                      x.text.encode('utf-8'))[0].split('<')[0]
            print self.r + '     [+]' + self.g + ' YouR post Got ' + self.y +\
                  str(int(GetSeenCount) - int(GetSeenCount1)) + self.g + ' Seen!'

        except:
            self.cls()
            self.print_logo()
            print self.r + '  ---------------------------------------------------------------------------------------'
            print self.y + '     [-]' + self.c + ' Check Internet connection! or Make Sure this url Is Valid!'
            sys.exit()

BYpassSeenTelegram()
