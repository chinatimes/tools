#输出当前目录下文件的MD5
#chinatimes
#mail:lhl_hb@163.com
#20200731

import os
import hashlib

md5log = open('sha256sums.txt','w');
for i in  (os.listdir()):
    if os.path.isfile(i):
        with open(i, 'rb') as fp:
            data = fp.read()
        file_md5= hashlib.sha256(data).hexdigest()
#        print(f'{i:50} ===>  {file_md5}') 
        print( "%50s ===>: %s"  % (i,file_md5))
        md5log.write("%-50s ===>: %s\n"  % (i,file_md5)) 
                
md5log.close()        
 
