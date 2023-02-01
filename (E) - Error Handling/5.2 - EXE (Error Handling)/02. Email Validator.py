import re
regex_email_validator = r"^(\w{5,})(\@{1})(\w{1,})(\.com{1}|\.bg{1}|\.net{1}|\.org{1})$"


class NameTooShort(Exception):
    """NameTooShortError - "Name must be more than 4 characters" """


class MustContainAtSymbolError(Exception):
    """MustContainAtSymbolError - "Email must contain @" """


class InvalidDomainError(Exception):
    """InvalidDomainError - "Domain must be one of the following: .com, .bg, .org, .net" """


def return_error_function(email: str):
    def check_length_function():
        name_length = 0
        for char in email:
            if char != "@":
                name_length += 1
            else:
                break
        if name_length > 4:
            return {"Length": True}
        else:
            return {"Length": False}

    def check_symbol_function():
        special_symbol = "@"
        if special_symbol in email:
            return {"Symbol": True}
        else:
            return {"Symbol": False}

    def check_domain_function():
        valid_domain_list = [".com", ".bg", ".org", ".net"]
        possible_domain = email[-4:]
        possible_domain_bg = email[-3:]
        if possible_domain in valid_domain_list or possible_domain_bg in valid_domain_list:
            return {"Domain": True}
        else:
            return {"Domain": False}
    first_check_dict = check_length_function()
    second_check_dict = check_symbol_function()
    third_check_dict = check_domain_function()
    check_list = [first_check_dict, second_check_dict, third_check_dict]
    for validator_dict in check_list:
        for validator, result in validator_dict.items():
            if not result:   # False
                return validator
            else:   # True
                continue


COMMAND_END = "End"
while True:
    command = input()
    if command == COMMAND_END:
        break
    else:
        current_email = command
        email_list = re.findall(regex_email_validator, current_email)
        if email_list:   # Email is valid
            print("Email is valid")
        else:   # Email is not valid
            error = return_error_function(current_email)
            if error == "Length":
                raise NameTooShort("Name must be more than 4 characters")
            elif error == "Symbol":
                raise MustContainAtSymbolError("Email must contain @")
            else:   # elif error == "Domain":
                raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")


# import re
# regex_email_validator = r"^(\w{5,})(\@{1})(\w{1,})(\.com{1}|\.bg{1}|\.net{1}|\.org{1})$"
#
#
# class NameTooShort(Exception):
#     """NameTooShortError - "Name must be more than 4 characters" """
#
#
# class MustContainAtSymbolError(Exception):
#     """MustContainAtSymbolError - "Email must contain @" """
#
#
# class InvalidDomainError(Exception):
#     """InvalidDomainError - "Domain must be one of the following: .com, .bg, .org, .net" """
#
#
# def check_length_function(some_email: str):
#     current_name_length = 0
#     for char in some_email:
#         if char != "@":
#             current_name_length += 1
#         else:
#             break
#     if current_name_length > 4:
#         return "True"
#     else:
#         return "False"
#
#
# def check_symbol_function(some_email: str):
#     special_symbol = "@"
#     if special_symbol in some_email:
#         return "True"
#     else:
#         return "False"
#
#
# def check_domain_function(some_email: str):
#     valid_domain_list = [".com", ".bg", ".org", ".net"]
#     possible_domain = some_email[-4:]
#     possible_domain_bg = some_email[-3:]
#     if possible_domain in valid_domain_list or possible_domain_bg in valid_domain_list:
#         return "True"
#     else:
#         return "False"
#
#
# COMMAND_END = "End"
# while True:
#     command = input()
#     if command == COMMAND_END:
#         break
#     else:
#         current_email = command
#         email_list = re.findall(regex_email_validator, current_email)
#         if email_list:
#             print("Email is valid")
#         else:
#             check_length = check_length_function(current_email)
#             if check_length == "False":
#                 raise NameTooShort("Name must be more than 4 characters")
#             else:
#                 check_symbol = check_symbol_function(current_email)
#                 if check_symbol == "False":
#                     raise MustContainAtSymbolError("Email must contain @")
#                 else:
#                     check_domain = check_domain_function(current_email)
#                     if check_domain == "False":
#                         raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
#                     else:
#                         continue
