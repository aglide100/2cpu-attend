import requests
import random
import os
from datetime import datetime
from urllib.parse import quote

url = "https://www.2cpu.co.kr/bbs/login_check.php"

id = os.environ.get('ID')
password = os.environ.get('PASSWORD')

payload = 'mb_id=' + id + '&mb_password=' + password

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}

session = requests.Session()

response = session.post(url, headers=headers, data=payload)

url = "https://www.2cpu.co.kr/plugin/attendance/attendance_update.php"

# 오늘 날짜
today = datetime.now().strftime('%Y-%m-%d')

# ?? 용도 모름
currentId = ''

# 묵찌빠
type = str(random.randint(1, 3))

# 출석체크 멘트
memo_options = [
    '장터는 하루에 1번만 들리겠습니다',
    '2CPU 최고!!',
    '주먹을 내고 져도 울지 않습니다.',
    '초성체와 이모티콘을 안쓰겠습니다',
    '안녕하세요 즐거운 하루 보내세요!!',
    '남자는 주먹을 냅니다.',
    '내가 멀낼까 궁금하지?'
]

selected_memo = random.choice(memo_options)

encoded_memo = quote(selected_memo.encode('euc-kr'))

payload = 's_date=' + today + '&at_type=' + type + '&at_memo=' + encoded_memo

print('payload : ' + payload)
response = session.post(url, headers=headers, data=payload)

print("\n")
print(response.text)
