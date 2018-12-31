"""wcount.py: count words from an Internet file.

__author__ = "袁长峰"
__pkuid__  = "1800011838"
__email__  = "1575163967@qq.com"
"""

import sys
from urllib.request import urlopen
from collections import OrderedDict

def wcount(lines,topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
    doc = urlopen(lines)
    docstr = doc.read()
    doc.close()
    txt = docstr.decode()   #获得文档，命名为txt
    
    turn1=txt.maketrans('~`!@#$%^&*)(}{][:;"?/\|<>,.=+_"','                               ') #将特殊符号替换为空格
    txt=txt.translate(turn1)
    turn2=txt.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')    #将大写转化为小写
    txt=txt.translate(turn2)
    txt=txt.split()
    
    ans={}  #建立一个列表，储存得到的数据
    for i in txt:
        ans[i] = ans.get(i, 0)+1
    ans_list=sorted(ans.items(),key=lambda x:x[1],reverse=True)  #对得到的数据根据出现次数大小降序排列
    ans_dict=dict(ans_list) 
    print(ans_dict)
    if topn <= len(ans):
        for (i,v) in ans_list[:topn]:
              print(i,'   ',v)
    else:
        for (i,v) in ans_dict.items():
            print(i,'   ',v)
def main():
    wcount('http://www.gutenberg.org/cache/epub/19033/pg19033.txt',7999999)
    
if __name__ == '__main__':
    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)
    main()
    # your code goes here
    # should anayze whether paras are right or not
