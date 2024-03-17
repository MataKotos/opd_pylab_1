from bs4 import BeautifulSoup
import requests
import os


def parse(url: str) -> list:
    os.environ['no_proxy'] = '127.0.0.1,localhost'
    fakeHeaders = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/109.0.0.0 Safari/537.36'}

    page = requests.get(url, headers=fakeHeaders, stream=True, verify=False)

    soup = BeautifulSoup(page.text, "html.parser")

    faculties = []
    root = soup.find('div', id='pagecontent').find('ul').find_all('li')
    for faculty in root:
        faculties.append(faculty.find('p').find('a').contents[0])

    return faculties
