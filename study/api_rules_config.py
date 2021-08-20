# encoding:utf-8

import json

configs = {
    "enable": True,
    "id": 1,
    "rule_name": "规则一",
    "group_name": "default",
    "group_by_domain": True,
    "filter_conditions": [
        {
            "key": "hostname",
            "type": "string",
            # max 100
            "value": "10.10.10.10",
            # include start_with end_with regular_exp
            "operation": "include"
        },
        {
            "key": "port",
            "type": "number",
            # 1-65535
            "value": 8080,
            # > == <
            "operation": ">"
        },
        {
            "key": "path",
            "type": "string",
            # max 100
            "value": "/start",
            # include start_with end_with regular_exp
            "operation": "start_with"
        },
        {
            "key": "referer",
            "type": "string",
            # max 100
            "value": "test.com",
            # include start_with end_with regular_exp
            "operation": "end_with"
        },
        {
            "key": "user_agent",
            "type": "string",
            "value": "[0-9 a-z A-Z \\- _]",
            # include start_with end_with regular_exp
            "operation": "regular_exp"
        },
        {
            "key": "method",
            "type": "enum",
            # GET，POST，HEAD, PUT, DELETE, OPTION, PATCH
            "value": "GET,POST",
            # == ~=
            "operation": "=="
        },
        {
            "key": "response_content_type",
            "type": "string",
            # include: text/xml, application/xml, application/json
            # customize: max input 100
            "value": "application/json;application/xml",
            # include
            "operation": "include"
        },
        {
            "key": "args",
            "type": "string",
            "value": "post",
            # GET，POST，HEAD, PUT, DELETE, OPTION, PATCH
            "operation": "exclude"
        },
        {
            "key": "request_header",
            "header_key": "cookie",
            "type": "string",
            "value": "application/json;application/xml",
            # include start_with end_with regular_exp
            "operation": "include"
        },
        {
            "key": "request_body",
            "type": "string",
            "value": "xxoo",
            # include start_with regular_exp
            "operation": "include"
        }
    ]
}

import null as null
import logging

print("hello MAC")

# actions_list = ['percent = {100}', 'delay = %(delay)s', '%(action)s = %(action_value)s']
# lua_action_str = '{' + ', '.join(actions_list) + '}'
rule_parameter = {
    "is_advfilter": False,
    "key_value": "172.16.30.1",
    "enable": True,
    "action_list": [
        {
            "action": "block_code",
            "action_value": 400,
            "delay": 0,
            "weight": 1
        }
    ],
    "dev_type": [
        "pc",
        "mac",
        "mobile"
    ],
    "auto_list_type": "ip",
    "statistic_counter": [

    ],
    "percent": 100,
    "host": "172.16.30.4",
    "ubb_scene_type": "web",
    "filter_conditions": [
        {
            "key": "src_ip",
            "type": "ip",
            "value": "123.224.244.123/24",
            "operation": "~="
        },
        {
            "key": "has_input",
            "type": "boolean",
            "value": True,
            "operation": "="
        },
        {
            "key": "in_whitelist_in",
            "type": "boolean",
            "value": True,
            "operation": "="
        },
        {
            "key": "is_api",
            "type": "boolean",
            "value": True,
            "operation": "="
        },
        {
            "key": "args",
            "type": "string",
            "value": "jsonid",
            "operation": "include"
        },
        {
            "key": "business_post_data",
            "type": "string",
            "value": "$ -- %% -_ % \\\\' \\' % * # `",
            "operation": "include"
        }
    ],
    "is_path_regx": False,
    "timer_type": "close",
    "key": "ip",
    "auto_list": 0,
    "path": "/",
    "id": 2001,
    "is_host_regx": False,
    "desc": "",
    "freq_limit_type": "rate",
    "time_window_type": "minute",
    "time_window_value": null,
    "threat_value": "undefined",
    "is_key_regx": False,
    "high_freq": 0.001
}

