#for문
#for 변수 in 변수 범위:
#       실행문

#예제1
for waiting_no in [0, 1, 2, 3, 4]:
    print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(5): #range(start, end) => start부터 end-1까지의 숫자열 생성 => 0,1,2,3,4  *(순차적으로 커질 경우 사용 용이)
    print("대기번호 : {0}".format(waiting_no))

#예제2
starbucks = ["아이언맨", "토르", "그루트"]
for customer in starbucks:
    print("{0}, 커피 준비되었습니다".format(customer))