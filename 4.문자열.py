#문자열

sentence = '나는 소년입니다.'
print(sentence)
sentence2 = '파이썬은 쉬워요.'
print(sentence2)
#여러줄을 포함하는 문자열 변수 생성 가능
sentence3 = '''나는 소년이고,
파이썬은 쉬워요.'''
print(sentence3) 

#슬라이싱

jumin =  "990120-1234567"

#문자열 슬라이싱 => [start, end] => start ~ (end-1)까지 반환
print("성별 : " + jumin[7])
print("년생 : " + jumin[0:2]) # index 0 ~ 1 까지
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6]) # 0 부터 5 까지의 index의 값 반환(처음부터 가져올 경우 시작 index번호 생략 가능)
print("뒤 7자리 : " + jumin[7:]) # 7 부터 끝까지의 index의 값 반환(끝까지 가져올 경우 끝자리 index번호 생략 가능)
print("뒤 7자리(뒤에서부터) : " + jumin[-7:]) # 끝의 index번호를 -1로하여 지칭 가능

#문자열 처리 함수

python = "python is Amazing"
print(python.lower()) 