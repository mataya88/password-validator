from pw_checker_refactor import password_validator


def test_one():
    assert password_validator("dfjklsfa") == (3, ["no capital letters",
                                                 "no numbers",
                                                 "no non-alphanumeric characters"])


def test_two():
    assert password_validator(r"\fdD 34dld") == (6, [])

def test_three():
    assert password_validator("dfjklsfad;lajs;fljaf;lfa;lsdfjas;lfjfds") ==      (3,["more than 30 characters",
    "no capital letters",
    "no numbers"])

def test_four():
    assert password_validator("Asf34#fdss", no_plus = '[+]', no_Q = 'Q') == (6,['no_plus', 'no_Q'] )

def test_five():
    assert password_validator("Asf34#fdss+", no_plus = '[+]', no_Q = 'Q') == (7,['no_Q'] )
