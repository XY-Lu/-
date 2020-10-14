import xlrd
from pyecharts import options as opts
from pyecharts.charts import Bar
wb=xlrd.open_workbook(r'C:\Users\uLtra\Desktop\中非贸易总览.xls')
xl=wb.sheet_by_index(0)
l1=xl.row_values(0,4,11)
s1=xl.row_values(1,4,11)
s2=xl.row_values(2,4,11)
s3=xl.row_values(3,4,11)
s4=xl.row_values(4,4,11)
s5=xl.row_values(5,4,11)
bar=(
    Bar()
    .add_xaxis(l1)
    .add_yaxis("阿尔及利亚",s1)
    .add_yaxis("安哥拉",s2)
    .add_yaxis("尼日利亚",s3)
    .add_yaxis("南非",s4)
    .add_yaxis("埃及",s5)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="前五"),
        xaxis_opts=opts.AxisOpts(name="年份"),
        yaxis_opts=opts.AxisOpts(name="金额"),
        )
    )
bar.render("中非数据柱形图（前五）.html")
a=open('./中非数据柱形图（前五）.html','r',encoding="utf-8")
b=a.read()
print(b)