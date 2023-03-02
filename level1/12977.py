def solution(nums):
    import itertools
    answer = 0

    # 주어진 nums 배열에서 3개 원소를 선택하는 모든 조합을 만듭니다.
    # combinations 함수는 중복되지 않은 순서쌍을 반환합니다.
    sum_list = [sum(i) for i in list(itertools.combinations(nums, 3))]

    # 중복된 합을 제거합니다.
    # set 함수는 중복을 허용하지 않는 집합으로 만들어줍니다.
    # list 함수를 이용해 리스트로 변환합니다.
    # sum_list = list(set(sum_list))
        
    # 가능한 최대 소수를 찾기 위해, 주어진 합계 중 가장 큰 수를 찾습니다.
    max_num = max(sum_list)

    # 소수를 찾기 위한 에라토스테네스의 체 알고리즘을 사용합니다.
    # 먼저, 모든 수를 소수로 가정한 후, 소수가 아닌 수를 제거해줍니다.
    # sieve 리스트의 인덱스는 각 수를, True와 False 값은 소수 여부를 나타냅니다.
    sieve = [True for _ in range(max_num+1)]
    sieve[0], sieve[1] = False, False
    
    for i in range(2, int(max_num ** 0.5)+1):
        for j in range(i+i, max_num+1, i):
            sieve[j] = False

    # number 리스트에 가능한 모든 소수를 저장합니다.
    number = [i for i in range(2, max_num+1) if sieve[i]]
                
    # 합이 소수인 경우 answer를 증가시킵니다.
    for i in sum_list:
        if i in number:
            answer += 1
    return answer
