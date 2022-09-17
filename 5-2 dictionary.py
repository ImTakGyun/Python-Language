#사전 => key 중복 허용X
cabinet = {3: '유재석', 100: '김태호'}
print(cabinet)
print(cabinet[3])
print(cabinet[100])

# #key를 통한 value 추출
print(cabinet.get(3))

#주의사항
#print(cabinet[5]) => 사전 자료형에 할당되지 않은 key를 []로 가져올 때 = 에러+중단
#print(cabinet.get(5)) => 사전 자료형에 할당되지 않은 key를 get()로 가져올 때 = None 반환
#print(cabinet.get(5, "사용가능")) => get을 통해 가져올 때 해당 key가 비어있다면 설정한 초기값으로 반환

#사전 자료형 안에서 key가 채워져 있는지 확인하는 방법
print(3 in cabinet) #True
print(5 in cabinet) #False

#string key
cabinet = {"A-3": "유재석", "B-100": "김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

#key의 value 변경 및 새로운 key-value생성 => 새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# key-value 삭제하기 => 퇴장한 손님
del cabinet["A-3"]
print(cabinet)

#key 들만 출력
print(cabinet.keys())

#value 들만 출력
print(cabinet.values())

#key, value 쌍으로 출력
print(cabinet.items())

#사전 자료형 모두 비우기 => 가게 폐점
cabinet.clear()
print(cabinet)
