import streamlit as st
import streamlit.components.v1 as components
import json
st.set_page_config(page_title="简政(演示模型)",)
def videoplay(filename):
    video_file = open(filename, 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes)

'''
'''
##init
s=   '''通告二
            发布时间：2021-12-10 
            各相关单位：

              根据工作安排，凡准备参与2021年“试点在五个新城和自贸区新片区就业的本市应届研究生毕业生符合基本条件可直接落户的政策”用人单位，可以根据下列方式至对应新城和新片区受理点进行单位资质申报。申报时间统一为即日起至2021年12月24日。

            一、临港新片区及南汇新城

              临港新片区国际人才服务港二楼12号综合窗口（紫杉路158弄A1座）。周一至周五，9:00-11:30,13:30-16:30。咨询电话：68289698-8069，金老师。

            二、嘉定新城

              嘉定区嘉戬公路118号三楼就业人才专区E01窗口。周一至周五，9:00-11:30,13:00-17:00。咨询电话：69530382-802，朱老师。

            三、青浦新城

              青浦区北青公路8098号二楼综合窗口1-4号窗口。周一至周四：9:00-11:30,13:30-16:30 ；周五：9:00-11:30,13:30-15:30。咨询电话：33862073，唐老师。

            四、松江新城

              通过所在街镇园区申报，核实形成确认名单后报区人才服务中心。周一至周五，9：00-11:00,13:30-16:30。咨询电话：37043013，华老师;57657037,阮老师。

            五、奉贤新城

              奉贤区望园南路1529弄B楼二层。周一至周五，8：30-11:30,13:00-16:30。咨询电话：67137757、67137800，褚老师、陆老师。

             

            上海市学生事务中心

        2021年12月10日
        '''
s2= '''
            通告
            发布时间：2021-11-29 


            为贯彻本市相关会议精神，推进本市高质量人才高地建设，加大吸引人才支持力度，特别是支持“五个新城”建设招揽人才。经上海市高校招生和就业工作联席会议研究，决定开放第二批2021年非上海生源应届普通高校毕业生进沪就业落户受理工作，并试点在五个新城和自贸区新片区就业的本市应届研究生毕业生符合基本条件可直接落户的政策。受理时间为2021年12月1日至12月31日（工作日）。

            特此通告。

             

            上海市学生事务中心

            2021年11月29日
         '''
vue="10000+"
def jsadd(file,dic):

    import json

    a_dict = dic

    with open(file) as f:
        data = json.load(f)

    data.update(a_dict)

    with open(file, 'w') as f:
        json.dump(data, f)
###
###开启简政
tt4=''
ojyc1=open("jyc1.txt",'r',encoding='utf-8').read()
text1=ojyc1
tt6='2021年非上海生源应届普通高校毕业生进沪就业申请本市户籍办法'
tt2='2021年非上海生源应届普通高校毕业生进沪就业申请本市户籍办法'
a1=st.sidebar.checkbox('开启简政')
@st.cache(suppress_st_warning=True)
def cach2():

    ojyc1=text1
    tt2=tt6
@st.cache(suppress_st_warning=True)
def cach():
    tt_source=tt4
    tt_title=tt3
    tt_text=text2

###
###after 开启简政
if a1:
    ##
    a2=st.checkbox('点击开启筛选')
    a3=st.checkbox('快速打开词典')
    ##

    if a3:
        t1=st.sidebar.text_input('输入你想查找的词语', '')
        tt_title='*********'
        tt_source='***********'
        tt_text='**********'
        if t1=="落户基本条件":
            
            
            
            radi=st.sidebar.radio('',('查看该词条','新建词条','我要编辑此词条'))
                
            if radi=='新建词条':
                with st.sidebar.form("词条"):
                    uploaded_file = st.file_uploader("此处上传视频文件")
                    
                    tt3=st.text_input('输入词条名称','')
                    text2=st.text_area('输入正文','')
                    tt4=st.text_input('输入来源政策','')
                    sub4 = st.form_submit_button("创建完毕")
                if sub4:
                    jsadd("D:\桌面\python 简政\datadic.json",{tt3:[text2,tt4]})

                    
                        
            elif radi=='我要编辑此词条':
                with st.sidebar.form("词条"):
                    text1=st.text_area('',ojyc1,height=500)
                    tt6=st.text_input('来源政策文件','2021年非上海生源应届普通高校毕业生进沪就业申请本市户籍办法')
                    sub3 = st.form_submit_button("确定")
                if sub3:
                    
                    tt2=tt6
                    ojyc1=text1
            else:
                
                with st.sidebar.form("词条"):
           
                    sub2 = st.form_submit_button("点赞")

                    video_file = open("jyc.MP4", 'rb')
                    video_bytes = video_file.read()
                    
                    st.video(video_bytes)
                    ojyc1
                    '来源政策文件：'
                    
                    
                    with st.expander(tt2):
                        ''

        else:
            try:
                ojyc2=open("datadic.json",'r',encoding='utf-8')
                ojyc2=json.load(ojyc2)
                with st.sidebar.form("词条"):
                    sub2 = st.form_submit_button("点赞")
                            
                    t1
                    "****************"
                    ojyc2[t1][0]
                    '来源政策文件：'
                    with st.expander(ojyc2[t1][1]):
                        ''
            except:
                ''
                
                    

