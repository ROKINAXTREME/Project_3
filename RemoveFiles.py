import time, os, shutil
print('hi')
path=input('what is you path name')
result = time.localtime()
day =result.tm_mday
if os.path.exists(path):
    os.walk(path)
    os.path.join()
    os.stat.path
    if day > 30:
        try:
            os.remove(path)
        except:
            shutil.rmtree()
