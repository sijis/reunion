from collections import namedtuple

class Meeting:

    def __init__(self):
        self.results = {
            'discussion': [],
            'topics': {},
            'actions': {},
        }

        self.keywords = [
            '#startmeeting',
            '#topic',
            '#action',
            '#endmeeting',
        ]

        self._started = False
        self._start_topic = None
        self._start_action = None

    def parse(self, message):

        msg = self.message_parser(message)
        self.keyword_parser(msg)

        if self._started:
            self.results['discussion'].append(msg.full_message)

            if self._start_topic and not msg.action:
                self.results['topics'][self._start_topic].append(msg.full_message)

            if self._start_action and not msg.action:
                self.results['actions'][msg.username].append(msg.full_message)

    def message_parser(self, message):
        items = [
            'username',
            'full_message',
            'action',
            'text',
        ]

        Message = namedtuple('Message', items)
        username, *full_message = message.split()

        if full_message[0] in self.keywords:
            action, *rest_message = full_message
        else:
            action, rest_message = None, full_message

        m = {
            'username': username,
            'full_message': message,
            'action': action,
            'text': ' '.join(rest_message)
        }

        msg = Message(**m)
        return msg

    def keyword_parser(self, msg):
        if msg.action in self.keywords:
            if '#startmeeting' == msg.action:
                self._started = True

            if '#endmeeting' in msg.action:
                self._started = False
                self.results['discussion'].append(msg.full_message)
                return

            if '#topic' == msg.action:
                self._start_topic = msg.text
                self.results['topics'][self._start_topic] = []

            if '#action' == msg.action:
                self._start_action = msg.text
                self.results['actions'][msg.username] = []
