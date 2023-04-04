#!/usr/bin/python3
#1.将字符串hello_world_I_am_a_students_who_are_about_to_graduate中的单词分割出来，保存在一个list类型的变量里面
str = "hello_world_I_am_a_students_who_are_about_to_graduate"
list = str.split("_")
print (type(list))         # 以空格为分隔符

#2.将题目1中的分割得到的list中的单词，按照英文格式打印出来
# 打印结果：hello world I am a students who are about to graduate.
# 提示：使用python内置函数join实现

add = " "
print(add.join(list))

# 3.找出单词 “welcome” 在字符串“Hello, welcome to my world.” 中出现的位置，找不到返回 -1。
# 提示：python的string类支持大量的函数，可供我们分析字符串
str1 = "Hello, welcome to my world."
str2 = "welcome"
print(str1.find(str2))

# 4.统计字符串“Hello, welcome to my world. I wish you happiness.” 中字母 w 出现的次数
str3 = "Hello, welcome to my world. I wish you happiness."
sub = 'w'
print("str3.count('w'):",str3.count(sub))



# 5.把welcome这个单词的首字母转成大写，并打印出来。
str4 = "welcome"
print(str4.capitalize())

# 6.将字符串HELLO WORLD转换成小写。

str5 = "HELLO WORLD"
print(str5.lower())




