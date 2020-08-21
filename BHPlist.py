import plistlib

class BHPlist:
    def __init__(self, path):
        self.plistPath = path
        self.pl = self.loadPlist()

    def loadPlist(self):
        file = open(self.plistPath, 'rb')
        return plistlib.load(file)

    def writeChanges(self):
        file = open(self.plistPath, 'wb')
        plistlib.dump(self.pl, file)
        file.close()