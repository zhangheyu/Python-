# encoding:utf-8

import json

configs = [
    {
        "enable": True,
        "id": 1,
        "name": "规则一",
        "group": "default",
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
                # include customize
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
    },
    {
        "enable": True,
        #   cdvssf
        "id": 2,
        "name": "规则2",
        "group": "default",
        "group_by_domain": True,
        "filter_conditions": [
            {
                "key": "hostname",
                "type": "string",
                "value": "10.10.10.10",
                "operation": "include"
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
                "key": "response_content_type",
                "type": "string",
                "value": "application/json",
                "operation": "include"
            },
            {
                "key": "args",
                "type": "string",
                "value": "post",
                "operation": "exclude"
            }
        ]
    }
]


# print(config)
print('config_len:', len(configs))
print('config[0]["filter_conditions"]:', len(configs[0]["filter_conditions"]))
print('config[1]["filter_conditions"]:', len(configs[1]["filter_conditions"]))


for config in configs:
    for key, value in config.items():
        print('key:{}'.format(key))
        print('value:{}'.format(value))
