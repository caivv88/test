json_dict = {"int": "整数", "float": "浮点", "str": "字符串", "list": "列表", "tuple": "元组", "dict": "字典", "set": "集合"}
json_list = list(json_dict.keys())
key_need = ["int", "float", "tuple", "dict", "double", "boolean"]
key_need = ["int", "float", "tuple", "dict"]

# 多余的
redundant_list = list(set(json_dict)-set(key_need))
# 缺失的
missing_list = list(set(key_need)-set(json_dict))
