from get_data import Get_data
import os

data = Get_data()
data.get_data()

time_cn,time_glo = data.get_time()
confirmed_cn,confirmed_glo = data.parse_data()

#绘制地图
import execution
execution.province_map(time_cn)
execution.china_map(confirmed_cn,time_cn)
execution.world_map(confirmed_glo,confirmed_cn,time_glo)

#删除过程文件
os.remove('html.txt')
os.remove('data_cn.json')
os.remove('data_glo.json')
