import gzip
import shutil


from selenium import webdriver
from selenium_stealth import stealth

chrome = None

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
    __init()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = "/tmp/chrome/chrome"
    for arg in ARGUMENTS:
        chrome_options.add_argument(arg)
    chrome = webdriver.Chrome("/opt/bin/chromedriver", options=chrome_options)

def getDriver():
    return chrome


def __init():
    shutil.copytree('/opt/google/chrome','/tmp/chrome')
    __unzip('/tmp/chrome/chrome.gz','/tmp/chrome/chrome')

def __unzip(source, target):
    with gzip.open(source, 'rb') as f_in:
        with open(target, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

__import__()
