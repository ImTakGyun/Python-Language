# 연산자

print(1+1) 
print(3-2)
print(5*2)
print(6/3)

print(2**3) # '**'는 제곱을 의미 => 2^3 = 8
print(5%3) # '%'는 나머지 구하기 => 2
print(10//3) # '//'는 몫 구하기 => 3

print(10 > 3) #True
print(4>=7) #False

print(3 == 3) # '==' 동일 값 비교연산자 => True
print(3+4 == 7) #True
print(1 != 3) # 비교연산자 '!' => True
print(not(1 != 3)) # boolean값을 반대로 반환 => False

# and == & , or == |
print((3>0) and (3<5)) #True
print((3>0) & (3<5)) #True

print((3>0) or (3>5)) #True
print((3>0) | (3>5)) #True

# 3중 비교 가능
print(5>4>3) #True
print(5>4>7) #False