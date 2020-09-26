import numpy as np


def get_lines_for_int(n):
    """
    get_lines は引数に渡した数値行分だけリストにして取得する
    :param n: int
    :return: List[List[int]]
    """
    m = []
    for _ in range(n):
        list_str = input().split()
        list_int = []
        for s in list_str:
            list_int.append(int(s))
        m.append(list_int)
    return m


def print_two_dimensional_list(lines):
    """
    print_two_dimensional_list は二次元配列を出力する
    :param lines: List[List[any]]
    :return: None (print)
    """
    for line in lines:
        line = map(str, line)
        print(' '.join(line))


m = get_lines_for_int(int(input()))

total = 0
for m_line in m:
    total_line = sum(m_line)
    if total < total_line:
        total = total_line

for m_line in m:
    if total != sum(m_line) and m_line.count(0) == 1:
        m_line[m_line.index(0)] = total - sum(m_line)
    if total != sum(m_line) and m_line.count(0) == 2:
        target = m_line.index(0)
        x = np.sum(m, axis=0)
        m_line[m_line.index(0)] = total - x[m_line.index(0)]
        m_line[m_line.index(0, target)] = total - x[m_line.index(0, target)]

print_two_dimensional_list(m)
