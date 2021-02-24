def bubble_sort(target_list: list) -> list:
    s = len(target_list) - 1  # リスト最後尾のインデックス番号を取得
    while s > 0:

        k = 0  # 先頭インデックスからループスタート
        while k < s:
            t = k + 1
            if target_list[k] < target_list[t]:
                # 入れ替え
                hold = target_list[k]
                target_list[k] = target_list[t]
                target_list[t] = hold
            k += 1

        s -= 1

    return target_list


target_list = [20, 30, 10, 40, 50]
res = bubble_sort(target_list)
print(res)
