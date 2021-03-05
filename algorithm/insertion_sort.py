from typing import List
import random


def insertion_sort(number_list: List[int]) -> List[int]:
    """
    計算量 ave: O(n**2), best: O(n), worst: O(n**2)
    安定ソート
    隣同士の要素を比較し、大きい方を右に、小さい方を適切な位置までもっていく
    :param number_list:
    :return:
    """

    for i in range(1, len(number_list)):

        temp = number_list[i]
        j = i - 1

        while j >= 0 and number_list[j] > temp:
            number_list[j + 1] = number_list[j]
            j -= 1

        number_list[j + 1] = temp

    return number_list


if __name__ == '__main__':
    numbers = [random.randint(10, 1000) for _ in range(10)]
    res = insertion_sort(numbers)
    print(res)
