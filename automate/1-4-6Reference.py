list,dictionary这些可变数据类型，使用reference
#############################################################################################
>>> spam = [0, 1, 2, 3, 4, 5] 
>>> cheese = spam      #sapm赋值给cheese
>>> cheese[1] = 'Hello!' #改变chesse里的值，按说spam不应该改变
>>> spam
[0, 'Hello!', 2, 3, 4, 5]  #可是spam改变了！这是因为存在变量里的不是list本身，而是reference，spam赋值给cheese的是reference，
                            spam和chesse这两个变量使用同一个reference
>>> cheese
[0, 'Hello!', 2, 3, 4, 5]
#############################################################################################
def eggs(someParameter): 
  someParameter.append('Hello')##2。增加someParameter（也就是spam的赋给的值）

spam = [1, 2, 3] 
eggs(spam)  ##1。调用了eggs（someParameter），然后spam的值赋给了someParameter
print(spam) ##3.按说spam是global 变量，打印出来是[1, 2, 3] ，但是他与someParameter使用相同的reference，所以被改变了
#############################################################################################
所以如果我们不想要改变spam的值，应该怎么办呢？
使用module copy 
function copy()（copy整个list）;deepcopy()（copy任意值）copy.deepcopy(spam[2])
#############################################################################################
import copy
def eggs(someParameter): 
  someParameter.append('Hello')

spam = [1, 2, 3] 
eggs(copy.copy(spam))###在这里使用copy（），把值赋给someParameter，而不是reference
print(spam)

结果：打印出来[1, 2, 3] ，而不是[1, 2, 3，‘Hello’] 



总结：
Variables do not store list values directly; they store references to lists.
