# 说明:
## 一、安装依赖库
* pip install -r requirements.txt

## 二、使用方法
* 修改auto_testing_excel目录中的case.xlsx的用例
* 修改auto_testing_excel目录中的config.py的相关配置
* 安装xlrd/xlwt/requests 
* python \*/auto_testing_excel/test_main.py > myreport.html

## 三、使用的软件
* unittest    单元测试
* HTMLTestRunner=0.8.2    将unittest结果生成html
* requests=2.12.4    http请求
* xlrd=1.0.0    读excel
* xlwt=1.1.2    写excel
