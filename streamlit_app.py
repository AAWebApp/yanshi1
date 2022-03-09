import jieba
import collections
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import streamlit as st
from jieba import analyse
from annotated_text import annotated_text
import json
from newspaper import Article
import pandas as pd
from pandas.core.frame import DataFrame
import numpy as np
st.title("简政")
"""
欢迎进入简政！在这里我们将和您一起汇集政策资讯
"""

from LAC import LAC
lac = LAC(mode='lac')
from annotated_text import annotated_text
def yuchuli(x):
    ls=''
    for line in x:  #打开文件
        rs = line.rstrip('\n')  # 移除行尾换行符
      # 输出移除后的行
        ls+=rs
    return ls
def fenju(x):#x is 'xxxx。xxxxx。xxxx....'
    x=x.split('。')
o=open('演示文本1.txt','r',encoding='utf-8').read()
q=lac.run(yuchuli(o))
p=q[0]
p2=q[1]
d={}
for i in range(len(p)):
    if p2[i]=='nr'or p2[i]=='nz'or p2[i]=='PER'or p2[i]=='LOC'or p2[i]=='ORG'or p2[i]=='nt'or p2[i]=='nw'or p2[i]=='ns':
        #print(p[i],p2[i])
        z=p[i].replace('。','')
        z=z.replace(',','')
        for i2 in range(0,10):
            z=z.replace('{0}'.format(i2),'')
        
        d[z]=p2[i]
li=list(d.keys())

option1 = st.sidebar.selectbox(
        '选择关键词',
         li)

for i in range(len(p)):
    if option1==p[i]:
        annotated_text(p[i], "#8ef")
            
    else:
        st.write(p[i],end='')
