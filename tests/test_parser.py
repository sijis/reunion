import pytest


@pytest.mark.parametrize(
    "text,action,user",
    [
        ("foo: #startmeeting", "#startmeeting", "foo"),
        ("foo: #startmeeting now", "#startmeeting", "foo"),
        ("$bar: #info", "#info", "$bar"),
        ("%foo: #action", "#action", "%foo"),
        ("baz: #nothing", None, "baz"),
        ("foo: #endmeeting", "#endmeeting", "foo"),
    ],
)
def test_msg_parser_action(meeting, text, action, user):
    response = meeting.message_parser(text)
    assert response.action == action
    assert response.username == user


@pytest.mark.parametrize(
    "message,user,text",
    [
        ("user1: comment1", "user1", "comment1"),
        ("foo bar: comment1", "foo bar", "comment1"),
        ("foo bar: comment two", "foo bar", "comment two"),
        ("@foo bar: comment two", "@foo bar", "comment two"),
        ("$baz: comment one", "$baz", "comment one"),
    ],
)
def test_msg_parser_non_action(meeting, message, user, text):
    response = meeting.message_parser(message)
    assert response.action == None
    assert response.username == user
    assert response.text == text


@pytest.mark.parametrize(
    "message",
    [
        ("foo: comment1"),
        ("baz: #something text"),
        ("#bar: #endmeeting text"),
    ],
)
def test_msg_parser_full_message(meeting, message):
    response = meeting.message_parser(message)
    assert response.full_message == message