api_customized_rule = {
    "enable": False,
    "group_name": "default",
    "rule_name": "规则三",
    "filter_conditions": [
        {
            "operation": "include",
            "type": "string",
            "value": "10.10.10.10",
            "key": "host"
        },
        {
            "operation": "==",
            "type": "number",
            "value": 8888,
            "key": "port"
        },
        {
            "operation": "start_with",
            "type": "string",
            "value": "/root/api",
            "key": "path"
        },
        {
            "operation": "end_with",
            "type": "string",
            "value": "test.com",
            "key": "referer"
        },
        {
            "operation": "regular_exp",
            "type": "string",
            "value": "[0-9 a-z A-Z \\- _]",
            "key": "user_agent"
        },
        {
            "operation": "==",
            "type": "enum",
            "value": "GET,POST,OPTION",
            "key": "method"
        },
        {
            "operation": "include",
            "type": "string",
            "value": "application/xml",
            "key": "resp_content_type"
        },
        {
            "operation": "include",
            "type": "string",
            "value": "post",
            "key": "args"
        },
        {
            "value": "application/xml",
            "operation": "include",
            "type": "string",
            "header_key": "Accept",
            "key": "req_header"
        },
        {
            "operation": "include",
            "type": "string",
            "value": "xxoo",
            "key": "req_body"
        }
    ],
    "group_by_domain": False,
    "id": 3
}


def create_precondition_action(rule_info, action_info):
    print('rule_info:{}'.format(rule_info))
    print('action_info:{}'.format(action_info))
    percent = rule_info.get('percent', 100)
    actions_list = ['percent = {}'.format(percent)]
    # add unique_actions to basic_actions set
    unique_action_value_dic = {
        'response_html': "%(action)s = '%(action_value)s'",
        'insertjs': "%(action)s = '%(action_value)s'",
        'redirect': "%(action)s = '%(action_value)s'",
        'forward': "%(action)s = '%(action_value)s'",
        'block_code': "%(action)s = %(action_value)s",
        'challenge': "captcha={%(action_value)s}",
        'transpare': "transpare = true",
        'pass': "pass = true",
        'none': "no_action = true"
    }
    action = action_info.get('action', None)
    if (not action) or (action not in unique_action_value_dic):
        raise Exception('Invalid action: {}'.format(action))

    if action == 'none':
        actions_list.append(unique_action_value_dic.get(action))
    else:
        actions_list.append('delay = %(delay)s')
        actions_list.append(unique_action_value_dic.get(action))

    # auto_list
    auto_list_time = rule_info.get('auto_list', 0)
    if auto_list_time > 0:
        pass
    # convert from set to list
    lua_action_str = '{' + ', '.join(actions_list) + '}'
    print('actions_list:{}'.format(actions_list))
    print('lua_action_str:{}'.format(lua_action_str))
    print('action_info:{}'.format(action_info))

    return lua_action_str % action_info


def create_precondition_action_list(rule_info):
    action_template = "rules[%(id)d]['action_list'] = {{ {} }} "

    action_info_list = rule_info.get('action_list', None)
    # compat old flat action
    if action_info_list is None:
        action_info_list = [
            {"action": rule_info['action'], "action_value": rule_info['action_value'], "delay": rule_info['delay'],
             "weight": 1}]
    if not isinstance(action_info_list, list) or len(action_info_list) < 1 or len(action_info_list) > 5:
        raise Exception('Invalid action_list: {}'.format(action_info_list))
    action_list = []
    for action_info in action_info_list:
        # basic actions set
        lua_action = create_precondition_action(rule_info, action_info)
        print('lua_action:{}'.format(lua_action))

        action_list.append(lua_action)

    print('action_list:{}'.format(action_list))
    action_list_str = ',\n'.join(action_list)
    print('action_list_str:{}'.format(action_list_str))

    return action_template.format(action_list_str)


operation_func_template_and_field_type = {
    'include': ("ubb_util:find_plain({field}, '{value}')", ('string',)),  # func_template, allowed_type
    'exclude': ("not ubb_util:find_plain({field}, '{value}')", ('string',)),
    'full_match': ("{field} == '{value}'", ('string',)),
    'start_with': ("ubb_util:string_sub({field},1,#'{value}') == '{value}'", ('string',)),
    'end_with': ("ubb_util:string_sub({field},-#'{value}', -1) == '{value}'", ('string',)),
    'regular_exp': ("ubb_util:reg_find({field}, '{value}')", ('string',)),
    'empty': ("(not {field} or {field} == '')", ('string',)),
    'in_list': ("ubb_util:is_in_list({field}, '{value}')", ('string', 'ip')),
    'not_in_list': ("not ubb_util:is_in_list({field}, '{value}')", ('string', 'ip'))
}


