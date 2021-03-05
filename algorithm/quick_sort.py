from typing import List
import random


def partition(number_list: List[int], low: int, high: int) -> int:
    i = low - 1
    pivot = number_list[high]
    for j in range(low, high):
        if number_list[j] <= pivot:
            i += 1
            number_list[i], number_list[j] = number_list[j], number_list[i]

    number_list[i + 1], number_list[high] = number_list[high], number_list[i + 1]
    return i + 1


def quick_sort(number_list: List[int]) -> List[int]:
    """
    計算量 ave: O(n log n), best: O(n log n), worst: O(n**2)
    非安定ソート
    隣同士の要素を比較し、大きい方を右に、小さい方を適切な位置までもっていく
    :param number_list:
    :return:
    """

    # 再帰処理
    def _quick_sort(number_list: List[int], low: int, high: int) -> None:
        if low < high:
            partition_idx = partition(number_list, low, high)
            _quick_sort(number_list, low, partition_idx - 1)
            _quick_sort(number_list, partition_idx + 1, high)

    _quick_sort(number_list, 0, len(number_list) - 1)
    return number_list


if __name__ == '__main__':
    numbers = [random.randint(10, 1000) for _ in range(10)]
    res = quick_sort(numbers)
    print(res)
