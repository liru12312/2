#7.打印字符串gbgkkdehh中第 2 个只出现过 1 次的字符
# 输出结果：d
# str ="gbgkkdehh"
# counter = 0
# dict = []
# for char in str:
#     if 1 == str.count(char):
#         counter += 1
#         if counter == 2:
#             print(char)
#             break

target_str ="gbgkkdehh"
counter = 0
target_char = []
for char in target_str:
    if 1 == target_str.count(char):
        counter += 1
        target_char.append(char)
        if counter == 2:
            print("第 2 个只出现过 1 次的字符:",char)
print(*target_char)







