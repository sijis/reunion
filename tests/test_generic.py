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
    'user3: #action I will do that.',
    'user2: Another response',
    'user1: #topic Last Topic',
    'user4: #info Test info',
    'user3: Thank you',
    'user5: Adios',
    'user2: #action Action must be taken',
    'user2: #action Another action must be taken',
    'user1: #endmeeting',
    'user4: last message',
]

def test_parse():

    meeting = reunion.Meeting()
    for text in BASIC_REUNION:
        meeting.parse(text)

    assert type(meeting.results) == dict
    assert 'actions' in meeting.results
    assert 'topics' in meeting.results
    assert 'users' in meeting.results
    assert meeting.results['discussion'] == BASIC_REUNION[1:-1]

    import pprint
    pprint.pprint(meeting.results)
