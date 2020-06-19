import requests
from lxml import etree
import json
import re
import openpyxl


class Get_data():
    def get_data(self):
        # 目标url
        url = "https://voice.baidu.com/act/newpneumonia/newpneumonia/"

        # 伪装请求头
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/80.0.3987.149 Safari/537.36 '
        }

        # 发出get请求
        response = requests.get(url,headers=headers)

        # 将请求的结果写入文件,便于后续处理
        with open('html.txt', 'w') as file:
            file.write(response.text)

    def get_time(self):
        with open('html.txt','r') as file:
            text = file.read()
        # 获取更新时间
        time_cn = re.findall('"mapLastUpdatedTime":"(.*?)"',text)[0]
        time_glo = re.findall('"foreignLastUpdatedTime":"(.*?)"',text)[0]
        print('国内疫情更新时间为 '+time_cn)
        print('国外疫情更新时间为 '+time_glo)
        return time_cn,time_glo
  
        
    def parse_data(self):
        with open('html.txt','r') as file:
            text = file.read()
        # 生成HTML对象
        html = etree.HTML(text)
        
        # 处理数据
        result = html.xpath('//script[@type="application/json"]/text()')
        result = result[0]
        result = json.loads(result)
        
        #国内累计感染人数
        confirmed_cn =int(result['component'][0]['summaryDataIn']['confirmed'])
        #世界累计感染人数
        confirmed_glo =int(result['component'][0]['summaryDataOut']['confirmed'])
        
        #国内数据
        result_cn = json.dumps(result['component'][0]['caseList'])
        #国外数据
        result_glo = json.dumps(result['component'][0]['globalList'])  
        
        with open('data_cn.json','w') as file:
            file.write(result_cn)
            print('国内数据已写入json文件...')
        
        with open('data_glo.json','w') as file:
            file.write(result_glo)
            print('国外数据已写入json文件...')

        response = requests.get("https://voice.baidu.com/act/newpneumonia/newpneumonia/")
        # 将请求的结果写入文件,便于分析
        with open('html.txt', 'w') as file:
            file.write(response.text)

        # 获取时间
        time_cn = re.findall('"mapLastUpdatedTime":"(.*?)"', response.text)[0]
        time_glo = re.findall('"foreignLastUpdatedTime":"(.*?)"', response.text)[0]
        print(time_cn)
        print(time_glo)

        # 生成HTML对象
        html = etree.HTML(response.text)
        # 解析数据
        result = html.xpath('//script[@type="application/json"]/text()')
        
        result = result[0]
       
        result = json.loads(result)
       
        # 以每个省的数据为一个字典
        data_cn = result['component'][0]['caseList']
       

        data_glo = result['component'][0]['globalList']
      
        
        # 将得到的数据写入excel文件
        # 创建一个工作簿
        wb = openpyxl.Workbook()
        # 创建工作表,每一个工作表代表一个area
        ws_cn = wb.active
        ws_cn.title = "国内疫情"
        ws_cn.append(['省份', '累计确诊', '死亡', '治愈', '现有确诊', '累计确诊增量', '死亡增量', '治愈增量', '现有确诊增量'])
        for each in data_cn:
            ws_cn.append([each['area'], each['confirmed'], 
                         each['died'], each['crued'], each['curConfirm'],
                         each['confirmedRelative'], each['diedRelative'], 
                         each['curedRelative'],each['curConfirmRelative']])

        # 获取国外疫情数据
        for each in data_glo:
            
            sheet_title = each['area']
            # 创建一个新的工作表
            ws_glo = wb.create_sheet(sheet_title)
            ws_glo.append(['国家', '累计确诊', '死亡', '治愈', '现有确诊', '累计确诊增量'])
            for country in each['subList']:
              
                ws_glo.append([country['country'], country['confirmed'], 
                              country['died'], country['crued'],
                             country['curConfirm'], country['confirmedRelative']])

        # 保存excel文件
        wb.save('./data.xlsx')
        return confirmed_cn ,confirmed_glo
