import re, sys, threading, time
# Iran-Cyber.Net
try:
    import requests
except ImportError:
    print '---------------------------------------------------'
    print '[*] pip install requests'
    print '   [-] you need to install requests Module'
    sys.exit()

try:
    PROXYx = open(sys.argv[1], 'r').read().splitlines()
    url = sys.argv[2]
except:
    print('\n\n-----------------------------------------------------')
    print('usage: python {} proxy.txt linkPost'.format(sys.argv[0]))
    sys.exit()
thread = []
if url.startswith('http://'):
    url = url.replace('http://', '')
elif url.startswith('https://'):
    url = url.replace('https://', '')
else:
    pass

def StartSeen(url, PROXY):
    sess = requests.session()
    sess.proxies = {'http': PROXY, 'https': PROXY}
    agent = 'Mozilla/5.1 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)' \
                                    ' Chrome/58.1.3029.110 Safari/537.36'
    try:
        getz = sess.get('http://httpbin.org/html', timeout=10, headers={'User-Agent': agent}).text
        if 'Herman Melville - Moby-Dick' in getz:
            headersx = {'User-Agent': agent}
            aa2 = sess.get('http://' + url + '?embed=1', timeout=10, headers=headersx)
            x = aa2.headers.get('Set-Cookie')
            if 'data-view="' in aa2.text.encode('utf-8'):
                headers = {'X-Requested-With': 'XMLHttpRequest',
                           'User-Agent': agent,
                           'Cookie': str(x).split(';')[0]}
                Getviwe = 'http://' + url + '?embed=1&view=' + re.findall('data-view="(.*)">', aa2.text.encode('utf-8'))[0]
                DoneRequest = sess.get(Getviwe, timeout=10, headers=headers)
                if 'true' in DoneRequest.text.encode('utf-8'):
                    print '{} --> Seen OK!'.format(PROXY)
                    with open('GoodProxy.txt', 'a') as XX:
                        XX.write(PROXY + '\n')
                else:
                    print '{} --> Seen No!'.format(PROXY)
                    with open('SeenNoProxy.txt', 'a') as XX:
                        XX.write(PROXY + '\n')
            else:
                print '{} --> Cant Get data-view'.format(PROXY)
                with open('cantGetDAta-viewProxy.txt', 'a') as XX:
                    XX.write(PROXY + '\n')
        else:
            print '{} --> Proxy Not Work'.format(PROXY)
            with open('BadProxy.txt', 'a') as XX:
                XX.write(PROXY + '\n')
    except requests.exceptions.ReadTimeout:
        print '{} --> Proxy Time Out!'.format(PROXY)
        with open('BadProxy.txt', 'a') as XX:
            XX.write(PROXY + '\n')
    except requests.exceptions.ConnectionError:
        print '{} --> Connection aborted!'.format(PROXY)
        with open('BadProxy.txt', 'a') as XX:
            XX.write(PROXY + '\n')


for proxy in PROXYx:
    t = threading.Thread(target=StartSeen, args=(url, proxy))
    t.start()
    thread.append(t)
    time.sleep(0.08)
for j in thread:
    j.join()

