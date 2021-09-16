#coding=utf-8

api_list = [('/api/api_list','[["duplicate_id", "update_time", "protocol", "online_status", "pii_type", "api_manager", "match_sub_path", "host", "port", "group_name", "auto_tag", "method", "api_name", "api_max_body_args_cnt", "enable_args", "api_max_body_size", "api_max_query_args_cnt", "manual_tags", "path", "group_id", "id"], ["51d306b4f61ca1327827f009734f10a26bc594c0", 1623303713, "ANY", false, "", "", false, "172.16.30.4", 80, "BANK", "", "ANY", "login", 1, true, -1, -1, ["\\u767b\\u5f55"], "/doLogin", "85573ffff8c6bfb8b635d979296665319bedab70", "b4d3388be3fac4879a63c9dddbd49471fbb4b355"]]')]
# print api_list

data = {}
[data.update({k: v}) for k, v in api_list]
# print data
for k, v in api_list:
    print('===k==' * 40)
    print(k)
    print('===v==' * 40)
    print(v)

test_tuple = [('aaaa', 'bbbbb')]
for k, v in test_tuple:
    print('****##k###****' * 40)
    print(k)
    print('****###v###****' * 40)
    print(v)

# test_list = ['aaaa', 123, 'bbbbb']
# for k, v in test_list:
#     print('****k****' * 40)
#     print(k)
#     print('****v****' * 40)
#     print(v)

listA = [('Mon', 3), ('Tue', 1), ('Mon', 2), ('Wed', 3)]
for k, v in listA:
    print('～～～～～k～～～～' * 40)
    print(k)
    print('～～～～～v～～～～' * 40)
    print(v)

data = {}
[data.update({k: v}) for k, v in [('name', 'zhangsan'), ('age', 'zhangsan')]]
print(data)
