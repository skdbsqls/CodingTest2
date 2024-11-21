# 1. 배열 선언
# 1) 일반적인 방법
arr = [0, 0, 0, 0,]
arr = [0] * 5
# 2) 리스트 생성자를 사용하는 방법
arr= list(range(5)) # [0, 1, 2, 3, 4]
# 3) 리스트 컴프리헨션을 활용하는 방법
arr = [0 for _ in range(5)]

# 2. 배열과 차원
# 2차원 배열
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(arr[1][2]) # 6
# 크기가 3 * 4인 리스트를 선언하는 예
arr = [[i]*4 for i in range(3)]
print(arr) # [[0, 0, 0, 0], [1, 1, 1, 1], [2, 2, 2, 2]]


# 3. 자주 활용하는 리스트 기법
# 1) 리스트에 데이터 추가
# append() 메서드
my_list = [1, 2, 3]
my_list.append(4) # [1, 2, 3, 4]
# + 연산자
my_list = [1, 2, 3]
my_list = my_list + [4, 5] # [1, 2, 3, 4, 5]
# insert()
my_list = [1, 2, 3]
my_list.insert(2, 999) # [1, 2, 999, 3]

# 2) 리스트에서 데이터 삭제
# del
my_list = [1, 2, 3, 4, 5]
del my_list[2]
print(my_list) # [1, 2, 4, 5]
# pop()
my_list = [1, 2, 3]
popped_element = my_list.pop(1) 
print(popped_element) # 2
print(my_list) # [1, 3]
# remove()
my_list = [1, 2, 3, 2, 4, 5]
my_list.remove(2)
print(my_list) # [1, 3, 2, 4, 5]

# 3) 리스트 슬라이싱
my_list = [1, 2, 3, 4, 5]
print(my_list[0:2]) # [1, 2]
print(my_list[1:]) # [2, 3, 4, 5]
print(my_list[3:4]) # [4]
print(my_list[-4:-2]) # [2, 3]

# 4) 리스트 컴프리헨션으로 데이터에 특정 연산 적용
numbers = [1, 2, 3, 4, 5]
squares = [num**2 for num in numbers]
print(numbers) # [1, 2, 3, 4, 5]
print(squares) # [1, 4, 9, 16, 25]


# 4. 이외 리스트 연관 메서드
colors = ["red", "orange", "yellow", "red", "blue", "yellow", "purple"]
print(len(colors)) # 7
print(colors.index("yellow")) # 2
colors.sort()
print(colors) # ['blue', 'orange', 'purple', 'red', 'red', 'yellow', 'yellow']
colors.sort(reverse=True)
print(colors) # ['yellow', 'yellow', 'red', 'red', 'purple', 'orange', 'blue']
print(colors.count("red")) # 2