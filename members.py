from logging import getLogger

logger = getLogger()

class MembersList():

    def __init__(self):
        self.new('', 0)

    def full(self):
        return len(self.members) == self.limit
 
    def add(self, cid, name):
        if sum(1 for i in self.ids if i == cid) == 2:
            return False
        self.ids.append(cid)
        number = len(self.members) + 1
        item = str(number) + '. ' + name
        self.members.append(item)
        return True

    def get(self):
        return self.header + '\n\n' + '\n'.join(self.members)

    def new(self, header, limit):
        self.members = []
        self.ids = []
        self.header = header
        self.limit = limit
