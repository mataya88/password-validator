def password_validator(input_pw: str, min_chars=8, max_chars=30, lower_char=True, upper_char=True, num=True, non_alphanum=True, **kwargs):
    """
    Function to check the validity of an input password

    Parameters
    ----------

    input_pw : str 
        The tested password
    min_chars : int, default 8
        The minimum number of characters wanted in the password
    max_chars : int, default 30
        The maximum number of characters wanted in the password
    lower_char : bool, default True
        True if the password must contain lower-case letters
    upper_char : bool, default True
        True if the password must contain upper-case letters
    num : bool, default True
        True if the password must contain a number
    non_alphanum : bool, default True
        True if the password must contain a non-alphanumeric character

    **kwargs : str, optional
        Extra tests, the argument name must be the error, and the value must be a regular expression representing the character wanted in the password, e.g., no_M_letter = "M" 

    Returns
    -------
    int
        The number of passed tessed
    list
        The errors in the input password as strings
    """
    import re

    # We want to check if the builtin conditions are wanted by the user by comparing the following list against the following dict
    builtin_conditions_list = [lower_char, upper_char, num, non_alphanum]

    builtin_regex_dict = {"no small characters": r"[a-z]",
                          "no capital letters": r"[A-Z]",
                          "no numbers": r"[0-9]",
                          "no non-alphanumeric characters": r"[\W]"}

    conditions_dict = {**kwargs}

    errors_list = []  # Each unpassed test will be added here

    for i, j in zip(builtin_conditions_list, builtin_regex_dict.items()):
        # This loop is to add the wanted builtin conditions to the conditions dict
        if i:
            conditions_dict.update({j[0]: j[1]})

    passed_conditions_int = 0

    # The following if else is to check for minimum and maximum number of characters
    if len(input_pw) >= min_chars:
        passed_conditions_int += 1
    else:
        errors_list.append(f"less than {min_chars} characters")
    if len(input_pw) <= max_chars:
        passed_conditions_int += 1
    else:
        errors_list.append(f"more than {max_chars} characters")

    for key, val in conditions_dict.items():
        # Conduting the tests
        if not re.search(val, input_pw):
            errors_list.append(key)
        else:
            passed_conditions_int += 1

    return passed_conditions_int, errors_list

