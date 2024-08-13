from errors import ImproperlyConfigured


# def user_to_names(user: str | None) -> tuple[str, str]:
#     if user is None:
#         raise ImproperlyConfigured("User name is empty")

#     name_tokens = user.split(" ")
#     if len(name_tokens) == 0:
#         raise ImproperlyConfigured("User name is empty")
#     elif len(name_tokens) == 1:
#         first_name, last_name = name_tokens[0], name_tokens[0]
#     else:
#         first_name, last_name = " ".join(name_tokens[:-1]), name_tokens[-1]

#     return first_name, last_name
# 將 type hint 的寫法改為兼容的方式
# def user_to_names(user: str) -> tuple[str, str]:  # 移除 | None
#     if user is None:
#         return ("", "")  # 或者根據需求返回其他預設值
#     first_name, last_name = user.split(" ", 1)
#     return first_name, last_name

def user_to_names(user: str) -> tuple[str, str]:
    parts = user.split(" ", 1)
    if len(parts) == 2:
        first_name, last_name = parts
    else:
        first_name = parts[0]
        last_name = ""  # 如果沒有姓氏,使用空字符串作為默認值
    return first_name, last_name