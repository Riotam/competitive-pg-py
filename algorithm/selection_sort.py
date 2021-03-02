from typing import List
import random


def selection_sort(number_list: List[int]) -> List[int]:
    """
    計算量 ave: O(n**2), best: O(n**2), worst: O(n**2)
    安定ソート
    バブルソートの改良的存在
    各要素で最も小さいものを選択し、リストの左側と交換
    :param number_list:
    :return:
    """

    # startを移動させるループ
    for i in range(len(number_list) - 1):

        min_index = i

        # 最小の要素を探すループ
        for j in range(len(number_list) - i):

            # 暫定の最小値より対象要素が小さければ最小値を更新
            if number_list[j + i] < number_list[min_index]:
                min_index = j + i

        # 上記とは別の記述方法として、index値jをi+1でループスタートする方法もある
        # for j in range(i+1, len(numbers)):
        #     if number_list[min_index] > number_list[j]:
        #         min_index = j

        # 最小値を左端の要素と交換
        number_list[i], number_list[min_index] = number_list[min_index], number_list[i]

    return number_list


if __name__ == '__main__':
    numbers = [random.randint(10, 1000) for i in range(10)]
    res = selection_sort(numbers)
    print(res)
