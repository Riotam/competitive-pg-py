from typing import List


def main(line: str) -> int:
    numbers: List[int] = list(map(int, line.split()))
    return numbers[0] // numbers[1]


if __name__ == '__main__':
    input_line = input()
    res = main(input_line)
    print(res)
