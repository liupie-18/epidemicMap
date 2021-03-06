import map_draw 
import json

map = map_draw.Draw_map()


#国家中英文对照字典    
couDic = {'新加坡': 'Singapore Rep.',
        '多米尼加': 'Dominican Rep.', 
        '巴勒斯坦': 'Palestine', 
        '巴哈马': 'The Bahamas', 
        '东帝汶': 'East Timor', 
        '阿富汗': 'Afghanistan', 
        '几内亚比绍': 'Guinea Bissau',
        '科特迪瓦': "Côte d'Ivoire", 
        '锡亚琴冰川': 'Siachen Glacier', 
        '英属印度洋领土': 'Br. Indian Ocean Ter.', 
        '安哥拉': 'Angola', 
        '阿尔巴尼亚': 'Albania', 
        '阿拉伯联合酋长国': 'United Arab Emirates', 
        '阿根廷': 'Argentina', 
        '亚美尼亚': 'Armenia', 
        '法属南半球和南极领地': 'French Southern and Antarctic Lands', 
        '澳大利亚': 'Australia', 
        '奥地利': 'Austria', 
        '阿塞拜疆': 'Azerbaijan', 
        '布隆迪': 'Burundi', 
        '比利时': 'Belgium', 
        '贝宁': 'Benin', 
        '布基纳法索': 'Burkina Faso', 
        '孟加拉国': 'Bangladesh', 
        '保加利亚': 'Bulgaria', 
        '波斯尼亚和黑塞哥维那': 'Bosnia and Herz.', 
        '白俄罗斯': 'Belarus', 
        '伯利兹': 'Belize', 
        '百慕大': 'Bermuda', 
        '玻利维亚': 'Bolivia',
        '巴西': 'Brazil', 
        '文莱': 'Brunei', 
        '不丹': 'Bhutan', 
        '博茨瓦纳': 'Botswana', 
        '中非': 'Central African Rep.', 
        '加拿大': 'Canada', 
        '瑞士': 'Switzerland', 
        '智利': 'Chile', 
        '中国': 'China', 
        '象牙海岸': 'Ivory Coast', 
        '喀麦隆': 'Cameroon', 
        '刚果（金）': 'Dem. Rep. Congo', 
        '刚果（布）': 'Congo', 
        '哥伦比亚': 'Colombia', 
        '哥斯达黎加': 'Costa Rica', 
        '古巴': 'Cuba', 
        '北塞浦路斯': 'N. Cyprus', 
        '塞浦路斯': 'Cyprus',
        '捷克': 'Czech Rep.', 
        '德国': 'Germany', 
        '吉布提': 'Djibouti', 
        '丹麦': 'Denmark', 
        '阿尔及利亚': 'Algeria', 
        '厄瓜多尔': 'Ecuador', 
        '埃及': 'Egypt', 
        '厄立特里亚': 'Eritrea', 
        '西班牙': 'Spain', 
        '爱沙尼亚': 'Estonia', 
        '埃塞俄比亚': 'Ethiopia', 
        '芬兰': 'Finland', 
        '斐济': 'Fiji', 
        '福克兰群岛': 'Falkland Islands', 
        '法国': 'France', 
        '加蓬': 'Gabon', 
        '英国': 'United Kingdom', 
        '格鲁吉亚': 'Georgia', 
        '加纳': 'Ghana', 
        '几内亚': 'Guinea', 
        '冈比亚': 'Gambia', 
        '赤道几内亚': 'Eq. Guinea', 
        '希腊': 'Greece', 
        '格陵兰': 'Greenland', 
        '危地马拉': 'Guatemala', 
        '法属圭亚那': 'French Guiana', 
        '圭亚那': 'Guyana', 
        '洪都拉斯': 'Honduras', 
        '克罗地亚': 'Croatia', 
        '海地': 'Haiti', 
        '匈牙利': 'Hungary', 
        '印度尼西亚': 'Indonesia', 
        '印度': 'India', 
        '爱尔兰': 'Ireland', 
        '伊朗': 'Iran', 
        '伊拉克': 'Iraq', 
        '冰岛': 'Iceland', 
        '以色列': 'Israel', 
        '意大利': 'Italy', 
        '牙买加': 'Jamaica', 
        '约旦': 'Jordan',
        '日本': 'Japan', 
        '哈萨克斯坦': 'Kazakhstan', 
        '肯尼亚': 'Kenya', 
        '吉尔吉斯斯坦': 'Kyrgyzstan', 
        '柬埔寨': 'Cambodia', 
        '韩国': 'Korea', 
        '科索沃': 'Kosovo', 
        '科威特': 'Kuwait',
        '老挝': 'Lao PDR', 
        '黎巴嫩': 'Lebanon', 
        '利比里亚': 'Liberia', 
        '利比亚': 'Libya', 
        '斯里兰卡': 'Sri Lanka', 
        '莱索托': 'Lesotho', 
        '立陶宛': 'Lithuania', 
        '卢森堡': 'Luxembourg', 
        '拉脱维亚': 'Latvia', 
        '摩洛哥': 'Morocco', 
        '摩尔多瓦': 'Moldova', 
        '马达加斯加': 'Madagascar', 
        '墨西哥': 'Mexico', 
        '马其顿': 'Macedonia', 
        '马里': 'Mali', 
        '缅甸': 'Myanmar', 
        '黑山': 'Montenegro', 
        '蒙古国': 'Mongolia', 
        '莫桑比克': 'Mozambique', 
        '毛里塔尼亚': 'Mauritania', 
        '马拉维': 'Malawi', 
        '马来西亚': 'Malaysia', 
        '纳米比亚': 'Namibia', 
        '新喀里多尼亚': 'New Caledonia', 
        '尼日尔': 'Niger', 
        '尼日利亚': 'Nigeria', 
        '尼加拉瓜': 'Nicaragua', 
        '荷兰': 'Netherlands', 
        '挪威': 'Norway', 
        '尼泊尔': 'Nepal', 
        '新西兰': 'New Zealand',
        '阿曼': 'Oman', 
        '巴基斯坦': 'Pakistan',
        '巴拿马': 'Panama', 
        '秘鲁': 'Peru', 
        '菲律宾': 'Philippines', 
        '巴布亚新几内亚': 'Papua New Guinea', 
        '波兰': 'Poland', 
        '波多黎各': 'Puerto Rico', 
        '朝鲜': 'Dem. Rep. Korea', 
        '葡萄牙': 'Portugal', 
        '巴拉圭': 'Paraguay',
        '卡塔尔': 'Qatar', 
        '罗马尼亚': 'Romania', 
        '俄罗斯': 'Russia', 
        '卢旺达': 'Rwanda', 
        '西撒哈拉': 'W. Sahara', 
        '沙特阿拉伯': 'Saudi Arabia', 
        '苏丹': 'Sudan', 
        '南苏丹': 'S. Sudan', 
        '塞内加尔': 'Senegal', 
        '所罗门群岛': 'Solomon Is.', 
        '塞拉利昂': 'Sierra Leone', 
        '萨尔瓦多': 'El Salvador', 
        '索马里兰': 'Somaliland', 
        '索马里': 'Somalia',
        '塞尔维亚': 'Serbia', 
        '苏里南': 'Suriname', 
        '斯洛伐克': 'Slovakia',
        '斯洛文尼亚': 'Slovenia', 
        '瑞典': 'Sweden', 
        '斯威士兰': 'Swaziland', 
        '叙利亚': 'Syria', 
        '乍得': 'Chad', 
        '多哥': 'Togo', 
        '泰国': 'Thailand', 
        '塔吉克斯坦': 'Tajikistan', 
        '土库曼斯坦': 'Turkmenistan', 
        '特里尼达和多巴哥': 'Trinidad and Tobago', 
        '突尼斯': 'Tunisia', 
        '土耳其': 'Turkey', 
        '坦桑尼亚': 'Tanzania', 
        '乌干达': 'Uganda', 
        '乌克兰': 'Ukraine', 
        '乌拉圭': 'Uruguay', 
        '美国': 'United States', 
        '乌兹别克斯坦': 'Uzbekistan', 
        '委内瑞拉': 'Venezuela', 
        '越南': 'Vietnam', 
        '瓦努阿图': 'Vanuatu', 
        '西岸': 'West Bank', '也门': 'Yemen',
        '南非': 'South Africa',
        '赞比亚': 'Zambia', 
        '津巴布韦': 'Zimbabwe',
         '马尔代夫':'Maldives', 
         '巴林':'Bahrain',
         '马恩岛':'Isle of Man' ,
         '法罗群岛': 'Faeroe Is.',
         '马耳他': 'Malta',
         '梵蒂冈':'Vatican',
         '直布罗陀':'Gibraltar',
         '列支敦士登': 'Liechtenstein',
         '波黑':'Bosnia and Herzegovina',
         '格陵兰岛': 'Greenland',
         '中非共和国':'Central African Rep.' 
         }



