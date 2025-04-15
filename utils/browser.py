from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pathlib import Path
from time import sleep
import os

ROOT_DIR = Path(__file__).resolve().parent.parent
CHROMEDRIVER_PATH = ROOT_DIR / 'bin' / 'chromedriver.exe'


def make_chrom_browser(*options):
    chrome_options = webdriver.ChromeOptions()
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    if not os.environ.get('SELENIUM_HEADLESS'):
        chrome_options.add_argument('--headless')

    chrome_service = Service(executable_path=CHROMEDRIVER_PATH)
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
    return browser


if __name__ == '__main__':
    browser = make_chrom_browser('--headless')
    browser.get('http://google.com.br')
    sleep(3)
    browser.quit()
