# f12를 눌러 개발자 도구를 열고, ctrl+shift+c를 누른다음 원하는 부분을 선택하면, 해당 위치의 태그로 이동하게 됨

from bs4 import BeautifulSoup
from urllib.request import urlopen

response = urlopen("https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EA%B2%80%EC%83%89%EC%96%B4+%EC%88%9C%EC%9C%84")
soup = BeautifulSoup(response, 'html.parser')

i = 1
f = open("새파일.txt", 'w')

# tit라고 하는 부분은 계속 바뀔 수 있으니 원하는 위치의 태그를 정확히 확인할 것
for anchor in soup.select("span.tit"):
    data = (str(i) + "위 :" + anchor.get_text()) + "\n"
    i+=1
    f.write(data)
f.close()
print("저장이 완료되었습니다.")
