'''
문제 03. 두 개 뽑아서 더하기(*)

[문제 설명]
정수 배열 numbers가 주어집니다. 
numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.

[제약 조건]
- numbers의 길이는 2 이상 100 이하입니다.
- numbers의 모든 수는 0 이상 100 이하입니다.

[입출력 예]
numbers	        result
[2,1,3,4,1]	    [2,3,4,5,6,7]
[5,0,2,7]	    [2,5,7,9,12]
'''

def solution(numbers):
    ret = [] #빈 배열 생성
    
    #두 수를 선택하는 모든 경우의 수를 반복문으로 구함
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            #두 수를 더한 결과를 새로운 배열에 추가
            ret.append(numbers[i] + numbers[j])
    #중복된 값을 제거하고, 오름차순으로 정렬
    ret = sorted(set(ret))
    return ret