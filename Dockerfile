
# 基础镜像信息
FROM registry.local/factory/pythonbase:1.0
# 创建目录
RUN mkdir -p /usr/local/ph
# 拷贝文件
ADD ./ /usr/local/ph
# 设置工作目录
WORKDIR /usr/local/ph
# 安装requirements
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501
ENTRYPOINT ["streamlit", "run"]
 
CMD ["streamlit_app.py"]
COPY . /app
