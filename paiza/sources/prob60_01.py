import utils

# 2行目以降の標準入力を一次元リストに変更し、str型をint型にキャスト
a_list = list(int(n) for n in sum(utils.get_lines_by_first_line(), []))

res = 0
for a in a_list:
    if a >= 5:
        res += a

print(res)
