import gzip
import shutil
import os


from selenium import webdriver
from selenium_stealth import stealth

ARGUMENTS = [
        '--headless',
        '--no-sandbox',
        '--disable-dev-shm-usage',
        '--disable-gpu',
        '--disable-dev-tools',
        '--no-zygote',
        '--single-process',
        'window-size=2560x1440',
        '--user-data-dir=/tmp/chrome-user-data',
        '--remote-debugging-port=9222'
]



def __import__():
    if 'chrome' in globals():
        return
    __init()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = "/tmp/chrome/chrome"
    for arg in ARGUMENTS:
        chrome_options.add_argument(arg)
    global chrome
    chrome = webdriver.Chrome("/opt/bin/chromedriver", options=chrome_options)

def getDriver():
    return chrome


def __init():
    if not os.path.isdir('/tmp/chrome'):
        shutil.copytree('/opt/google/chrome','/tmp/chrome')
    if not os.path.exists('/tmp/chrome/chrome'):
        __unzip('/tmp/chrome/chrome.gz','/tmp/chrome/chrome')
        os.chmod("/tmp/chrome/chrome", 755)

def __unzip(source, target):
    with gzip.open(source, 'rb') as f_in:
        with open(target, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

__import__()
