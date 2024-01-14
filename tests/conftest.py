from pytest import fixture

import reunion


@fixture
def meeting():
    meeting = reunion.Meeting()
    return meeting
