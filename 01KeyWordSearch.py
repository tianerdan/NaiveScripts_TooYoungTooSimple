# 使用时把程序放到树洞txt同一级目录下.

import os

class Solution:
    def ReadFile(FileName,word):
        '''
        在FileName文件中搜索word
        '''
        fp = open(FileName, "r")
        for line in fp:
            if word in line:
                print(line)
        fp.close()
        return 0

word=input('The key word to be searched:')

for filename in os.listdir(os.path.dirname(os.path.abspath(__file__))):
    if filename[-4:]=='.txt':
        Solution.ReadFile(filename,word) # 注意相对路径。
