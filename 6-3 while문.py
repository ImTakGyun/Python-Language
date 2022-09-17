#while문 => 조건에 만족하면 반복

#예제1
customer = "토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비 되었습니다. {1}번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")

#while True:
#   실행문              => 무한루프

#예제2 => input을 통해 입력받은 값으로 반복 결정
customer = "토르"
person = ""

while person != customer :
    print("{0}, 커피가 준비되었습니다".format(customer))
    person = input("이름이 어떻게 되세요? ")