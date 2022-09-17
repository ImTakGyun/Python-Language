from random import *
users = range(1, 21) #1부터 20까지 숫자를 생성
print(type(users))

#type이 range이므로 list로 변환
users = list(users)
print(type(users))
print(users)

#random 모듈의 함수 shuffle => 무작위로 섞음
shuffle(users)
print(users)

#random 모듈의 함수 sample => 해당 리스트에서 무작위로 원소 반환
winners = sample(users, 4)

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다 --")
