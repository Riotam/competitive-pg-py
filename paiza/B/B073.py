import math
import numpy

import utils

# 1行目を取得してmに代入
input_line_first = input().split()
m = int(input_line_first[1])

# 2行目を取得して、aというリストに代入
a_str = input().split()
a = [int(i) for i in a_str]

# 3行目以降を取得してsという2次元リストに代入
s_str = utils.get_lines_by_first_line()
s = utils.cast_int_for_two_dimensional_list(s_str)

for s_line in s:

    start = s_line[0]-1
    end = s_line[1]

    target_list = a[start:end]
    average = numpy.average(target_list)

    diff = 0
    if average < m:
        diff = math.ceil(m - average)

        for i, v in enumerate(a):
            if i in range(start, end):
                a[i] += diff

utils.print_list(a)
