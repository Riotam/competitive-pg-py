def get_lines_by_first_line():
    """
    get_lines_by_first_line は1行目に与えられた標準入力の値を行数として、2行目以降の標準入力を文字列のリストにして取得する
    :return: List[List[str]]
    """
    n = int(input())
    m = []
    for _ in range(n):
        line = input().split()
        m.append(line)
    return m


def cast_int_for_two_dimensional_list(m):
    """
    cast_int_for_two_dimensional_list は、文字列の入った二次元リストを数値の二次元リストにキャストする
    :param m: List[List[str]]
    :return: List[List[int]]
    """
    m_int = []
    for row in m:
        row[:] = map(int, row)
        m_int.append(row)
    return m_int


def print_two_dimensional_list(lines):
    """
    print_two_dimensional_list は二次元配列を出力する
    :param lines: List[List[any]]
    :return: None (print)
    """
    for line in lines:
        line = map(str, line)
        print(' '.join(line))
