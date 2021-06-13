"""
Package to create Line charts. To make a simple line chart, go to https://sid72020123.github.io/pyhtmlchart/#making-line-chart
"""
import os
import time


class LineChart:
    def __init__(self, location, title='Chart', background_color='White', legend_position='right', width=900,
                 height=500, chart_actions=False,
                 y_axis_title='Y', x_axis_title='X', color=None, line_width=2, print_log=False):
        """
        Class to make a Line Chart!
        :param location: The Location in which the chart is stored as a '.html' file.
        :param title: The Main Title of the Chart.
        :param background_color: The background color of the chart.
        :param legend_position: The position of the legend in the chart(use values like --> 'top', 'bottom', 'right')
        :param width: The width of the chart.
        :param height: The height of the chart.
        :param chart_actions: 'False' by default. Set it to 'True' to enable chart options to pan and zoom. Scroll mouse button for zoom and drag for pan.
        :param y_axis_title: The title of 'Y' axis.
        :param x_axis_title: The title of 'X' axis.
        :param color: The list of colors to be added to the chart. Make sure that it is a list and is in 'string' datatype. Set it to 'None' to get the default color.
        :param line_width: The width of the line in Line Chart.
        :param print_log: Set it to 'True' to see the process and 'False' to disable the log.
        """
        self.wait = True
        self.location = location
        self.title = title
        self.legend_position = legend_position
        self.width = width
        self.height = height
        self.data = []
        self.chart_actions = chart_actions
        self.data_titles = []
        self.y_axis_title = 'Y'
        self.x_axis_title = 'X'
        self.auto_update = False
        self.update_time = 5000
        self.y_axis_title = y_axis_title
        self.x_axis_title = x_axis_title
        self.color = color
        self.line_width = line_width
        self.print_log = print_log
        self.background_color = background_color

    def add_data(self, data, data_titles):
        """
        Add data to a Line Chart.
        :param data: The 2-d list of the data to be added.
        :param data_titles: The list of titles of the data. Make sure that the length of the titles list is equal to the length of a item in a 2-d list.
        """
        if self.print_log:
            print(f"{self.title}: Creating Chart.....")
        self.data_titles = data_titles
        self.data = data
        file = open(f'{self.location}.html', "w")
        file.write(f"<html>\n<head>\n<title>{self.title}</title>")
        file.write(
            f'\n<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>\n<script type="text/javascript">')
        file.write("\ngoogle.charts.load('current', {'packages':['corechart']});")
        file.write(
            "\ngoogle.charts.setOnLoadCallback(drawChart);\nfunction drawChart() {\nvar data = google.visualization.arrayToDataTable([\n")
        if self.print_log:
            print(f"{self.title}: Adding Data.....")
        file.write(f"{data_titles},\n")
        for i in range(0, len(self.data)):
            file.write(f"{self.data[i]},\n")
        if self.print_log:
            print(f"{self.title}: Data Added!")
        file.write("]);\n")
        file.write("var options = {")
        file.write("title: '" + str(
            self.title) + f"',\ncurveType: 'function',\nlineWidth: {self.line_width},\n")
        if self.color is not None:
            file.write(f"\ncolors: {self.color},")
        file.write("legend: { position: '" + str(self.legend_position) + "'},\n")
        file.write("vAxis: {\ntitle:" + "'" + str(self.y_axis_title) + "'},\n")
        file.write("hAxis: {\ntitle:" + "'" + str(self.x_axis_title) + "'},\n")
        file.write(f"backgroundColor: '{self.background_color}',\n")
        if self.chart_actions:
            file.write("explorer: {}\n")
        file.write("\n};")
        file.write(f"\nvar chart = new google.visualization.LineChart(document.getElementById('line_chart'));\n")
        file.write("chart.draw(data, options);\n}")
        file.write(
            f"</script>\n</head>\n<body>\n<div id = 'line_chart' style = 'width: {self.width}px; height: {self.height}px'></div>\n</body>\n</html>")
        file.close()
        if self.print_log:
            print(f"{self.title}: Chart Created!")

    def enable_auto_update(self, time=5000):
        """
        Function to enable auto update.
        :param time: The time of update(in millisecond)
        """
        if self.print_log:
            print(f"{self.title}: Enabling Auto Update.....")
        self.auto_update = True
        self.update_time = time
        file = open(f'{self.location}.html', "w")
        file.write(f"<html>\n<head>\n<title>{self.title}</title>")
        file.write(
            f'\n<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>\n<script type="text/javascript">')
        file.write("\ngoogle.charts.load('current', {'packages':['corechart']});")
        file.write(
            "\ngoogle.charts.setOnLoadCallback(drawChart);\nfunction drawChart() {\nvar data = google.visualization.arrayToDataTable([\n")
        file.write(f"{self.data_titles},\n")
        for i in range(0, len(self.data)):
            file.write(f"{self.data[i]},\n")
        file.write("]);\n")
        file.write("var options = {")
        file.write("title: '" + str(
            self.title) + f"',\ncurveType: 'function',\nlineWidth: {self.line_width},\n")
        if self.color is not None:
            file.write(f"\ncolors: {self.color},")
        file.write("legend: { position: '" + str(self.legend_position) + "'},\n")
        file.write("vAxis: {\ntitle:" + "'" + str(self.y_axis_title) + "'},\n")
        file.write("hAxis: {\ntitle:" + "'" + str(self.x_axis_title) + "'},\n")
        file.write(f"backgroundColor: '{self.background_color}',\n")
        if self.chart_actions:
            file.write("explorer: {}\n")
        file.write("\n};")
        file.write(f"\nvar chart = new google.visualization.LineChart(document.getElementById('line_chart'));\n")
        file.write("chart.draw(data, options);\n}")
        file.write('function AutoRefresh( t ) {\nsetTimeout("location.reload(true);", t);\n}')
        file.write(
            f"\n</script>\n</head>\n" + '<body onload = "JavaScript:AutoRefresh(' + str(
                time) + ');">' + f"\n<div id = 'line_chart' style = 'width: {self.width}px; height: {self.height}px'></div>\n</body>\n</html>")
        file.close()
        if self.print_log:
            print(f"{self.title}: Auto Update Enabled!")

    def disable_auto_update(self):
        """
        Function to disable the auto update.
        """
        if self.print_log:
            print(f"{self.title}: Disabling Auto Update.....")
        self.auto_update = False
        file = open(f'{self.location}.html', "w")
        file.write(f"<html>\n<head>\n<title>{self.title}</title>")
        file.write(
            f'\n<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>\n<script type="text/javascript">')
        file.write("\ngoogle.charts.load('current', {'packages':['corechart']});")
        file.write(
            "\ngoogle.charts.setOnLoadCallback(drawChart);\nfunction drawChart() {\nvar data = google.visualization.arrayToDataTable([\n")
        file.write(f"{self.data_titles},\n")
        for i in range(0, len(self.data)):
            file.write(f"{self.data[i]},\n")
        file.write("]);\n")
        file.write("var options = {")
        file.write("title: '" + str(
            self.title) + f"',\ncurveType: 'function',\nlineWidth: {self.line_width},\n")
        if self.color is not None:
            file.write(f"\ncolors: {self.color},")
        file.write("legend: { position: '" + str(self.legend_position) + "'},\n")
        file.write("vAxis: {\ntitle:" + "'" + str(self.y_axis_title) + "'},\n")
        file.write("hAxis: {\ntitle:" + "'" + str(self.x_axis_title) + "'},\n")
        file.write(f"backgroundColor: '{self.background_color}',\n")
        if self.chart_actions:
            file.write("explorer: {}\n")
        file.write("\n};")
        file.write(f"\nvar chart = new google.visualization.LineChart(document.getElementById('line_chart'));\n")
        file.write("chart.draw(data, options);\n}")
        file.write(
            f"</script>\n</head>\n<body>\n<div id = 'line_chart' style = 'width: {self.width}px; height: {self.height}px'></div>\n</body>\n</html>")
        file.close()
        if self.print_log:
            print(f"{self.title}: Auto Update Disabled!")

    def update_data(self, data, append=False, wait=True):
        """
        Function to update a data if auto update is enabled.
        :param data: The new data to be added.
        :param append: If 'False' then it it will not append the data to the chart. If 'True' the it will append the data to the chart.
        :param wait: Wait for a given update time if 'True' and disabled when 'False'.
        """
        if self.print_log:
            print(f"{self.title}: Updating Data.....")
        self.wait = wait
        if self.wait:
            time.sleep(self.update_time / 1000)
        self.auto_update = True
        if append:
            self.data += data
        else:
            self.data = data
        file = open(f'{self.location}.html', "w")
        file.write(f"<html>\n<head>\n<title>{self.title}</title>")
        file.write(
            f'\n<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>\n<script type="text/javascript">')
        file.write("\ngoogle.charts.load('current', {'packages':['corechart']});")
        file.write(
            "\ngoogle.charts.setOnLoadCallback(drawChart);\nfunction drawChart() {\nvar data = google.visualization.arrayToDataTable([\n")
        file.write(f"{self.data_titles},\n")
        for i in range(0, len(self.data)):
            file.write(f"{self.data[i]},\n")
        file.write("]);\n")
        file.write("var options = {")
        file.write("title: '" + str(
            self.title) + f"',\ncurveType: 'function',\nlineWidth: {self.line_width},\n")
        if self.color is not None:
            file.write(f"\ncolors: {self.color},")
        file.write("legend: { position: '" + str(self.legend_position) + "'},\n")
        file.write("vAxis: {\ntitle:" + "'" + str(self.y_axis_title) + "'},\n")
        file.write(
            "hAxis: {\ntitle:" + "'" + str(self.x_axis_title) + "'},\n")
        file.write(f"backgroundColor: '{self.background_color}',\n")
        if self.chart_actions:
            file.write("explorer: {}\n")
        file.write("\n};")
        file.write(f"\nvar chart = new google.visualization.LineChart(document.getElementById('line_chart'));\n")
        file.write("chart.draw(data, options);\n}")
        file.write('function AutoRefresh( t ) {\nsetTimeout("location.reload(true);", t);\n}')
        file.write(
            f"\n</script>\n</head>\n" + '<body onload = "JavaScript:AutoRefresh(' + str(
                self.update_time) + ');">' + f"\n<div id = 'line_chart' style = 'width: {self.width}px; height: {self.height}px'></div>\n</body>\n</html>")
        file.close()
        if self.print_log:
            print(f"{self.title}: Data Updated!")

    def open(self):
        """
        Function to automatically open the chart in the browser. If the chart doesn't open then go to the saved location and open it.
        """
        if self.print_log:
            print(f"{self.title}: Opening chart.....")
        os.system(f'start {self.location}.html')
        if self.print_log:
            print(f"{self.title}: Chart Opened!")

    def print_chart_settings(self):
        """
        Function to print the Chart Settings.
        """
        chart_settings = f"Chart '{self.title}' Settings: \n\tChart Name:- {self.title}\n\tChart Type:- Line Chart\n\tChart Location:- {self.location}.html\n\tBackground Color:- {self.background_color}\n\tChart Width:- {self.width}\n\tChart Height:- {self.height}\n\tLegend Position:- {self.legend_position}\n\tChart Actions(pan/zoom):- {self.chart_actions}\n\tX Axis Title:- {self.x_axis_title}\n\tY Axis Title:- {self.y_axis_title}\n\tColor:- {self.color}\n\tLine Width:- {self.line_width}\n\tAuto Update:- {self.auto_update}"
        print(chart_settings)
        if self.auto_update:
            print(f"\tUpdate Time:- {self.update_time} millisecond")
        if self.wait:
            print(f"\tWait for update:- {self.wait}")
        print(f"\tPrint Log:- {self.print_log}")
