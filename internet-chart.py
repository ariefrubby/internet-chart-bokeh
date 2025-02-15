from bokeh.plotting import figure, show
from bokeh.models import DatetimeTickFormatter
from datetime import datetime

file = open('soal_chart_bokeh.txt', 'r')
content = file.read()
lines = content.count("\n")
chart_date_time = []
chart_speed = []
date_time_label = []

def time_lines():
    i = 0
    for x in range(i,lines,22):
        time_line_num = content.rstrip().split('\n')[x]
        date_time_str = str(time_line_num.split()[1] + ' ' + time_line_num.split()[2])
        adjusted_date_time = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
        chart_date_time.append(adjusted_date_time)
        date_time_label.append(date_time_str)
    return chart_date_time, date_time_label

def speed_lines():
    i = 16
    for x in range(i,lines,22):
        speed_line_num = content.rstrip().split('\n')[x]
        speed = float(speed_line_num.split()[4])
        chart_speed.append(float(speed))
    return chart_speed

chart_date_time, date_time_label = time_lines()
chart_speed = speed_lines()

p = figure(title="Testing Jaringan",x_axis_type='datetime', x_axis_label="DATE TIME", y_axis_label="Speed (Mbps)",sizing_mode="stretch_width")
p.line(x=chart_date_time, y=chart_speed, line_width=2)
p.xaxis.formatter = DatetimeTickFormatter(
    seconds = "%F %T",
    minutes = "%F %T",
    hours = "%F %T",
    days = "%F %T",
    months = "%F %T",
    years="%F %T")

show(p)

file.close()