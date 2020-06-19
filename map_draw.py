from pyecharts import options as opts
from pyecharts.charts import Map
import os

class Draw_map():
   
    def __init__(self):
        if not os.path.exists('./map/china'):
            os.makedirs('./map/china')


    def to_map_city(self, city, variate,province,update_time):
        #pices定义数据分段
        pieces = [
            {"max": 59999, "min": 10000, "label": ">10000", "color": "#990033"},
            {"max": 9999, "min": 5000, "label": "5000-9999", "color": "#CC0033"},
            {"max": 4999, "min": 1000, "label": "1000-4999", "color": "#FF0033"},
            {"max": 999, "min": 100, "label": "100-999", "color": "#FF6633"},
            {"max": 99, "min": 50, "label": "50-99", "color": "#FF9900"},
            {"max": 49, "min": 10, "label": "10-49", "color": "#FFCC66"},
            {"max": 9, "min": 1, "label": "1-9", "color": "#FFFFCC"},
            {"max": 0, "min": 0, "label": "0", "color": "#FFFFFF"},
              ]

        
        c = (
            # 设置地图大小
            Map(init_opts=opts.InitOpts(width = '1000px', height='880px'))
            .add("累计确诊人数", 
                 [list(z) for z in zip(city, variate)], 
                 province, is_map_symbol_show=False)
            #设置不显示市级名称
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            # 设置全局变量  
            .set_global_opts(
                title_opts=opts.TitleOpts(title="%s地区疫情地图分布"%(province), 
                                          subtitle = '截止%s  %s省疫情分布情况'%(update_time,province), 
                                          pos_left = "center", pos_top = "10px"),
                legend_opts=opts.LegendOpts(is_show = False),
                visualmap_opts=opts.VisualMapOpts(max_=200,is_piecewise=True,
                                                  pieces=pieces,
                                                  ),
            )
            .render("./map/china/{}疫情地图.html".format(province))
        )

    def to_map_china(self,province, variate,conf_cn,update_time):
        pieces = [
            {"max": 99999, "min": 10000, "label": ">10000", "color": "#8A0808"},
            {"max": 9999, "min": 1000, "label": "1000-9999", "color": "#B40404"},
            {"max": 999, "min": 100, "label": "100-999", "color": "#DF0101"},
            {"max": 99, "min": 10, "label": "10-99", "color": "#F78181"},
            {"max": 9, "min": 1, "label": "1-9", "color": "#F5A9A9"},
            {"max": 0, "min": 0, "label": "0", "color": "#FFFFFF"},
                  ]

        c = (
            # 设置地图大小
            Map(init_opts=opts.InitOpts(width='1000px', height='880px'))
                .add("累计确诊人数", 
                     [list(z) for z in zip(province, variate)], 
                     "china", 
                     is_map_symbol_show=False)
                .set_global_opts(
                title_opts=opts.TitleOpts(title="中国疫情地图分布", 
                                          subtitle='截止{0} 中国已确诊人数为{1}'.format(update_time,conf_cn),                                                       pos_left="center", pos_top="10px"),
                legend_opts=opts.LegendOpts(is_show=False),
                visualmap_opts=opts.VisualMapOpts(max_=200, is_piecewise=True,
                                                  pieces=pieces,
                                                  ),
            )
                .render("./map/中国疫情地图.html")
        )
        
        
    def to_map_world(self,country,variate,confirmed_glo,update_time):
        pieces = [   
            {"max": 9999999, "min": 1000000, "label": ">1000000", "color": "#990033"},
            {"max": 999999, "min": 100000, "label": "100000-999999", "color": "#CC0033"},
            {"max": 99999, "min": 10000, "label": "10000-99999", "color": "#FF0033"},
            {"max": 9999, "min": 1000, "label": "1000-9999", "color": "#FF6633"},
            {"max": 999, "min": 100, "label": "100-999", "color": "#FF9900"},
            {"max": 99, "min": 10, "label": "10-99", "color": "#FFCC66"},
            {"max": 9, "min": 1, "label": "1-9", "color": "#FFFFCC"},
            {"max": 0, "min": 0, "label": "0", "color": "#FFFFFF"},
                  ]
        c = (
            # 设置地图大小
            Map(init_opts=opts.InitOpts(width='1000px', height='880px'))
                .add("累计确诊人数", 
                     [list(z) for z in zip(country, variate)], 
                     "world", 
                     is_map_symbol_show=False)
                #设置不显示国家名称
                .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
                .set_global_opts(
                title_opts=opts.TitleOpts(
                    title="世界疫情地图分布", 
                    subtitle='截止{0}世界已确诊人数{1}'.format(update_time,confirmed_glo),                                                     pos_left="center", pos_top="10px"),
                legend_opts=opts.LegendOpts(is_show=False),
                visualmap_opts=opts.VisualMapOpts(max_=200, 
                                       is_piecewise=True,
                                       pieces=pieces,
                                                  ),
            )
                .render("./map/世界疫情地图.html")
        )