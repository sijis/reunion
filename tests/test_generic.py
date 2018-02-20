import reunion


BASIC_REUNION = [
    'user1: finishing some text',
    'user1: #startmeeting',
    'user1: #topic Who is here?',
    'user2: I am',
    'user3: I am here',
    'user4: I am here too',
    'user1: #topic Topic1',
    'user3: I replied',
    'user2: Another response',
    'user1: #topic End Topic',
    'user3: Thank you',
    'user5: Adios',
    'user2: #action Action must be taken',
    'user2: #action Another action must be taken',
    'user1: #endmeeting',
]

def test_parse():

    meeting = reunion.Meeting()
    for text in BASIC_REUNION:
        meeting.parse(text)

    assert type(meeting.results) == dict
    assert 'actions' in meeting.results
    assert 'topics' in meeting.results
    print(meeting.results)