def string_condition_creator(field, condition):
    operator = {
        '==': "{field} == '{value}'",
        '~=': "{field} ~= '{value}'",
    }
    if condition['operation'] in operator:
        return operator[condition['operation']].format(field=field, value=condition['value'])

    func_template = operation_func_template_and_field_type[condition['operation']][0].format(field=field,
                                                                                             value=condition['value'])
    return func_template


def num_condition_creator(field, condition):
    return " {} {} {}".format(field, condition['operation'], condition['value'])


def enum_condition_creator(field_name, condition):
    prefixes = {
        'data_collection_stage': 'BDCS_',
        'prev_invalid_request_action': 'ACTION_',
        'attack_detect_browser_type': 'BT_',
        'bot_type': 'BT_',
        'connection_type': 'BCT_',
        'dr_cookie': 'WE_',
        'dr_refer': 'WE_',
        'dr_post': 'WE_',
        'dr_uri': 'WE_'
    }
    enums = condition['value'].split(',')
    for i in range(0, len(enums)):
        if field_name not in prefixes.keys():
            enums[i] = "'{}'".format(enums[i].strip())
        else:
            if field_name in ('dr_cookie', 'dr_post', 'dr_refer', 'dr_uri') and enums[i].strip() in (
                    'OK', 'ALLOW_OFFLINE', 'HOSTS_REPLACED'):
                value = 'WR_' + enums[i].strip()
            else:
                value = prefixes[field_name] + enums[i].strip()
            enums[i] = "'{}'".format(value)

    enums_str = '{' + ','.join(enums) + '}'

    if condition['operation'] == '==':
        rt = "ubb_util:match_enum_value({}, {})".format(field_name, enums_str)
    elif condition['operation'] == '~=':
        rt = "not ubb_util:match_enum_value({}, {})".format(field_name, enums_str)
    else:
        raise Exception('The operator of Enumeration only allows ==/~=')

    return rt


def create_common_filter_conditions(rule_info):
    conditions = []
    fields = set()
    condition_str = ''

    condition_creators = {
        'string': (lambda x, y: string_condition_creator(x, y)),
        'number': (lambda x, y: num_condition_creator(x, y)),
        'enum': (lambda x, y: enum_condition_creator(x, y))
    }

    filter_conditions = rule_info.get('filter_conditions', None)
    if filter_conditions:
        for condition in filter_conditions:
            fields.add(condition['key'])
            field_type = condition['type']
            condition_str = condition_creators[field_type](condition['key'], condition)
            conditions.append('({})'.format(condition_str))

        condition_str = ' and '.join(conditions)

    return condition_str, fields


def create_filter_condition(rule_info, scene='common'):
    filter_tmpl = "filter_satisfied = function() local _, rt = xpcall(function() return {} end, error_traceback) return rt end"

    condition = ''
    filter_conditions = ''
    sniping_filter_condition = ''
    conditions_str, fields = create_common_filter_conditions(rule_info)
    print('conditions_str={}'.format(conditions_str))
    print('fields={}'.format(fields))

    if conditions_str:
        filter_conditions = filter_tmpl.format(conditions_str)
        condition = 'filter_satisfied()'

    rule_info['sniping_filter_condition'] = sniping_filter_condition
    rule_info['filter_condition'] = filter_conditions

    return condition, fields


action_list = []

settings = ['rules[%(id)d] = {}']

# print('lua_action_str:{}'.format(lua_action_str))
setting = create_precondition_action_list(rule_parameter)
print('setting:{}'.format(setting))
settings.append(setting)

setting_template = '\n'.join(settings)
print('settings:{}'.format(setting_template))

setting = setting_template % rule_parameter
print("==================setting_template {} created successfully:".format(setting))

fields = set()
variables = []
conditions, condition_fields = create_filter_condition(api_customized_rule)
if conditions:
    if isinstance(conditions, list):
        variables.extend(conditions)
    else:
        condition_in_lua = "({})".format(conditions)
        variables.append(condition_in_lua)

    # collect all the condition fields
if condition_fields:
    fields.update(condition_fields)

condition_variables = {
    'condition': '\n      and '.join(variables)
}
print('condition_variables=%(condition)s' % condition_variables)


