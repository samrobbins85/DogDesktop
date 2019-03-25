import requests, urllib.request,glob,os
url="Blank url lol"
def internet_on():
    try:
        urllib.request.urlopen('http://216.58.192.142', timeout=1)
        return True
    except urllib.request.URLError as err:
        return False
if internet_on():
    for f in glob.glob("*.(jpg|png)"):
        os.remove(f)
    while url[-3:] != ('jpg' or 'png'):
        link="http://www.reddit.com/r/rarepuppers/random.json"
        r=requests.get(link, headers = {'User-agent': 'your bot 0.1'})
        url=r.json()[0]['data']['children'][0]['data']['url']

    urllib.request.urlretrieve(url, '/home/sam/Documents/Personal_Projects/DogDesktop/Pics/'+str(url[url.rfind('/')+1:]))
