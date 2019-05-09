import sys

# 输入
square_array = []
N = sys.stdin.readline().rstrip("\n")

for i in range(0, int(N)):
    row = []
    line = sys.stdin.readline().rstrip("\n")
    temp_str = line.split(" ")
    for str_ in temp_str:
        row.append(int(str_))
    square_array.append(row)

M = sys.stdin.readline().rstrip("\n")

# 旋转处理
L = int(N)
M = int(M) % 4
"""
# rotate_array = square_array.copy()        # 之前出错，存在二维列表的浅复制问题，一维不存在这个问题
rotate_array = [([0]*L) for i in range(L)]    # 为了避免这种情况，使用二维列表推导式
if M % 4 == 0:
    rotate_array = [item for item in square_array]

if M % 4 == 1:
    for row_ix in range(L):
        for col_ix in range(L):
            # 原矩阵逐列赋值给旋转矩阵的每一行
            rotate_array[row_ix][col_ix] = square_array[L-1-col_ix][row_ix]

if M % 4 == 2:
    for row_ix in range(L):
        for col_ix in range(L):
            # 原矩阵逐列赋值给旋转矩阵的每一行
            rotate_array[col_ix][row_ix] = square_array[L-1-col_ix][L-1-row_ix]

if M % 4 == 3:
    for row_ix in range(L):
        for col_ix in range(L):
            # 原矩阵逐列赋值给旋转矩阵的每一行
            rotate_array[row_ix][col_ix] = square_array[col_ix][L-1-row_ix]
"""


# 封装为函数，递归实现
def rotate_matrix(handled_array, order):
    rotate = [([0] * order) for _ in range(order)]
    for row_index in range(order):
        for col_index in range(order):
            # 原矩阵逐列赋值给旋转矩阵的每一行
            rotate[row_index][col_index] = handled_array[order-1-col_index][row_index]
    return rotate


rotate_array = [item for item in square_array]
for i in range(M):
    rotate_array = rotate_matrix(rotate_array, L)

# 输出
for row in rotate_array:
    row_str = ""
    for item in row:
        row_str += str(item) + " "
    print(row_str)

"""
题目描述
输入一个N阶方阵(0<N<10),输出此方阵顺时针旋转M(0<=M<=10000)次后的方阵
旋转举例：（如下四个三阶方阵从上到下为数字围绕中心顺时针旋转）
1 2 3
4 5 6
7 8 9

7 4 1
8 5 2
9 6 3

9 8 7
6 5 4
3 2 1

3 6 9
2 5 8
1 4 7
输入描述：
输入第一行一个正整数N (0<N<10)
接下来N行每行N个整数用空格分开，为方阵的数据
接下来一行一个正整数M (0<=M<=10000)
说明：不用考虑异常输入，所有输入都是正常的，严格遵从取值范围
输出描述：
N行，每行N个整数，用空格分开，为旋转后的数据
示例1
输入
3
1 2 3
4 5 6
7 8 9
2
输出
9 8 7
6 5 4
3 2 1
"""