def is_valid_api_customized_rule(rule):
    if not rule or type(rule) != dict:
        raise Exception('Invalid api customized rule :{}'.format(rule))

    check_func_dict = {
        "enable": ubb_util.ubb_invalid_bool,
        "id": (lambda x: ubb_util.ubb_invalid_int_range(x, max_v=99, min_v=1)),
        "name": (lambda x: ubb_util.ubb_invalid_string(x, length=50, min_lenth=1)),
        # TODO check group whether exist
        "group_name": (lambda x: ubb_util.ubb_invalid_string(x.decode('utf-8'), length=50, min_lenth=1)),
        "group_by_domain": ubb_util.ubb_invalid_bool
    }

    for k, v in rule.items():
        if k in check_func_dict:
            try:
                check_func_dict[k](v)
            except Exception as e:
                logging.error(e.message)
                raise Exception(_('API customized rule Error: key({}) = v({}), msg:{}').format(k, v, e.message))

        else:
            raise Exception(_('key:{0} is not used in api customized rule').format(k))


def save_api_customized_rule(request):
    data = json.loads(request.body)
    rule = dict()
    rule['enable'] = data.get('enable', None)
    rule['id'] = data.get('id', 0)
    rule['name'] = data.get('name', '')
    rule['group_name'] = data.get('group_name', 'default')
    rule['group_by_domain'] = data.get('group_by_domain', None)

    is_valid_api_customized_rule(rule)


# print(config)
print('config_len:', len(configs))
print('config["filter_conditions"]:', len(configs["filter_conditions"]))

for key, value in configs.items():
    print('key:{}'.format(key))
    print('value:{}'.format(value))

conf = {
    "enable": 'True',
    "id": 1,
    "rule_name": "规则一",
    "group_name": "default",
    "group_by_domain": 'False',
    "filter_conditions": [
        {
            "key": "host",
            "type": "string",
            "value": "10.10.10.10",
            "operation": "include"
        },
        {
            "key": "port",
            "type": "number",
            "value": 8080,
            "operation": ">"
        },
        {
            "key": "path",
            "type": "string",
            "value": "/start",
            "operation": "start_with"
        },
        {
            "key": "referer",
            "type": "string",
            "value": "test.com",
            "operation": "end_with"
        },
        {
            "key": "user_agent",
            "type": "string",
            "value": "[0-9 a-z A-Z \\- _]",
            "operation": "regular_exp"
        },
        {
            "key": "method",
            "type": "enum",
            "value": "GET,POST",
            "operation": "=="
        },
        {
            "key": "resp_content_type",
            "type": "string",
            "value": "application/json;application/xml",
            "operation": "include"
        },
        {
            "key": "args",
            "type": "string",
            "value": "post",
            "operation": "include"
        },
        {
            "key": "req_header",
            "header_key": "cookie",
            "type": "string",
            "value": "application/json;application/xml",
            "operation": "include"
        },
        {
            "key": "req_body",
            "type": "string",
            "value": "xxoo",
            "operation": "include"
        }
    ]
}

