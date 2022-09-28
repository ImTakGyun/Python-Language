#간단한 수식
print( 2 + 3 * 4) #14
print( (2+3) * 4) #20

number = 2 + 3 * 4 #14
number = number + 2 #16
number += 2 #18
print(number)

number%=5 #3
print(number)

#숫자 처리 함수

#절댓값 -> abs()
print(abs(-5))   # 절댓값 반환  => 5

#제곱값 -> pow()
print(pow(4,2 )) # 제곱값 반환 => 4^2 = 16

#최대,최소 -> max(), min()
print(max(5,12)) # 입력받은 값들 중 최댓값 반환 => 12
print(min(5,12)) # 입력받은 값들 중 최솟값 반환 => 5

#반올림 -> round()
print(round(3.14)) # 반올림 => 3
print(round(4.9))  # 5

# math 라이브러리를 통한 숫자 처리 함수
from math import * #math 라이브러리의 모든 기능을 가져다 쓴다는 의미
print(floor(4.99))  # 내림 => 4
print(ceil(3.14))   # 올림 => 4
print(sqrt(16))     #제곱근 => 4


#랜덤 함수(random 라이브러리 사용)

from random import *
#random() => 0.0 ~ 1.0 미만
print(random())             # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10)        # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random()*10))     # 0 ~ 10 미만의 임의의 양수값 생성
print(int(random()*10 + 1)) # 1 ~ 10 이하의 임의의 양수값 생성
print(int(random()*45) + 1) # 1 ~ 45 이하의 임의의 양수값 생성

#randrange() => start ~ (end-1) 까지의 숫자중 랜덤
print(randrange(1, 46)) # 1 ~ 46미만의 임의의 양수값 생성

#randint() => start ~ end 까지의 숫자중 랜덤
print(randint(1, 45))   # 1 ~ 45이하의 임의의 양수값 생성