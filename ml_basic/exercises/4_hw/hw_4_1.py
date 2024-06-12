SPACE = " "


def split_by_rank():
    value = input()
    ostatok = len(value) % 3

    return handle_value(value, ostatok)


def handle_value(value: str, prefix: int):
    index_step = 1
    result = ""

    if prefix == 0:
        prefix = -1

    for digit in value:

        print(digit)
        if prefix > 0:
            prefix -= 1
        elif prefix == 0:
            prefix -= 1
            result += SPACE
        result += digit

        if prefix == -1 and index_step == 3:
            result += SPACE
            index_step = 0

        if prefix == -1:
            index_step += 1

    return result


result_d = split_by_rank()
print(result_d)
