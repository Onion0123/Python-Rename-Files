# https://paste.ubuntu.com/p/rVyyQK8D5T/
# 批量修改文件名
import os

path = 'D:/xxx\\xxx\\xxx'  # 文件地址,'\'这个符号不要忘了转义，要输入两个
count = 0  # 可以自定义心得命名规则，可以用字符串
for file_name in os.listdir(path):  # os.listdir(path) 返回一个文件名列表
    if file_name[-3::] == 'jpg':  # 切片获取文件扩展名,[]里面的数字是原始文件的 后缀名的长度
        count += 1  # 件名新文控制
        new_name = str(count) + '.jpg'  # os.rename 的参数要写全文件路径
        os.rename(path + '/' + file_name, path + '/' + new_name)
