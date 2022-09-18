#continue => 해당 반복을 건너뜀 (건너뛰고 이어서)
#break => 해당 반복에서 프로그램 자체를 종료해버림 (중단)

absent = [2, 5]  #결석
no_book = [7]    #책 소지X

for student in range(1, 11): # 1,2,3,4,5,6,7,8,9,10
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))