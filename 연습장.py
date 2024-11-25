''' enumerate()
: 반복 가능한 객체(iterable)를 반복하면서 인덱스와 해당 요소를 함께 반환해주는 내장 함수

    enumerate(iterable, start=0)
    - iterable: 반복 가능한 객체 (예: 리스트, 튜플, 문자열, 딕셔너리 등)
    - start: 인덱스의 시작값을 지정하며 기본값은 0

1) enumerate()는 각 요소와 함께 해당 요소의 인덱스를 튜플 형태로 반환
2) 리스트, 문자열, 튜플, 딕셔너리, 집합 등 다양한 iterable에서 사용 가능
3) 인덱스와 값을 다루는 반복문을 구현할 때, 별도로 인덱스를 계산하거나 변수로 관리할 필요가 없음

[사용 사례]
1) 데이터와 인덱스를 동시에 관리해야 할 때
2) 리스트를 순회하며 특정 조건에 맞는 요소의 인덱스를 찾을 때
'''

fruits = ['apple', 'banana', 'cherry']

print(fruits) 
# ['apple', 'banana', 'cherry']

print(list(enumerate(fruits))) 
# [(0, 'apple'), (1, 'banana'), (2, 'cherry')]

for index, value in enumerate(fruits):
    print(index, value)
    
# 0 apple
# 1 banana
# 2 cherry

# start 매개변수 사용
for index, value in enumerate(fruits, start=1):
    print(index, value)

# 1 apple
# 2 banana
# 3 cherry

