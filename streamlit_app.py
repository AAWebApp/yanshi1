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
#预加载标题及链接可修改
shhwj=open("浙江省人民政府门户网站 省政府行政规范性文件.json",'r',encoding='utf-8')
shhwj=json.load(shhwj)
shtitle=[]
shurl=[]
shtime=[]
d={}
for i in shhwj:
    shtitle.append(i['标题'])
    shurl.append(i['标题链接'])
shtitle2=[]
for i in shtitle:
    i=i.split(' ')
    
    shtitle2.append(i[len(i)-1])
for i2 in shtitle2:
    q1=jieba.lcut(i2)
   
    for i in q1:
        if len(i)==1:
            continue
        a=d.get(i,0)
        d[i]=a+1#计算i有多少个
        

n=list(d.items())
n.sort(key=lambda x:x[1],reverse=True)
chunktitles=[]
for i in range(len(n)):
    q,w=n[i]
    chunktitles.append(q)
#1
ge = st.radio('模式选择',('搜索模式','筛选模式'))
if ge=='搜索模式':
    put = str(st.text_input('搜索', '保障性租赁住房'))
    outs=[]
    puts=jieba.lcut(put)
    for i1 in puts:
        for i in shtitle2:
            if len(re.findall(r'{}'.format(i1),i))>0:
                outs.append(i)

        
    option = st.selectbox(
        '您的搜索结果是',
         outs)
    
##
else:
    option1 = st.selectbox(
        '选择领域,地域,人群',
         ['领域','地域','人群'])
    if option1=='领域':
        option2 = st.selectbox(
            '选择细目',
            ['文化保护','水利','安居','土地','工程建设','生态','旅游','养老','教育','就业','农业农村','社会保障救助','其他','医疗','服役'])
        if option2=="文化保护":
            option=st.selectbox(
            '筛选吧',['文物保护','遗址','文化','文化名城','文化遗产','','','','','',''])
        elif option2=="安居":
            option=st.selectbox(
            '筛选吧',['移民','淹没区','城市道路','','','','','','','',''])
        elif option2=="土地":
            option=st.selectbox(
            '筛选吧',['土地利用','占地','','','','','','','','',''])
        elif option2=="工程建设":
            option=st.selectbox(
            '筛选吧',['工程','开发区','城市道路','','','','','','','',''])
        elif option2=="生态":
            option=st.selectbox(
            '筛选吧',['生态县','','','','','','','','','',''])
        elif option2=="旅游":
            option=st.selectbox(
            '筛选吧',['名胜区','','','','','','','','','',''])
        elif option2=="养老":
            option=st.selectbox(
            '筛选吧',['养老','','','','','','','','','',''])
        elif option2=="教育":
            option=st.selectbox(
            '筛选吧',['教育','体育','义务教育','','','','','','','',''])
    elif option1=='地域':
        option = st.selectbox(
            '筛选吧',
            ['浙江省人民政府','浙江','全国','杭州','宁波','湖州','温州','金华','宁海','义乌','临安','钱塘江','衢江','县级','泰顺','舟山群岛','仙霞岭','廊桥','奉化','清溪','嘉兴','港区','台州','越城区','上虞','西林','南浔','龙港','诸暨'])
        
    else:
        option = st.selectbox(
            '筛选吧',['残疾人'])
    outs=[]
    puts=jieba.lcut(option)
    for i1 in puts:
        for i in shtitle2:
            if len(re.findall(r'{}'.format(i1),i))>0:
                outs.append(i)

        
    option = st.selectbox(
        '您的筛选结果是',
             outs)
#2
def padu(url):
        
        news = Article(url, language='zh')
        news.download()        # 加载网页
        news.parse()# 解析网页
        x=news.text
        return x
try:
    ww =padu(shurl[shtitle2.index(option)]).encode('utf-8')
    enre=st.radio('请点击相应的功能后查看',('政策关键词top10','词云图','政策文件','相关信息','政策脉络','政策落地','政策动向可视化'))
except:
    ww='无'.encode('utf-8')
    enre=st.radio('请点击相应的功能后查看',('政策关键词top10','词云图','政策文件','相关信息','政策脉络','政策落地','政策动向可视化'))
