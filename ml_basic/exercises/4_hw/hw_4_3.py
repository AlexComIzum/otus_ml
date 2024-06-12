import math
from re import search
import re as re

A = "a"
B = "b"
C = "c"

PLUS = "+"
MINUS = "-"
EQUAL = "="
SPACE = " "

MULTIPLIER_TWO = "**"
MULTIPLIER_ONE = "*"

# определить с какого индекса читать начало полного выражение, если перед ним стоит знак "-"
def get_index_start(expr_str: str, operator: str):
    return expr_str.find(operator)

def handle_expr(str_expression_2: str, var_dict: dict):

    index_start = 0
    str_expression = str_expression_2.strip(SPACE)
    index_minus_tmp = str_expression.find(MINUS)
    index_plus_tmp = str_expression.find(PLUS)

    operator = PLUS

    if index_minus_tmp == 0:
        operator = MINUS
        index_start = get_index_start(str_expression, MINUS) + 1
        str_expression = str_expression[index_start:].strip(SPACE)

    if index_plus_tmp == 0:
        operator = PLUS
        index_start = get_index_start(str_expression, PLUS) + 1
        str_expression = str_expression[index_start:].strip(SPACE)

    index_start = 0

    index_plus = str_expression.find(PLUS)
    index_minus = str_expression.find(MINUS)
    index_equal = str_expression.find(EQUAL)

    is_end_expr = False
    index_end_expr = -1
    substr_expr = ""

    if index_minus > index_plus and index_plus != -1:
        substr_expr = str_expression[index_start:index_plus]
        index_end_expr = index_plus
    elif index_minus > index_plus and index_plus == -1:
        substr_expr = str_expression[index_start:index_minus]
        index_end_expr = index_minus
    elif index_minus == -1 and index_plus == -1 and index_equal != -1:
        substr_expr = str_expression[index_start:index_equal]
        isend_expr = True
    elif index_plus > index_minus and index_minus != -1:
        substr_expr = str_expression[index_start:index_minus]
        index_end_expr = index_minus
    elif index_plus > index_minus and index_minus == -1:
        substr_expr = str_expression[index_start:index_plus]
        index_end_expr = index_plus

    if not is_end_expr:

        var_dict = handle_part_expr(substr_expr, operator, var_dict)
        next_str_expression = str_expression[index_end_expr:]
        var_dict = handle_expr(next_str_expression, var_dict)
        substr_expr_clean = substr_expr.strip()
        # если переменная C не в конце
        if substr_expr_clean.isnumeric():
            if operator == MINUS:
                substr_expr_clean = operator + substr_expr_clean
            var_dict[C] = float(substr_expr_clean)

    else:
        substr_expr_clean = substr_expr.strip()

        if substr_expr_clean.isnumeric():
            if operator == MINUS:
                substr_expr_clean = operator + substr_expr_clean
            var_dict[C] = float(substr_expr_clean)
        else:
            var_dict = handle_part_expr(substr_expr, operator, var_dict)

    return var_dict

#берет единицу выражения с одной переменной и
# определяет тип переменной для дискриминанта и его коэффициент
def handle_part_expr(expr_part_str, operator,  var_dict):

    expr_str = expr_part_str.strip()
    index_dve_zvezd = expr_str.find(MULTIPLIER_TWO)
    index_odna_zvezd = expr_str.find(MULTIPLIER_ONE)
    key_str = C
    substr_expr = ""

    if index_dve_zvezd != -1:
        key_str = A
        substr_expr = expr_str[:index_dve_zvezd]

    elif index_odna_zvezd != -1:
        key_str = B
        substr_expr = expr_str[:index_odna_zvezd]

    if len(substr_expr) == 1 and substr_expr.isalpha():
        var_dict[key_str] = 1.0
    elif len(substr_expr) > 1:
        digit_str = ""
        for s_char in substr_expr:
            if s_char.isdigit():
                digit_str += s_char
        if len(digit_str) > 0 and digit_str.isdigit():
            if operator == MINUS:
                digit_str = operator + digit_str
            var_dict[key_str] = float(digit_str)

    return var_dict


def decide_equation(variable_dict):

    result = ""
    a_val = variable_dict.get(A, 1)
    b_val = variable_dict.get(B, 1)
    c_val = variable_dict.get(C, 1)

    discr = b_val ** 2 - 4 * a_val * c_val

    if discr > 0:
        x_1 = (-b_val + math.sqrt(discr)) / (2 * a_val)
        x_2 = (-b_val - math.sqrt(discr)) / (2 * a_val)
        result ="x_1 = %.2f \nx_2 = %.2f" % (x_1, x_2)
    elif discr == 0:
        x = - b_val / (2* a_val)
        result = str(x)
    else:
        result = "Корней нет"

    return result

expr_sentence = input()
#expr_sentence = "x**2 +  28 - 11*x= 0"
var_dict = {}
handle_expr(expr_sentence, var_dict)

print(f"2 var_dict = {var_dict}")

result = decide_equation(var_dict)
print(f"Результат:\n{result}")

