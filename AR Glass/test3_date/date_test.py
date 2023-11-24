from datetime import time, datetime

mystruct = time(10, 30, 0)

print(mystruct)
print(f'기차는 {mystruct.hour}시 {mystruct.minute}분에 떠난다.')

time = datetime(2023, 10, 27, 11, 00)
print(time)


now = datetime.now()

print(now)
print(f'지금은 {now.month}월 {now.day}일 {now.hour}시 {now.minute}분 입니다.')
print(now.strftime('%Y %h.%d %p %I:%M'))
# %Y : 4자리 년도
# %h : 월
# %d : 일
# %p : am/pm
# %I : 시
# $M : 분