if st.button('用户中心'):
    st.balloons()
    st.sidebar.write('用户中心欢迎您')
    uploaded_file = st.sidebar.file_uploader("在此处共享您的信息")
    if uploaded_file is not None:
         # To read file as bytes:
         bytes_data = uploaded_file.getvalue()
         st.sidebar.write(bytes_data)

         # To convert to a string based IO:
         stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
         st.sidebar.write(stringio)

         # To read file as string:
         string_data = stringio.read()
         st.sidebar.write(string_data)

         # Can be used wherever a "file-like" object is accepted:
         dataframe = pd.read_csv(uploaded_file)
         st.sidebar.write(dataframe)
    st.sidebar.write('此处查看其他人的共享：')
    st.sidebar.write('用户123：“简政平台超好用”')
    st.sidebar.write('用户秋叶：给大家推荐一个有用的网站：http://www.gov.cn/zhengce/content/2021-07/02/content_5622027.htm')
    
    
else:
    d1=[]
    st.dataframe()
#2
if enre=='政策关键词top10':
    #h=open("实验1.txt","r",encoding='utf-8').read()
    h=ww
    keys=analyse.extract_tags(h)
    num1=1
    for key in keys:
        if num1<=10:
            st.write(key,'top',num1)
            
            num1+=1
            
        else:
            continue
elif enre=='政策动向可视化':
    chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['住房', '保障', '租赁'])

    st.area_chart(chart_data)

elif enre=='政策文件':
    
    o=ww.decode()
    o=ww.decode()
    o=o.replace('；','。')
    
    k2=o.split('\n\n')
    op1 = st.selectbox(
            '请选择',['政策目录','名词注释'])
    if op1=='政策目录':
        for i in k2:
            i=i.split('。')
            
            if len(i[0])<=17:
                st.sidebar.write(i[0])
    else:
        st.sidebar.write('1、保障性租赁住房保障性：租赁住房主要解决符合条件的新市民、青年人等群体的住房困难问题，以建筑面积不超过70平方米的小户型为主，租金低于同地段同品质市场租赁住房租金')
        st.sidebar.write('2、新市民：最初指的是长期居住在城市并有相对固定工作的农民工，后来这一名词的指代范围逐渐扩大，成为原籍不在当地、因各种原因来到一个城市的各种群体的集合统称。')
        st.sidebar.write('3、基本公共服务：参照《国家基本公共服务标准（2021年版）》')
    st.write(o)
elif enre=='相关信息':
    op2 = st.selectbox(
            '请选择',['相关信息总览','相关政策','相关数据'])
    if op2=='相关信息总览':
        
        import requests
        from bs4 import BeautifulSoup
        import re
        import json
        def getKeywordResult(keyword):
            url = 'https://www.baidu.com/s?wd='+keyword
            try:
                r  = requests.get(url, timeout = 30)
                r.raise_for_status()
                r.encoding = 'utf-8'
                return r.text
            except:
                return ""
        def parserLinks(html):
            soup = BeautifulSoup(html, "html.parser")
            links1 = []
            for div in soup.find_all('div', {'data-tools':re.compile('title')}):
                data = div.attrs['data-tools']
                d = json.loads(data)
                links1.append(d['title'])
                #print(links1)
            links2 = []
            for div in soup.find_all('div', {'data-tools':re.compile('url')}):
                data = div.attrs['data-tools']
                d = json.loads(data)
                links2.append(d['url'])
                #print(links2)
            link=[]
            for i in range(len(links1)):
                link.append(links1[i])
                link.append(links2[i])
                
                
            return link
        def main():
            html = getKeywordResult(option)
            y = parserLinks(html)
            count = 1
            
            for i1 in y:
                st.sidebar.write(i1)
                    
                    
        main()
    elif op2=='相关政策':
        st.sidebar.write('文字解读：《市区保障性租赁住房项目新（改）建操作细则》')
        st.sidebar.write('http://www.qz.gov.cn/art/2021/12/29/art_1229037077_2386671.html')
        st.sidebar.write('嘉兴市人民政府办公室关于加快发展保障性租赁住房的实施意见')
        st.sidebar.write('http://www.nanhu.gov.cn/art/2022/1/7/art_1229516974_2388424.html')
    else:
        st.write('')
        a=json.load(open("cata_19066.json",'r',encoding='utf-8'))
        
        #a=[[1,2,3,4],[5,6,7,8]]#包含两个不同的子列表[1,2,3,4]和[5,6,7,8]
        data=DataFrame(a)#这时候是以行为标准写入的
        st.dataframe(data)
        st.area_chart(data)