###shaixuan           
    if a2:
        
        
        import numpy as np
        option = st.sidebar.selectbox(
         '选择地区',
         ('','上海', '浙江省', '广东省'))
        option2=st.sidebar.selectbox(
         '选择领域',
         ('','教育', '就业','养老',''))
        option3=st.sidebar.selectbox(
            '选择人群',
            ('','应届高校毕业学生','待业人员',))
        numm=np.random.randn(300,3)
        if option=='上海':
            numm=numm[150:]
            vue='<1500'
            if option2=='就业':
                numm=numm[70:]
                vue='<300'
                if option3=='应届高校毕业学生':
                    numm=numm[55:]
                    vue='<100'

            # Every form must have a submit button.
            
        st.write("您所选的地区是",option,'，领域是',option2,'，人群是',option3)
        import pandas as pd
        
        import altair as alt
        import streamlit as st
        import warnings
        warnings.filterwarnings("ignore")
        
        df = pd.DataFrame(
             numm,
             columns=['a', 'b', 'c'])

        c = alt.Chart(df).mark_circle().encode(
             x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
        st.write('当前样本数量的估计值',vue)
        try:
            st.altair_chart(c, use_container_width=True)
        except:
            ''
###
        
### txt input area    
    txt = st.text_area('输入你想搜索的内容', '')
###    
### init col       
    col1, col2 = st.columns([3, 1])
###
    ## after inputing
    if txt=='落户':
        
        y=3
        a97=st.checkbox('百度搜索结果')
        a99=st.checkbox('政策篇章结构')
        if a99:
            lsjyc=[]
         
            
            def f(s):
                ss=s.split()
                for i in range(len(ss)):
                    try:
                        if len(ss[i])<=13 and len(ss[i+1])>13:
                            with st.expander(ss[i]):
                                try:
                                    for i2 in range(3):
                                        if len(ss[i+i2])>13:
                                            ss[i+i2]
                                        else:
                                            ''
                                except:
                                    ''
                        elif len(ss[i])<=13:
                            ss[i]
                        
                            
                    except:
                        ss[i]
            '**********************'
            2
            f(s)
            def f2(x,y):
                with expander(x):
                    y

            
                
                
            
            '**********************'
            1
            f(s2)
            
                            
        if a97:
            from PIL import Image
            image = Image.open("Screenshot_20220319_223003_com.baidu.searchbox(1).jpg")

            st.image(image, caption='Sunrise by the mountains')
                                    
        else:
            with st.expander("*政策链-0087*  直接落户  应届研究生毕业生 试点 五个新城 自贸区新片区,时间：2021-11-29/2021-12-10 "):
            
                '**********************'
                2
                s
                '**********************'
                1
                s2
                
                
                
                '************************'
           
                '**************************'
                '*****************************'
                '名词解释：'
                a5=st.checkbox('非上海生源')
                if a5:
                    '是指籍贯不是上海本地的大学生。'
                a6=st.checkbox('五个新城')
                if a6:
                    '嘉定、青浦、松江、奉贤、南汇等五个新城'
                    
                    
                a7=st.checkbox('自贸区新片区')
                if a7:
                    '''中国（上海）自由贸易试验区临港新片区在上海大治河以南、金汇港以东以及小洋山岛、浦东国际机场南侧区域。
    新片区的开发利用须遵守土地、无居民海岛利用和生态环境、城乡规划等法律法规，并符合节约集约利用资源的有关要求；支持按照国家相关法规和程序，办理合理必需用海。
    '''

                           
                    
            
                
                    
            with st.expander('*政策链-0089* 就业 非上海生源应届普通高校毕业生 进沪 ,时间：2021-06-09'):
                ''

   #
a89=st.sidebar.checkbox('我的订阅')
if a89:
    
    enre=st.sidebar.radio(('请选择相应的功能'),('订阅','我的邮箱'))
    if enre=="订阅":
        st.title("订阅")
        op=st.selectbox(
            '选择功能',

             ['按照地区订阅','按照机构订阅','按照关键词订阅','按照政策分类订阅','综合订阅'])
        if op=='按照地区订阅':
        
            option2 = st.selectbox(
                '选择地区',

                 ['黄浦区','徐汇区'])

        elif op=='按照机构订阅':
            option3 = st.selectbox(
                '选择机构',

                 ['上海市政府','上海市发展与改革委员会'])

        elif op=='按照关键词订阅':
            sou=st.text_input('输入你关心的关键词', '保障性租赁住房')
            
        elif op=='按照政策分类订阅':
            option4 = st.selectbox(
                '选择分类',

                 ['住房','就业'])

        elif op=='综合订阅':
            options = st.multiselect(
             '点击你需要的',
             ['残疾人', '住房', '发展与改革委员会', '黄浦区'],
             [])
        
        
        if st.button('确认订阅'):
            st.write('订阅成功！以后将及时提醒您')
    else:
        st.title("我的订阅接收邮箱")
        col1, col2, col3 = st.columns(3)
        with st.container():
            with col1:
                st.write("您订阅的关于“住房”的政策")
                with st.expander("最新信息*"):
                    o=open("演示文本1.txt",'r',encoding='utf-8').read()
                    o

            with col2:
                st.write("您订阅的关于“黄浦区”的政策")
                with st.expander("暂无信息"):
                    o=open("演示文本1.txt",'r',encoding='utf-8').read()
                    o

            with col3:
                st.write("您订阅的关于“黄浦区”“发展与改革委员会”的政策")
                with st.expander("暂无信息"):
                    o=open("演示文本1.txt",'r',encoding='utf-8').read()
                    o
                


