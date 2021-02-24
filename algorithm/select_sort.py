def select_sort(target_list: list) -> list:
    s = 0
    while s < len(target_list) -1:
        max_index = s
        k = s + 1
        while k < len(target_list):
            if target_list[k] > target_list[max_index]:
                max_index = k
            k += 1
        # 最大値が既に先頭にあれば交換不要
        if s != max_index:
            # データの交換
            hold = target_list[max_index]
            target_list[max_index] = target_list[s]
            target_list[s] = hold
        s += 1

    return target_list

target_list = [20, 30, 10, 40, 50]
res = select_sort(target_list)
print(res)
