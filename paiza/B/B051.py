import numpy as np

import utils

m_str = utils.get_lines_by_first_line()
m = utils.cast_int_for_two_dimensional_list(m_str)

# 各行の合計を調べ、最大値をtotalに代入
total = max(np.sum(m, axis=0))

for m_line in m:
    if total != sum(m_line) and m_line.count(0) == 1:
        m_line[m_line.index(0)] = total - sum(m_line)
    if total != sum(m_line) and m_line.count(0) == 2:
        target = m_line.index(0)
        x = np.sum(m, axis=0)
        m_line[m_line.index(0)] = total - x[m_line.index(0)]
        m_line[m_line.index(0, target)] = total - x[m_line.index(0, target)]

utils.print_two_dimensional_list(m)
