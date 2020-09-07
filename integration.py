#积分
# -*- coding: UTF-8 -*-


'''
import types
def integration(func, a, b):
    if not isinstance(func,  types.FunctionType):
        raise Exception("func must be a function")
    if not isinstance(a, int) and not isinstance(a, float) and not isinstance(a, long):
        raise Exception("a must be a number")
    if not isinstance(b, int) and not isinstance(b, float) and not isinstance(b, long):
        raise Exception("b must be a number")
    if a > b:
        raise Exception("a must be smaller than b")
    n = 1000.
    step = (float(b) - float(a) + 1.) / n
    print(step)
    i = a
    total = 0.
    while i <= b and (i + step) <= b:
        print("i=" + i)
        temp = func(i)
        #print(temp * step)
        total += temp * step
        #total += func(i) * step
        i += step
    return total
   
def squar(x):
    return float(x) * float(x)     
    
if __name__ == "__main__":
    result = integration(squar, 2, 4)
    #result = squar(5)
    print(result)
'''

import math

#定义标准正态分布概率密度函数
def Normal_pdf(x):
    result = 1/math.sqrt(2*math.pi)*math.exp(-x*x/2)
    return result

#定义复合辛普森法求积分
def Simpson(func,a,b,eps=1e-10):
    '''
    :param func: 被积函数
    :param a: 积分下限
    :param b: 积分上限
    :param eps: 计算精度，默认为1e-10
    :return: 返回积分结果
    '''

    #定义一个字典，用来存储被积函数(x,f(x))，避免重复计算
    func_result_dict = {}

    def f(x):
        if func_result_dict.get(x) is None:
            r = func(x)
            func_result_dict[x] = r
        else:
            r = func_result_dict[x]
        return r

    #辛普森函数
    def Sn(a,b,n):
        '''
        :param a: 积分下限
        :param b: 积分上限
        :param n: 将区间[a,b]划为n等分
        :return: 返回积分结果
        '''
        sum_result = 0
        half_h = (b-a)/(2*n)
        for k in range(n):
            #k=0的时候，f(a+2kh)=f(a),后面需要再减去f(a)
            sum_result += 2*f(a+2*k*half_h)
            sum_result += 4 * f(a + (2 * k + 1) * half_h)
        sum_result = (sum_result+f(b)-f(a))*half_h/3
        return sum_result

    #依次计算S1,S2,S4,S8...当相邻的精度小于eps时退出循环，返回S4n的结果
    i = 1
    S2n = Sn(a,b,i)
    S4n = Sn(a,b,2*i)
    while abs(S4n-S2n) > eps:
        i += 1
        S2n = S4n
        S4n = Sn(a,b,2**i)
    return S4n

#定义泰勒级数求积分法
def Taylor(t,n=50):
    '''
    :param t: 积分上限
    :param n: 泰勒级数前n项和，默认50项，n=0,1,2...50
    :return: 返回积分结果
    '''
    sum_t = 0
    for i in range(n+1):
        s = (-1)**i*t**(2*i+1)/(math.factorial(i)*2**i*(2*i+1))
        sum_t += s

    return 0.5+1/math.sqrt(2*math.pi)*sum_t


def main():
    print('辛普森法计算结果：')
    print('负无穷到0.7:',Simpson(Normal_pdf,-20,0.7))
    print('[-1,1]：',Simpson(Normal_pdf,-1,1))
    print('泰勒级数法计算结果：')
    print('负无穷到0.7:',Taylor(0.7))
    print('[-1,1]：',Taylor(1)-Taylor(-1))
if __name__ == '__main__':
    main()
