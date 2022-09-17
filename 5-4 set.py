# 집합(set) => 중복X, 순서X
my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"]) #리스트를 set()를 통해 집합으로 변환

#교집합 (java와 python)
print(java & python)
print(java.intersection(python))

#합집합 (java 또는 python)
print(java | python)
print(java.union(python))

#차집합 (java - python)
print(java - python)
print(java.difference(python))

# 집합에 원소 추가
python.add("김태호")
print(python)

# 집합에서 원소 삭제
java.remove("김태호")
print(java)