一、返回值#有句话，python只有名字没有变量，不理解，说是和其他语言的区别
return None或值
None比如print（）
二、函数作用域
1.局部变量
只能在函数里访问
在函数内部可以访问全局变量，但是修改的话，需要加global
例如
def a(x, y):
  global c #修改全局变量c
  c = 10
  print(10)
c = 7
2.全局变量
可以在整个程序里访问


二、内嵌函数（内部函数）
在一个函数里面再定义一个函数
内部函数只能在外部函数调用，在全局里面不可以调用

三、闭包
1.定义：内部函数引用外部函数的变量
2.内部函数可以应用外部函数变量，但是不可以直接修改，需要加nonlocal
def fun1():
    print('fun1()正在被调用...')
    def fun2():
        print('fun2()正在被调用...')
    return fun2

i = fun1()#fun1()的return值给了i，也就是fun2()
i = fun1()()#fun1()执行，然后返回fun2，第二个括号是调用fun2
##闭包##
def fun3(x):
    def fun4(y):
        print(x*y)
    return fun4
fun3(4)(6)

def fun3():
    x = 4
    def fun4():
        nonlocal x#修改外部函数的变量
        x *= x
        return x
    return fun4()#返回函数的值，和上面不一样，上面是返回函数
fun3()#不是fun3()(),思考下为什么呢

三、函数文档
写在函数开头部分，可以解释程序，方便别人理解代码。
def Dec2Bin(dec):
    '这款毛孔'#函数文档，通过函数名字.__doc__打印出来，只有放在第一行的才可以打印出来
    temp = []
    result = ''
    while dec:
        quo = dec % 2
        dec = dec // 2
        temp.append(quo)

    while temp:
        result += str(temp.pop())
    
    return result

print(Dec2Bin(62))

四、
>>> help(print)
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    # 文件类型对象，默认是sys.stdout（标准输出流）
    sep:   string inserted between values, default a space.
    # 第一个参数如果有多个值（第一个参数是收集参数），各个值之间默认用空格（space）隔开
    end:   string appended after the last value, default a newline.
    # 打印最后一个值之后默认参数一个新行标识符(‘\n’)
    flush: whether to forcibly flush the stream.
    # 是否强制刷新流
 五、匿名函数lambda#消除了匿名的烦恼
 lambda x : 2 + x -----创造了一个函数
 #######################################
 下面这个函数可以很好的理解lambda
 def make_repeat(n):
        return lambda s : s * n

double = make_repeat(2)#这一步，return 了一个匿名函数：lambda s:s*2
print(double(8))# 8是赋值给s的所以结果是16
print(double('FishC'))#结果 FishCFishC
#######################################
 
 1.BIF filter()过滤器#满足条件，就可以留下
 filter(条件，可迭代数据)#条件（函数或None【意思是删除0，保留非0】）
 例如：
 删除偶数，只留奇数
 a.先定义一个函数
 def a(x):
  return x%2==1
 b.确定要进行操作的可迭代数据[1,4,5,7]
 c.开始！
 list(filter(a,[1,4,5,7]))
 结果：[1,5,7]
 
 2.filter与lambda应用
 a.函数 lambda
 b.数据
 c.开始！
 list(filter(lambda x : x > 5, [1, 4, 6, 7]))
结果：[6，7]
 
 3.map()#操作猛如虎
 list(map(lambda x : x+2, range(3)))
 结果：[2,3,4]
 接下来。如果我们要用普通函数来操作：
 def a(x):
  return x + 2
 list(map(a, range(3)))
 相比较就很麻烦了
 
 六、递归
 python默认100层
 


