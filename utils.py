def get_lines(n):
    """
    get_lines は引数に与えられた値の行数だけ、標準入力を取得する
    :param n: int
    :return: List[List[str]]
    """
    m = []
    for _ in range(n):
        line = input()
        m.append(line)
    return m


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


def print_list(results):
    """
    print_list はリストを結合して一列の文字列にして下記のように出力する
    ```
    1 2 3 4 5
    ```
    :param results: List[any]
    :return: None (print)
    """
    list_str = [str(i) for i in results]
    print(' '.join(list_str))


def print_two_dimensional_list(lines):
    """
    print_two_dimensional_list は二次元配列を下記のように出力する
    ```
    1 2 3
    4 5 6
    7 8 9
    ```
    :param lines: List[List[any]]
    :return: None (print)
    """
    for line in lines:
        line = map(str, line)
        print(' '.join(line))
