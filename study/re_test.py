# -*encoding:utf-8*-
import re

input_psd = input("请输入字符串:")
test_str = re.search(r"[^a-zA-Z_\-\d\.]", input_psd)  # re.search 扫描整个字符串并返回第一个成功的匹配

if test_str is None:
    print("没有没有真没有特殊字符")
else:
    print("只允许录入英文字母、数字、_、-、.")
    print("search到非法字符:{}".format(test_str[0]))

match_str = re.match(r"[^a-zA-Z_\-\d\.]", input_psd)  # re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none
if match_str is None:
    print("match failed")
else:
    print("只允许录入英文字母、数字、_、-、.")
    print("match到非法字符:{}".format(test_str[0]))


def read_file(fn):
    with open(fn, 'rb') as fp:
        return fp.read()


def save_file(fn, content):
    # print(content)
    with open(fn, 'wb') as fp:
        if type(content) == 'unicode':
            content = content.encode('utf-8')
        fp.write(content)


# value = read_file('ports.conf')
# print('before:{}'.format(value))
# ret = re.sub('^Listen 20147\n', '', value.decode(),
#              flags=re.DOTALL | re.MULTILINE)  # 替换value中符合'^Listen 20147\n'模式的字符串为空
# print('after:', ret)
# save_file('ports.conf', ret.encode('utf-8'))


def to_double(matched):
    # print(matched.group())
    value_ = int(matched.group())
    return str(value_ * 2)


ori_text = "price is 66 $"
sub = re.sub(r'\d+', to_double, ori_text)
# print('sub:', sub)


name_pattern = re.compile(r'^\w{1,64}$')
value_pattern = re.compile(r'^\d+[mM]$')
description_pattern = re.compile(r'.{0,50}$')
match_name = name_pattern.match(input_psd)
search_name = name_pattern.search(input_psd)

if match_name:
    print('name_pattern match:', match_name[0])
if search_name:
    print('name_pattern search:', search_name[0])


print('请输入字母数字.-_中文name')
name = input('input:')
test_str = re.search(r"[^a-zA-Z0-9\.\-_\u4e00-\u9ffc]", input_psd)  # re.search 扫描整个字符串并返回第一个成功的匹配
if test_str is None:
    print("合法的name")
else:
    print("只允许录入字母数字._-中文")
    print("search到非法字符:{}".format(test_str[0]))
