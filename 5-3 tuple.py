#튜플 => list와는 달리 내용 변경이나 추가가 불가능 but 속도가 더 빠름(변경되지 않는 목록에 사용)
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

#menu.add("생선까스") => tuple에서는 add 기능 제공X

(name, age, hobby) = ("김종국", 20, "운동")
print(name)
print(name, age, hobby)
