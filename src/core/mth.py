# import sympy as sp
from sympy import parse_expr, Eq, symbols, And, solve, simplify
from typing import List, Dict, Any, Optional, Union, Tuple
import re

from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication, convert_xor


def help1():
    func = {"平方根":"sqrt()","a的n次方根":"root(a,n)","阶乘":"factorial()","正弦函数":"sin()","余弦函数":"cos()","正切函数":"tan()","余切函数":"cot()","正割函数":"sec()","余割函数":"csc()","反正弦":"asin()","反余弦":"acos()","反正切":"atan()","反余切":"acot()","反正割":"asec()","反余割":"acsc()","sinc函数":"sinc()","指数运算":"exp()","以n为底的对数":"log(var, n)","自然对数":"ln(x)或log(x)"}
    out = "帮助\n方程组输入格式为: 方程1,方程2,...\n\n函数列表:\n"
    for i in range(len(func)):
        out = out + str(list(func.keys())[i]) + "\t\t  " + str(list(func.values())[i]) + "\n"
    return out
def solve_equation(
        eq_str: str,
        unknowns: Optional[str] = None,
        allow_complex: Optional[bool] = None,
        allow_negative: Optional[bool] = None,
        allow_integer: Optional[bool] = None,
        constraints: Optional[str] = None
) -> Union[Dict, List, None]:
    """
    解方程或方程组的函数，支持约束条件

    参数:
    eq_str: 方程或方程组的字符串，多个方程用逗号分隔
    unknowns: 未知数字符串，多个未知数用逗号分隔，如果为None则自动识别
    allow_complex: 是否允许复数解，None表示自动
    allow_negative: 是否允许负数解，None表示自动
    allow_integer: 是否要求整数解，None表示自动
    constraints: 约束条件字符串，如 "0<x<100" 或 "0<=x<=100,0<y<100" 或 "x<y"

    返回:
    方程的解，如果无解则返回None
    """

    # 预处理方程字符串：替换^为**，并添加括号以确保正确解析
    eq_str = eq_str.replace('^', '**')

    # 定义转换规则
    transformations = standard_transformations + (implicit_multiplication, convert_xor)

    # 分割方程字符串（如果有多个方程）
    eq_parts = [part.strip() for part in eq_str.split(',')]

    # 解析方程
    equations = []
    for part in eq_parts:

        if '=' in part:
            left, right = part.split('=', 1)
            left_expr = parse_expr(left.strip(), transformations=transformations)
            right_expr = parse_expr(right.strip(), transformations=transformations)
            equations.append(Eq(left_expr, right_expr))
        else:
            # 如果没有等号，假设方程为表达式=0
            expr = parse_expr(part.strip(), transformations=transformations)
            equations.append(Eq(expr, 0))

    # 确定未知数
    if unknowns is None:
        # 自动识别未知数：收集所有表达式中的自由符号
        all_symbols = set()
        for eq in equations:
            all_symbols.update(eq.free_symbols)
        unknown_symbols = list(all_symbols)
    else:
        # 使用用户提供的未知数
        unknown_names = [name.strip() for name in unknowns.split(',')]
        unknown_symbols = symbols(unknown_names)

    # 解析约束条件
    constraint_exprs = []
    if constraints:
        # 分割多个约束条件
        constraint_parts = [part.strip() for part in constraints.split(',')]

        for constraint in constraint_parts:
            # 处理范围约束 (如 0<x<100)
            range_match = re.match(r'(.+?)([<>=]+)(.+?)([<>=]+)(.+)', constraint)
            if range_match:
                left_expr, op1, mid_expr, op2, right_expr = range_match.groups()

                # 解析表达式
                left_val = parse_expr(left_expr, transformations=transformations)
                mid_val = parse_expr(mid_expr, transformations=transformations)
                right_val = parse_expr(right_expr, transformations=transformations)

                # 创建两个不等式
                if op1 in ['<', '<=']:
                    constraint_exprs.append(And(mid_val > left_val if op1 == '<' else mid_val >= left_val,
                                                   mid_val < right_val if op2 == '<' else mid_val <= right_val))
                else:
                    # 处理其他情况，如 x>0<y (这种情况较少见)
                    constraint_exprs.append(parse_expr(constraint, transformations=transformations))
            else:
                # 处理简单约束 (如 x<y)
                constraint_exprs.append(parse_expr(constraint, transformations=transformations))

    # 解决方程
    solutions = solve(equations, unknown_symbols, dict=True)

    # 如果没有解
    if not solutions:
        return None

    # 应用约束条件
    if constraint_exprs:
        constrained_solutions = []
        for sol in solutions:
            # 检查解是否满足所有约束条件
            satisfies_all = True
            for constr in constraint_exprs:
                # 将解代入约束条件
                substituted_constr = constr.subs(sol)
                # 尝试简化并检查是否为真
                try:
                    # 尝试数值计算
                    if not substituted_constr:
                        satisfies_all = False
                        break
                except:
                    # 如果无法直接计算，尝试符号简化
                    simplified = simplify(substituted_constr)
                    if simplified == False:
                        satisfies_all = False
                        break

            if satisfies_all:
                constrained_solutions.append(sol)

        solutions = constrained_solutions

    # 如果没有满足约束的解
    if not solutions:
        return None

    # 过滤解
    filtered_solutions = []
    for sol in solutions:
        valid = True

        # 检查每个解的条件
        for var, value in sol.items():
            # 检查复数条件
            if allow_complex is False and not value.is_real:
                valid = False
                break

            # 检查负数条件
            if allow_negative is False and value.is_real and value < 0:
                valid = False
                break

            # 检查整数条件
            if allow_integer is True and value.is_real and not value.is_integer:
                valid = False
                break

        if valid:
            filtered_solutions.append(sol)

    # 如果没有满足条件的解
    if not filtered_solutions:
        return None

    # 如果只有一个解，返回字典；如果有多个解，返回列表
    return filtered_solutions[0] if len(filtered_solutions) == 1 else filtered_solutions