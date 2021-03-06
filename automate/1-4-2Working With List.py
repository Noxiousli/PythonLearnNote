一、Using for Loops with Lists
使用for和range(len(somelist))来把一个list的索引浏览一遍
##########################################################################
for i in range(4): #range(4)是list-like value 被叫做sequences
      print(i)
for i in [0, 1, 2, 3]: 
      print(i)   
##########################################################################      
这两个程序一样，结果
0
1
2
3

>>> supplies = ['pens', 'staplers', 'flame-throwers', 'binders'] 
>>> for i in range(len(supplies)):
            print('Index ' + str(i) + ' in supplies is: ' + supplies[i])
Index 0 in supplies is: pens 
Index 1 in supplies is: staplers 
Index 2 in supplies is: flame-throwers 
Index 3 in supplies is: binders

二、The in and not in Operators
使用in和not in来检查某个value是否在某个list里面，结果为Boolean
##########################################################################
>>> 'howdy' in ['hello', 'hi', 'howdy', 'heyas'] 
True 
>>> spam = ['hello', 'hi', 'howdy', 'heyas'] 
>>> 'cat' in spam 
False 
>>> 'howdy' not in spam 
False 
>>> 'cat' not in spam 
True
##########################################################################

三、The Multiple Assignment Trick
把一个list里面的values赋值给几个变量
变量数量和value数量必须一致，不然会有ValueError
格式：变量名字 = list名字
##########################################################################
>>> cat = ['fat', 'black', 'loud'] 
>>> size = cat[0]
>>> color = cat[1]
>>> disposition = cat[2]
简化如下
>>> cat = ['fat', 'black', 'loud'] 
>>> size, color, disposition = cat


