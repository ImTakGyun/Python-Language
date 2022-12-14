#함수 정의
def open_account():
    print("새로운 계좌가 생성되었습니다")

def deposit(balance, money): #입금
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money): #출금
    if balance >= money: # 잔액이 출금금액보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
        return balance

#함수 선언
open_account()

balance = 0 #잔액
balance = deposit(balance, 1000)
balance = withdraw(balance, 2000)
balance = withdraw(balance, 500)
print(balance)