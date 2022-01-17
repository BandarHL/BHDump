import os
import pathlib
from BHUtility import make_zipfile
from BHPlist import BHPlist
from colorit import *


class Application:
    def __init__(self, path, path2):
        self.applicationPath = path
        self.basePath = path2

    def getListOfFiles(self):
        listOfFiles = list()
        for (dirpath, dirnames, filenames) in os.walk(self.applicationPath):
            for file in filenames:
                listOfFiles += [os.path.join(dirpath, file)]
        return listOfFiles

    # https://stackoverflow.com/a/51495076/9910699
    def is_binary(self, file_name):
        try:
            with open(file_name, 'tr') as check_file:  # try open file in text mode
                check_file.read()
                return False
        except:  # if fail then file is non-text (binary)
            return True

    def getListOfFileThatNeedDump(self):
        listOfFiles = list()
        for i in self.getListOfFiles():
            file = pathlib.PurePosixPath(i).suffix
            if "dylib" in file:
                listOfFiles.append(i)
            elif not file:
                if "_CodeSignature" not in i and "PkgInfo" not in i:
                    if self.is_binary(i):
                        listOfFiles.append(i)
        return listOfFiles

    def getInfoPlistPath(self):
        for i in self.getListOfFiles():
            file = i.split('/')[-1]
            if file == 'Info.plist':
                return i

    def fixPlist(self):
        InfoPlist = BHPlist(path=self.getInfoPlistPath())
        InfoPlist.pl['MinimumOSVersion'] = '12.0'
        InfoPlist.writeChanges()
        for key in list(InfoPlist.pl):
            if key == 'UISupportedDevices':
                InfoPlist.pl.pop('UISupportedDevices')
                InfoPlist.writeChanges()

    def zipTheApp(self):
        zipPath = '{}/{}.ipa'.format(self.basePath, self.applicationPath.split('/')[-1].replace('.app', ''))
        dirZip = '{}/Payload'.format(self.basePath)
        print(color('All Done, Creating ipa file...', Colors.green))
        make_zipfile(zipPath, dirZip)

    @classmethod
    def dumpFile(cls, path):
        cmd = 'flexdecrypt {} --output {}'.format(path.replace(' ', '\ '), path.replace(' ', '\ '))
        os.popen(cmd).read()
