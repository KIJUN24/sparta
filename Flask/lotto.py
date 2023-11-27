import random

def generate_lotto_numbers():
    # 1부터 45까지의 숫자 중에서 6개를 무작위로 선택
    lotto_numbers = random.sample(range(1, 46), 6)
    lotto_numbers.sort()  # 번호를 정렬하여 출력

    return lotto_numbers

if __name__ == "__main__":
    recommended_numbers = generate_lotto_numbers()
    print("로또 추천 번호:", recommended_numbers)

from collections import Counter

def count_common_elements(list1, list2):
    # Counter를 사용하여 각 리스트의 요소 개수를 세기
    counter1 = Counter(list1)
    counter2 = Counter(list2)

    # 두 리스트에서 공통된 요소의 개수 세기
    common_elements_count = sum((counter1 & counter2).values())

    return common_elements_count

if __name__ == "__main__":
    # 두 리스트 예시
    list1 = [1, 2, 2, 3, 4, 5]
    list2 = [2, 3, 3, 4, 5, 5]

    # 공통된 요소의 개수 출력
    result = count_common_elements(list1, list2)
    print("두 리스트에서 공통된 요소의 개수:", result)