# 获取数据
with open('data_cn.json', 'r') as file:
    data_cn = file.read()
    data_cn = json.loads(data_cn)

with open('data_glo.json', 'r') as file:
    data_glo = file.read()
    data_glo = json.loads(data_glo)    

# 中国疫情地图
def  china_map(conf_cn,update_time):
    pro = []
    confirmed_pro = []
    for each in data_cn:
        pro.append(each['area'])
        confirmed_pro.append(each['confirmed'])
    map.to_map_china(pro,confirmed_pro,conf_cn,update_time)



# 省份疫情地图
def province_map(update_time):
    for each in data_cn:
        city = []
        confirmed_city = []
        province = each['area']
        for each_city in each['subList']:
            city.append(each_city['city']+"市")
            confirmed_city.append(each_city['confirmed'])
            map.to_map_city(city,confirmed_city,province,update_time)
        if province == '上海' or '北京' or '天津' or '重庆':
            for each_city in each['subList']:
                city.append(each_city['city'])
                confirmed_city.append(each_city['confirmed'])
                map.to_map_city(city,confirmed_city,province,update_time)
                
#世界疫情地图
def world_map(confirmed_glo, confirmed_cn,update_time):
    country = []
    confirmed_cou = []
    for each in data_glo:
        if each !="其他" and each !="热门":
            for cou in each['subList']:
                if cou['country'] in couDic:
                    country.append(couDic[cou['country']])
                    confirmed_cou.append(cou['confirmed'])
    #添加中国数据
    country.append('China')
    confirmed_cou.append(confirmed_cn)
            
    map.to_map_world(country,confirmed_cou,confirmed_glo,update_time) 
           

                
                

