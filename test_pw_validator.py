from pw_validator import password_validator


def test_one():
    """ Testing default conditions. Three are not met"""
    assert password_validator("dfjklsfa") == (3, ["no capital letters",
                                                  "no numbers",
                                                  "no non-alphanumeric characters"])


def test_two():
    """Testing with default conditions. All are met"""
    assert password_validator(r"\fdD 34dld") == (6, [])


def test_three():
    """Testing maximum range of characters, upper characters condition and numers conditions"""
    assert password_validator("dfjklsfad;lajs;fljaf;lfa;lsdfjas;lfjfds") == (3, ["more than 30 characters",
                                                                                 "no capital letters",
                                                                                 "no numbers"])


def test_four():
    """Testing two added conditions. Both are not met"""
    assert password_validator(
        "Asf34#fdss", no_plus='[+]', no_Q='Q') == (6, ['no plus', 'no Q'])


def test_five():
    """ Testing two added conditions. One is met and one is not met.
    """
    assert password_validator(
        "Asf34#fdss+", no_plus='[+]', no_Q='Q') == (7, ['no Q'])

def test_six():
    """Testing added condition and turning off default conditions. Successful password"""
    assert password_validator("jsdd88$ffd", upper_char = False, no_dollar_sign = '\$') == (6,[])

def test_seven():
    """Testing one added condition. Upper character conditions is turned off and minimum characters is changed. Two conditions are not met"""
    assert password_validator("jsdd8@ffd", upper_char = False, min_chars = 10, no_dollar_sign = '\$') == (4,["less than 10 characters", "no dollar sign"])
