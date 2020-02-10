# pyhton 沒有陣列
# () tuple --> 一但建立就無法新增,刪除,修改
# [] list
# {} set   --> 不可重複
# {key:value} dict
#################################
# 有支援utf-8編碼 中文可以當變數名稱
# 大小寫代表不同變數
# dir()
# dir(物件) 可以看有什麼屬性和方法
# dir('__builtin__') --> 看內建有哪些字

# 記憶體位置: 創了一個值後,後面有一樣值得變數未直接指向之前的
# pros 減少重複記憶體使用
# cons 執行效率會下降
x = 1
y = 1
print('x的記憶體位置:', id(x)) #--> 印記憶體位置
print('y的記憶體位置:', id(y)) #--> x, y會共用同一個記憶體位置
s = 'shango' # 如果還要執行 s[0] = 'W' -->  會報錯 object does not support item assignment
print('-----------')
################################# 
color = 0xffffff   # 16進位轉換
print(color)       #!!! 16777215 
j = 0.1+0.1+0.1    # 浮點數運算要小心
print(j)           #!!! 0.30000000000000004
k = False          # True/False 可以以 1/0表示
print(k == 0)      #!!!
print(k+1)         #!!! True/False 可以計算
print(True*3)         
print(k == bool({})) #!!! bool() ==>  0, '', {}, None, []都為False, 有值都為Ture
print(k == bool(None))
print('-----------')
################################# 
#複數的表示:使用大寫或小寫j  ???用在哪裡
complex = 3+6j
complex2 = (3+4j)*(4+3j) 
# 12 + 9j + 16j + 12j*2 
# 12 + 9j + 16j - 12
# j = 根號-1
# j*2 = -1
print(complex)
print(complex2)     #!!! 交叉相乘得25j
print(complex.real) #取得實部
print(complex.imag) #取得虛部
print('-----------')
#################################
#list 可以放不同型態的值
l = []
l = list()
list_count10 = [i for i in range(10)]
l = [10 , 20, ['a', 'b', 'c'], '太棒了']
l[2][1] = 'shango' # l = [10 , 20, ['a', 'shango', 'c'], '太棒了']
print(l[2][1])
l2 = l
l2[0] = -99.9      # l & l2的值都改變了, 原因是他們都指向同一個list
print(l[0])        #!!! l2 = l = #[-99.9 , 20, ['a', 'shango', 'c'], '太棒了']
print('-----------')
################################# 
#tuple --> 用在大型專案時,當成常數的集合??
str = ('shango')  #如果只有一個元素 不會當tuple
v = (1)         #如果只有一個元素 不會當tuple
t = ('shango',) #只想有一個元素又要是tuple就再加一個,
print(type(str), type(t), type(v))
#tuple 不能直接加東西
for i in list_count10:
    t += (i,)
print('1.創立一個1-10的tuple:',t)
t2 = (list_count10)
print('2.創立一個1-10的tuple:',t2)
s = 'abc'
print(tuple(s))
print('-----------')
#################################
#dict
dict = {
    'a':'dict1',
    'b':2,
    'c':['list'],
    'd':('shango',)
}
print(dict['d']) #使用[]取用
print(type(dict['d'])) #使用[]取用
print('-----------')
################################# 
s = {'shango', 'indra', 'agni'}
l = [1, 1, 2, 2, 2, 3]
print(set(l))           #!!!
print('indra' in s)     #!!!
print('-----------')
################################# 
#習題
list = [i%5==0 for i in range(50)]         #印出每個數字是否有被五整除的布林
print(list)
#印出五十以內五的倍數
list2 = [i for i in range(50) if i%5==0]   #印出五十以內 五的倍數
print(list2)

#印出123451234512345
list3 = [i%5+1 for i in range(15)]
print(list3) 

#印出111222333444555
list4 = [i+1 for i in range(5) for j in range(3)]
list4 = [i for i in range(1, 6) for j in range(3)]
print(list4)

#查ASCII code
o = {}
o['A'] = ord('A')
o['\n'] = ord('\n')
print(o)

l = ['A', '\n', 'i']
o = {}
for i in l:
    o[i] = ord(i) 
print(o)
print('-----------')
##################################

