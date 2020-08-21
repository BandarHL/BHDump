from application import Application
from BHUtility import *
from colorit import *
import argparse
import time

start_time = time.time()
init_colorit()
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--applicationpath", required=True,
                help="Application path to dump")
basePath = '/var/mobile/Documents/Apps'

if __name__ == '__main__':
    args = vars(ap.parse_args())
    old = args['applicationpath']
    new = '{}/Payload/{}'.format(basePath, old.split('/')[-1])
    copy_dir(old, new)
    app = Application(path=new, path2=basePath)
    for i in app.getListOfFileThatNeedDump():
        Application.dumpFile(i)
        print(color(i.split('/')[-1], Colors.green))
    app.fixPlist()
    app.zipTheApp()
    shutil.rmtree(new)
    print(color("Done, its take: %s seconds" % (time.time() - start_time), Colors.red))