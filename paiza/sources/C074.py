# 不正解 なぜか半分ほど通過する

def get_lines(n):
    m = []
    for _ in range(n):
        line = input()
        m.append(line)
    return m


input_first_line = list(map(int, input().split()))
input_lines = get_lines(input_first_line[0])
s = ''.join(input_lines)

for i in range(input_first_line[1]):
    start = i * input_first_line[2]
    end = start + input_first_line[2]
    res = s[start:end]
    print(res)
