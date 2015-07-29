#!/usr/bin/env python
#coding=utf-8

#实现加减乘除-无优先级，从左至右计算
def split_str_psmd(str):
    expression = []
    index_l = 0 #上次切割的索引
    index_r = 0 #遍历时当前的索引
    for s in str:
        if s in '+-*/': #遇到运算符开始执行切割
            expression.append(str[index_l:index_r]) #写入list
            index_l = index_r #上次切割索引前移
        index_r += 1 # 非运算符索引前移
    expression.append(str[index_l:])#切割后最后一部分写入list
    init_value = expression[0] #list第一个值无需计算，设为初始值
    #expression #['8', '/2', '+10', '+2', '*3', '-14'] 

    for num in range(1,len(expression)):
        init_value = calculate_list(init_value,expression[num]) #计算结果赋值给初始值，即左操作数
    return init_value

def split_str_ps(str):
    expression = []
    index_l = 0 #上次切割的索引
    index_r = 0 #遍历时当前的索引
    for s in str:
        if s in '+-': #遇到运算符开始执行切割
            expression.append(str[index_l:index_r]) #写入list
            expression.append(s)
            index_l = index_r + 1  #上次切割索引前移
        index_r += 1 # 非运算符索引前移
    expression.append(str[index_l:])#切割后最后一部分写入list
    return expression

def calculate_list(a,b):
    return operate_map[b[0]](int(a),int(b[1:]))

#定义词典 + - * / 符号为key，value为运算结果
operate_map = {
	'+' : lambda x,y : x+y,
	'-' : lambda x,y : x-y,
	'*' : lambda x,y : x*y,
	'/' : lambda x,y : x/y
}

if __name__ == '__main__':
    cal_str = raw_input("Enter an arithmetic express:")
    cal_list = split_str_ps(cal_str)
    exp = ''
    for item in cal_list:
        if "*" in item or '/' in item:
            exp = exp+str(split_str_psmd(item))
        else:
            exp = exp+str(item)
    print split_str_psmd(exp)

