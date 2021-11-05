import requests
from bs4 import BeautifulSoup
import re
from konlpy.tag import Kkma

kkma = Kkma()

#텍스트 정제(전처리)
def cleanText(readData):
    #텍스트에 포함되어 있는 특수 문자 제거
    text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', readData)
    return text

url = 'https://www.joongang.co.kr/article/25021311'

res = requests.get(url)

if res.status_code == 200:
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')

    c = soup.select('#container > section')

    content = cleanText(c[0].get_text(strip=True).replace('\n', '').replace('\xa0', '')).split(' ')

    for i in content:
        if i == '':
            continue
        print(kkma.morphs(i))

else :
    print(res.status_code)