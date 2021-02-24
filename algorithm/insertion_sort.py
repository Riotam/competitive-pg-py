def insertion_sort(target_list: list) -> list:

    s = 1  # 先頭の要素は、既に処理済みからスタート
    while s < len(target_list):
        hold = target_list[s]

        k = s - 1  # 対象の要素の1つ前の要素から前は、既に処理済み
        # 対象の要素と処理済みの要素達を比べ、対象要素が大きければ入れ替え
        # また、対象要素が先頭になるとループから抜ける
        while target_list[k] < hold and k >= 0:
            # 入れ替え
            target_list[k + 1] = target_list[k]
            target_list[k] = hold

            k -= 1

        s += 1

    return target_list

target_list = [20, 30, 10, 40, 50]
res = insertion_sort(target_list)
print(res)
