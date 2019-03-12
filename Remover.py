import shutil,os,urllib.request,glob
def internet_on():
    try:
        urllib.request.urlopen('http://216.58.192.142', timeout=1)
        return True
    except urllib.request.URLError as err:
        return False
if internet_on():
    # shutil.rmtree('/home/sam/Documents/Desktop/Pics/')
    # os.makedirs('/home/sam/Documents/Desktop/Pics/')
    files = glob.glob('/home/sam/Documents/Personal_Projects/DogDesktop/Pics/*')
    for f in files:
        os.remove(f)