import os
import re
from typing import Any

ori_path='nietzsche'
ori_names=os.listdir(ori_path)
tar_path='docsify/sources'

class Readme:
    def __init__(self) -> None:
        self.f=open('./docsify/readme.md',mode='w')
        self.f.write('# 目录\n\n')
    def __call__(self, line,*args: Any, **kwds: Any) -> Any:
        self.f.write(line)
    def __del__(self):
        print('file close')
        self.f.close()

def logging(name:str):
    # print('processing: ',name)
    text={'name':name.split('.')[0],'md':os.path.join(name.split('.')[0]+'.md')}
    string='* [{name}](sources/{md})'.format(**text)
    print(string)
    return string+"\n\n"

def process(line:str=None):
    annotation=[chr(i+9312) for i in range(20)]
    if (re.match(pattern='第.*章|第.*卷',string=line) is not None) or \
        (re.match(pattern='§',string=line)is not None):
        # (re.match(pattern='第')):
        line = '# '+line+ '***'
    elif line[0] in annotation:
        line='<font size=2>'+line+"</font>"
    elif len(line)>1:
        line='   > '+line
    return line

if __name__ =="__main__":
    readme=Readme()

    for name in ori_names:
        if name.split('.')[-1] in ['txt']:
            string=logging(name)
            readme(string)
            with open(os.path.join(tar_path,name.split('.')[0]+'.md'),mode='w') as t_f:
                with open(os.path.join(ori_path,name)) as f:
                    for line in f:
                        line = process(line)
                        t_f.write(line)
                f.close()
            t_f.close()
    
    del readme
