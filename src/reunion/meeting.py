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

        username, *full_message = message.split()
        action, *rest_message = full_message
        nice_message = ' '.join(rest_message)

        if action in self.keywords:
            if '#startmeeting' == action:
                self._started = True

            if '#endmeeting' in action:
                self._started = False
                return

            self.results['discussion'].append(message)

            if '#topic' == action:

                if nice_message in self.results['topics']:
                    self.results['topics'][nice_message].append(nice_message)
                else:
                    self.results['topics'][nice_message] = []

            if '#action' == action:

                if nice_message in self.results['actions']:
                    self.results['actions'][username].append(nice_message)
                else:
                    self.results['actions'][username] = []

    def message_parser(self, message):
        return message