elif enre=='政策脉络':
    grn=st.radio('请点击相应的区域后查看',('政策背景','政策目标','国家层面政策发布','省级层面政策发布','地方政策对接情况'))
    if grn=='国家层面政策发布':
        st.write('国务院关于加快发展保障性租赁住房的意见')
    elif grn =='省级层面政策发布':
        st.write('浙江省关于加快发展保障性租赁住房的指导意见')
    elif grn =='地方政策对接情况':
        st.write('杭州市加快发展保障性住房实施方案')
    elif grn =='政策背景':
        o2=open("政策背景1.txt",'r',encoding='utf-8').read()
        st.write(o2)
    else:
        st.write('浙江省将建设120万套保障性租赁住房')
elif enre=='政策落地':
    st.write('杭州市住房保障和房产管理局')
    st.write('http://fgj.hangzhou.gov.cn/col/col1619052/index.html')
    st.write('租赁自住住房提取住房公积金办理')
    st.write('https://www.zjzwfw.gov.cn/zjservice/item/detail/index.do?localInnerCode=41e1e8ea-eb61-48f5-85b7-abf029be5d54&u_atoken=731f467a-8b35-4b3f-ad99-fd3fafba3869&u_asession=01yEvAhJWHpnS-6c3a9gtxSnnHBfUF9zVSYMbgCBeHikNnV6XwWcRNUOapeb90Plk-X0KNBwm7Lovlpxjd_P_q4JsKWYrT3W_NKPr8w6oU7K_IGdFUjyFGi0lfWIz1CfEcN8vRduUQwPh0AKmxeQDfhWBkFo3NEHBv0PZUm6pbxQU&u_asig=05AKYiLESMHAo-kt1XbMg8MpGoKeP6d0p8Mup4GhaqjoumBi3TXo8jBFz9x_QAIoUlcnD6fBMVY03jz2RUng_hI2jUruhNex_M1thmmadBsqe9Ci6TJWiM1mNQTi_inqlmLZo9ADPL5orjvVq2JAHWJgpvm5GtX1r5g-qA-IlnI_39JS7q8ZD7Xtz2Ly-b0kmuyAKRFSVJkkdwVUnyHAIJzS53MuDBrWUTFXn2zNqhndvZrJHnPSS3uS4qaE9iYVLrPwez5KVXjxN4YIJY2x2pxu3h9VXwMyh6PgyDIVSG1W_O6Wlt8QcqaP7WuLOvdCWiHANw4_8BpU31TkZPiPBinl07zGokYqv9a7tWJ7UTdsyDtgVr_VbMWTevp7v4LqaHmWspDxyAEEo4kbsryBKb9Q&u_aref=FIcIy1OQqYjCab5u0cv649awKzo=')
    
    

else:
        # 958条评论数据
    f= padu(shurl[shtitle2.index(option)]).encode('utf-8') 
    data = f.decode()

    # 文本预处理  去除一些无用的字符   只提取出中文出来
    new_data = re.findall('[\u4e00-\u9fa5]+', data, re.S)
    new_data = " ".join(new_data)

    # 文本分词
    seg_list_exact = jieba.cut(new_data, cut_all=True)

    result_list = []
    with open('stop_word.txt', encoding='utf-8') as f:
        con = f.readlines()
        stop_words = set()
        for i in con:
            i = i.replace("\n", "")   # 去掉读取每一行数据的\n
            stop_words.add(i)

    for word in seg_list_exact:
        # 设置停用词并去除单个词
        if word not in stop_words and len(word) > 1:
            result_list.append(word)
    print(result_list)

    # 筛选后统计
    word_counts = collections.Counter(result_list)
    # 获取前100最高频的词
    word_counts_top100 = word_counts.most_common(100)
    print(word_counts_top100)

    # 绘制词云
    my_cloud = WordCloud(
        background_color='white',  # 设置背景颜色  默认是black
        width=900, height=600,
        max_words=100,            # 词云显示的最大词语数量
        font_path='simhei.ttf',   # 设置字体  显示中文
        max_font_size=99,         # 设置字体最大值
        min_font_size=16,         # 设置子图最小值
        random_state=50           # 设置随机生成状态，即多少种配色方案
    ).generate_from_frequencies(word_counts)

    st.set_option('deprecation.showPyplotGlobalUse', False)
    # 显示生成的词云图片
    plt.imshow(my_cloud, interpolation='bilinear')
    # 显示设置词云图中无坐标轴
    #plt.axis('off')
    #plt.show()
    st.pyplot()