list_dict = [
    {
        "enable": False,
        "group_name": "default",
        "rule_name": "规则一",
        "filter_conditions": [
            {
                "operation": "include",
                "type": "string",
                "value": "172.16.30.4",
                "key": "host"
            },
            {
                "operation": "<",
                "type": "number",
                "value": 8888,
                "key": "port"
            },
            {
                "operation": "start_with",
                "type": "string",
                "value": "/start",
                "key": "path"
            },
            {
                "operation": "end_with",
                "type": "string",
                "value": "test.com",
                "key": "referer"
            },
            {
                "operation": "regular_exp",
                "type": "string",
                "value": "[0-9 a-z A-Z \\- _]",
                "key": "user_agent"
            },
            {
                "operation": "==",
                "type": "enum",
                "value": "GET,POST",
                "key": "method"
            },
            {
                "operation": "include",
                "type": "string",
                "value": "application/json;application/xml",
                "key": "resp_content_type"
            },
            {
                "operation": "include",
                "type": "string",
                "value": "post",
                "key": "args"
            },
            {
                "value": "application/json",
                "operation": "include",
                "type": "string",
                "header_key": "content-type",
                "key": "req_header"
            },
            {
                "operation": "include",
                "type": "string",
                "value": "xxoo",
                "key": "req_body"
            }
        ],
        "group_by_domain": False,
        "id": 1
    },
    {
        "enable": False,
        "group_name": "default",
        "rule_name": "规则三",
        "filter_conditions": [
            {
                "operation": "include",
                "type": "string",
                "key": "host",
                "value": "10.10.10.10"
            },
            {
                "operation": "==",
                "type": "number",
                "key": "port",
                "value": 8888
            },
            {
                "operation": "start_with",
                "type": "string",
                "key": "path",
                "value": "/root/api"
            },
            {
                "operation": "end_with",
                "type": "string",
                "key": "referer",
                "value": "test.com"
            },
            {
                "operation": "regular_exp",
                "type": "string",
                "key": "user_agent",
                "value": "[0-9 a-z A-Z \\- _]"
            },
            {
                "operation": "==",
                "type": "enum",
                "key": "method",
                "value": "GET,POST,OPTION"
            },
            {
                "operation": "include",
                "type": "string",
                "key": "resp_content_type",
                "value": "application/xml"
            },
            {
                "operation": "include",
                "type": "string",
                "key": "args",
                "value": "post"
            },
            {
                "key": "req_header",
                "operation": "include",
                "type": "string",
                "header_key": "Accept",
                "value": "application/xml"
            },
            {
                "operation": "include",
                "type": "string",
                "key": "req_body",
                "value": "xxoo"
            }
        ],
        "group_by_domain": True,
        "id": 3
    },
    {
        "enable": False,
        "group_name": "default",
        "rule_name": "rule五",
        "filter_conditions": [
            {
                "operation": "include",
                "type": "string",
                "key": "host",
                "value": "10.10.10.10"
            },
            {
                "operation": ">",
                "type": "number",
                "key": "port",
                "value": 8080
            },
            {
                "operation": "start_with",
                "type": "string",
                "key": "path",
                "value": "/start"
            },
            {
                "operation": "end_with",
                "type": "string",
                "key": "referer",
                "value": "test.com"
            },
            {
                "operation": "regular_exp",
                "type": "string",
                "key": "user_agent",
                "value": "[0-9 a-z A-Z \\- _]"
            },
            {
                "operation": "==",
                "type": "enum",
                "key": "method",
                "value": "GET,POST"
            },
            {
                "operation": "include",
                "type": "string",
                "key": "resp_content_type",
                "value": "application/x-www-form-urlencoded"
            },
            {
                "operation": "include",
                "type": "string",
                "key": "args",
                "value": "post"
            },
            {
                "key": "req_header",
                "operation": "include",
                "type": "string",
                "header_key": "Connection",
                "value": "keep-alive"
            },
            {
                "operation": "include",
                "type": "string",
                "key": "req_body",
                "value": "xxoo xoxo oxox"
            }
        ],
        "group_by_domain": False,
        "id": 5
    },
    {
        "enable": False,
        "group_name": "172.16.30.4:80",
        "rule_name": "api规则11",
        "filter_conditions": [
            {
                "operation": "include",
                "type": "string",
                "key": "host",
                "value": "30.4"
            },
            {
                "operation": "==",
                "type": "number",
                "key": "port",
                "value": 80
            },
            {
                "operation": "==",
                "type": "enum",
                "key": "method",
                "value": "GET,POST"
            }
        ],
        "group_by_domain": False,
        "id": 11
    },
    {
        "enable": False,
        "group_name": "172.16.30.4:80",
        "rule_name": "api规则12",
        "filter_conditions": [
            {
                "operation": "include",
                "type": "string",
                "value": "fromAccount",
                "key": "req_body"
            },
            {
                "operation": "regular_exp",
                "type": "string",
                "value": "[0-9 a-z A-Z \\- _ . :]",
                "key": "req_body"
            },
            {
                "operation": "==",
                "type": "enum",
                "value": "GET,POST",
                "key": "method"
            }
        ],
        "group_by_domain": False,
        "id": 12
    },
    {
        "enable": False,
        "group_name": "172.16.30.4:80",
        "rule_name": "api规则13",
        "filter_conditions": [
            {
                "operation": "include",
                "type": "string",
                "key": "req_body",
                "value": "fromAccount"
            },
            {
                "operation": "regular_exp",
                "type": "string",
                "key": "req_body",
                "value": "[0-9 a-z A-Z]"
            },
            {
                "operation": "==",
                "type": "enum",
                "key": "method",
                "value": "GET,POST"
            }
        ],
        "group_by_domain": False,
        "id": 13
    },
    {
        "enable": False,
        "group_name": "172.16.30.4:80",
        "rule_name": "api规则14 update",
        "filter_conditions": [
            {
                "operation": "include",
                "type": "string",
                "key": "req_body",
                "value": "fromAccount"
            },
            {
                "operation": "regular_exp",
                "type": "string",
                "key": "req_body",
                "value": "[0-9 a-z A-Z]"
            },
            {
                "operation": "==",
                "type": "enum",
                "key": "method",
                "value": "GET,POST"
            }
        ],
        "group_by_domain": False,
        "id": 14
    },
    {
        "enable": False,
        "group_name": "172.16.30.4:80",
        "rule_name": "api规则添加ID生产",
        "filter_conditions": [
            {
                "operation": "include",
                "type": "string",
                "value": "fromAccount",
                "key": "req_body"
            },
            {
                "operation": "regular_exp",
                "type": "string",
                "value": "[0-9 a-z A-Z]",
                "key": "req_body"
            },
            {
                "operation": "==",
                "type": "enum",
                "value": "GET,POST",
                "key": "method"
            }
        ],
        "group_by_domain": False,
        "id": 15
    },
    {
        "enable": False,
        "group_name": "172.16.30.4:80",
        "rule_name": "api规则添加ID服务器生成",
        "filter_conditions": [
            {
                "operation": "include",
                "type": "string",
                "key": "req_body",
                "value": "fromAccount"
            },
            {
                "operation": "regular_exp",
                "type": "string",
                "key": "req_body",
                "value": "[0-9 a-z A-Z]"
            },
            {
                "operation": "==",
                "type": "enum",
                "key": "method",
                "value": "GET,POST"
            }
        ],
        "group_by_domain": False,
        "id": 16
    },
    {
        "enable": False,
        "group_name": "default",
        "rule_name": "规则一",
        "filter_conditions": [
            {
                "operation": "include",
                "type": "string",
                "key": "host",
                "value": "10.10.10.10"
            },
            {
                "operation": ">",
                "type": "number",
                "key": "port",
                "value": 8080
            },
            {
                "operation": "start_with",
                "type": "string",
                "key": "path",
                "value": "/start"
            },
            {
                "operation": "end_with",
                "type": "string",
                "key": "referer",
                "value": "test.com"
            },
            {
                "operation": "regular_exp",
                "type": "string",
                "key": "user_agent",
                "value": "[0-9 a-z A-Z \\- _]"
            },
            {
                "operation": "==",
                "type": "enum",
                "key": "method",
                "value": "GET,POST"
            },
            {
                "operation": "include",
                "type": "string",
                "key": "resp_content_type",
                "value": "application/json;application/xml"
            },
            {
                "operation": "include",
                "type": "string",
                "key": "args",
                "value": "post"
            },
            {
                "key": "req_header",
                "operation": "include",
                "type": "string",
                "header_key": "cookie",
                "value": "application/json;application/xml"
            },
            {
                "operation": "include",
                "type": "string",
                "key": "req_body",
                "value": "xxoo"
            }
        ],
        "group_by_domain": False,
        "id": 17
    }
]

filter_conditions = [
    {
        "operation": "include",
        "type": "string",
        "value": "30.4",
        "key": "host"
    },
    {
        "operation": "==",
        "type": "number",
        "value": 80,
        "key": "port"
    },
    {
        "operation": "==",
        "type": "enum",
        "value": "GET,POST",
        "key": "method"
    },
    {
        "key": "req_header",
        "operation": "include",
        "type": "string",
        "header_key": "cookie",
        "value": "’\  / % %%% %%"
    },
    {
        "operation": "regular_exp",
        "type": "string",
        "key": "req_body",
        "value": "[0-9 a-z A-Z \\- _]"
    }
]
# print(conf['filter_conditions'][0].keys())
# count = rule.count("regular_exp")
# print('rule.values:', filter_conditions.values())
print('****'.center(80, '*'))
regular_exp = 0
for rule in list_dict:
    for one_filter in rule['filter_conditions']:
        print(one_filter['operation'])
        if one_filter['operation'] == 'regular_exp':
            regular_exp += 1

print('regular_exp:', regular_exp)
