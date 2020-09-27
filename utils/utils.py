def get_lines_for_int():
    """
    get_lines_for_int は引数に渡した数値行分だけ数値のリストにして取得する
    :param n: int
    :return: List[List[int]]
    """
    n = int(input())
    m = []
    for _ in range(n):
        list_str = input().split()
        list_int = []
        for s in list_str:
            list_int.append(int(s))
        m.append(list_int)
    return m


def get_lines_for_str():
    """
    get_lines_for_str は引数に渡した数値行分だけ文字列のリストにして取得する
    :param n: int
    :return: List[List[str]]
    """
    n = int(input())
    m = []
    for _ in range(n):
        line = input().split()
        m.append(line)
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
