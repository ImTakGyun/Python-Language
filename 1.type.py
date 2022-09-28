#숫자형

print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)  #print 내부의 매개변수가 계산되어 실행
print(2*8)
print(3*(3+1))

#문자열

print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*7)   #문자에 사칙연산을 적용할 수 있음

#boolean

print(5>10)
print(5<10)
print(True)
print(False)
print(not True) # not은 뒤에 따라오는 boolean값의 반대를 반환
print(not False)
print(not (5>10))   # 사직연산의 결과인 boolean 값 print 가능

#변수

# '+' 를 포함한 문자열 출력문에서 정수와 boolean값을 출력하기 위해서는 str() 로 감싸줘야함
# ','로 변수와 문자열을 연결해줄 수 있지만 , 이후에는 무조건 한 칸을 띄어쓰게 됨 그리고 ','로 문자열을 출력할 경우 정수와 boolean값은 str() 필요X
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age>3    #조건문의 값으로 저장 가능

print("우리집 " + animal + "의 이름은 " + name + "이에요")
print(name + "는 " + str(age) + "살이며 " + hobby +"을 아주 좋아해요")  # +로 연결된 문자열 출력 => 정수나 boolean을 str()로 묶어줘야함
print(name,"는 어른일까요? ", is_adult) # ,로 연결된 문자열 출력 => 정수나 boolean을 str()로 묶을 필요 없음

# 주석

# '#'는 한 줄 주석
'''는 여러줄 주석'''
# 여러줄을 한번에 주석처리하기 => 여러줄 드래그 후 Ctrl + '/' (해지는 한 번 더 반복)
