def solution(numbers):
    numbers = sorted(numbers, reverse=True)
    
    return numbers[0]*numbers[1]