def get_lines(count: int) -> list:
    """
    get_lines は引数に与えられた値の行数だけ、標準入力を取得する
    :param count: 取得したい行数
    :return input_list: 取得した行数strのlist
    """

    lines = []
    for _ in range(count):
        line = input()
        lines.append(line)
    return lines


def get_lines_by_first_line() -> list:
    """
    get_lines_by_first_line は1行目に与えられた標準入力の値を行数として、2行目以降の標準入力を文字列のリストにして取得する
    :param: None
    :return lines:
    """

    count = int(input())
    return get_lines(count)


def cast_int_for_two_dimensional_list(str_list_in_list: list) -> list:
    """
    cast_int_for_two_dimensional_list は、文字列の入った二次元リストを数値の二次元リストにキャストする
    :param str_list_in_list: [[str, str, ...], [str, str, ...], ...]
    :return int_list_in_list: [[int, int, ...], [int, int, ...], ...]
    """

    int_list_in_list = []
    for row in str_list_in_list:
        row[:] = map(int, row)
        int_list_in_list.append(row)
    return int_list_in_list


def print_list(result_list: list) -> None:
    """
    print_list は任意の型のリストを、str型にキャストして、下記のように出力する
    ```
    1 2 3 4 5
    ```
    :param result_list: [any, any, ...]
    :return: None (print)
    """
    str_list = [str(i) for i in result_list]
    print(*str_list)


def print_two_dimensional_list(result_list_in_list):
    """
    print_two_dimensional_list は二次元配列をstr型にキャストして、下記のように出力する
    ```
    1 2 3
    4 5 6
    7 8 9
    ```
    :param result_list_in_list: [[any, any, ...], [any, any, ...], ...]
    :return: None (print)
    """
    for result_list in result_list_in_list:
        print_list(result_list)
