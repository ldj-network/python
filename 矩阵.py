#设A为m×n阶矩阵（即m行n列），第i 行j 列的元素是a(i,j)，即：A=a(i,j)
#定义A的转置为这样一个n×m阶矩阵B，满足B=a(j,i)，即 b (i,j)=a (j,i)（B的第i行第j列元素是A的第j行第i列元素），记A’=B
matrix = eval(input('输入矩阵（格式为 [[a11,a12],[a21,a22]] 以此类推）: \n'))
t_2 = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(t_2)