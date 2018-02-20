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

    def parse(self, message):

        msg = self.message_parser(message)

        if msg.action in self.keywords:
            if '#startmeeting' == msg.action:
                self._started = True

            if '#endmeeting' in msg.action:
                self._started = False
                return

            self.results['discussion'].append(msg.full_message)

            if '#topic' == msg.action:

                if msg.text in self.results['topics']:
                    self.results['topics'][msg.text].append(msg.text)
                else:
                    self.results['topics'][msg.text] = []

            if '#action' == msg.action:

                if msg.username in self.results['actions']:
                    self.results['actions'][msg.username].append(msg.text)
                else:
                    self.results['actions'][msg.username] = []

    def message_parser(self, message):
        items = [
            'username',
            'full_message',
            'action',
            'text',
        ]

        Message = namedtuple('Message', items)
        username, *full_message = message.split()
        action, *rest_message = full_message

        m = {
            'username': username,
            'full_message': message,
            'action': action,
            'text': ' '.join(rest_message)
        }

        msg = Message(**m)
        return msg
