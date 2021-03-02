from typing import List
import random


def bubble_sort(number_list: List[int]) -> List[int]:
    """
    計算量 ave: O(n**2), best: O(n), worst: O(n**2)
    安定ソート
    隣同士を比較して大きい方を右に移動 最も大きいものが右端に行く
    :param number_list:
    :return:
    """

    # limitを左にズラしていくループ
    for i in range(len(number_list) - 1):

        # 隣同士を比較、並び替えるループ
        for j in range(len(number_list) - 1 - i):

            # もし対象の要素が右隣の要素より大きければ並び替え
            if number_list[j] > number_list[j + 1]:
                number_list[j], number_list[j + 1] = number_list[j + 1], number_list[j]

    return number_list


if __name__ == '__main__':
    numbers = [random.randint(10, 1000) for i in range(10)]
    res = bubble_sort(numbers)
    print(res)
