class UserManager(object):
    def __init__(self):
        # uid => username
        self.uid = {}
        self.onlineUsers = {}

    def userSignon(self):
        pass

    def userSignoff(self):
        pass

class User(object):
    def __init__(self):
        self.uid = 0
        self.username = ''
        self.status = 0
        self.privateChat = {}
        self.groupChat = {}
        self.friends = {}

    def sendMsgToUser(self, uid, msg):
        pass

    def sendMsgToGroup(self, gid, msg):
        pass

    def addUser(self, fromUser, toUser):
        pass

    def approveAdd(self):
        pass

    def rejectAdd(self):
        pass

    def addConversationToUser(self, uid):
        pass

    def addConversationToGroup(self, uid, gid):
        pass

class Conversation(object):
    def __init__(self):
        self.gid = 0
        self.participants = []
        self.message = []

    def getMsg(self):
        pass

    def addMsg(self):
        pass

class PrivateChat(Conversation):
    def addParticipant(self):
        pass

    def removeParticipant(self):
        pass

class GroupChat(Conversation):
    def addParticipants(self):
        pass

    def removeParticipants(self):
        pass

class Message(object):
    def __init__(self):
        self.mid = 0
        self.content = ''
        self.time = 0

    def getContent(self):
        pass

    def getDate(self):
        pass