# # 8.判断给定的字符串中是否包含单词某个单词，包含返回 True，不包含返回 False。
# str1 = input("字符串：")
# str2 = input("单词：")
# if(str2 in str1):
#     print(True)
# else:
#     print(False)

# 9.从 0 开始计数，输出指定字符串 A = “hello”在字符串
# B = “hi how are you hello world, hello yoyo!”中最后出现的位置，如果 B 中不包含 A，则输出 -1。
# A = "hello"
# B = "hi how are you hello world, hello yoyo!"
# print (B.rfind(A))

# def last_position():
#     dest_str = "hi how are you hello world, hello yoyo!"
#     start_ps = -1
#     while True:
#         ps = dest_str.find("hello",start_ps+1)
#         if ps  == -1:
#             break
#         start_ps = ps
#     return  start_ps
# print(last_position())


# 10.给定一个数 a，判断一个数字是否为奇数或偶数。
# a = int(input("请输入数字："))
# if a <= 0:
#     print(a,"既不是奇数也不是偶数")
# elif a % 2 == 0:
#     print(a,"是偶数")
# elif a % 2 == 1:
#     print(a,"是奇数")
# # input("点击enter键退出")

# def even_judgement(target_int):
#     input("请输入一个数字：")
#     if target_int % 2 == 0:
#         print("input number is a even number")
#     else:
#         print("input number is a not even number")

# 11.输入一个姓名，判断是否姓王。
# 提示：使用python内置函数input
# user = input("请输入您的姓名：")
# if user[0] == '王':
#     print("用户姓王")
# else:
#     print("用户不姓王")

# 12.写一个函数判断一个字符串是不是纯数字组成。
# str_num = input("输入数字：")
# print(str_num.isdecimal())

# 13.打印九九乘法表
# 打印结果应该是下面的样式：
# 提示：使用for循环和print函数实现
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('{}x{}={}\t'.format(j, i, i*j), end='')
#     print()

def print_multi_table():
    for i in range(1,10):
        for j in range(1,i + 1):
            multi_result = i * j
            print(f"{j}x{i}={multi_result}",end=" ")
        print()
print(print_multi_table())
