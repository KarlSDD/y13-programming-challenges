from task6_email_checker import *


def test_invalid_list():
    assert validate_email_list(["jared", "diane@dc-high", "@dchigh-suzhou.cn", "manisha.cn"]) == []


def test_valid_list():
    assert validate_email_list(["jared.rigby@dchigh-suzhou.cn", "diane@dchigh-suzhou.cn", "manisha@dchigh-suzhou.cn"]) == ["diane@dchigh-suzhou.cn", "jared.rigby@dchigh-suzhou.cn", "manisha@dchigh-suzhou.cn"]


def test_mixed_list():
    assert validate_email_list(["@dchigh-suzhou.cn", "manisha.cn", "jared.rigby@dchigh-suzhou.cn", "diane@dchigh-suzhou.cn"]) == ["diane@dchigh-suzhou.cn", "jared.rigby@dchigh-suzhou.cn"]
