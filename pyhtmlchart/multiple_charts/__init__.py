"""
Package to display multiple charts on one '.html' page. To make a simple multiple chart, go to https://sid72020123.github.io/pyhtmlchart/multiple_charts.html
"""
import os


class MultipleCharts:
    def __init__(self, location, title="Multiple Chart", height=600, width=1000, frame_border=0, border=0,
                 border_color='Black'):
        """
        Class to create multiple charts on one page.
        :param location: The location of the '.html' page to be saved.
        :param title: The title of group of charts.
        :param height: The height of all frames.
        :param width: The width of all frames.
        :param frame_border: The frame border of all frames.
        :param border: The border width of all frames.
        :param border_color: The border color of all frames.
        """
        self.location = location
        self.title = title
        self.height = height
        self.width = width
        self.frame_border = frame_border
        self.border = border
        self.border_color = border_color
        self.frame_value = []
        self.frame_size = []
        self.chart_locations = ''

    def add_chart(self, chart_locations, frame_value=[], frame_size=[]):
        """
        Function to add the saved charts on one page.
        :param chart_locations: The list of all the chart's saved locations to be added on one page. The elements should be separated by commas and should be in 'string' format. Please give the correct location along with the extension. The order of charts in the page is same as the order of files given in the list. You can change the values in the list to add the charts accordingly.
        :param frame_value: If you want to change the size of one chart in a page then give the chart's list index according to the 'chart_locations' list and use the frame_size parameter to set a different size for that specified chart.
        :param frame_size: If you pass the 'frame_size' parameter, then give the size of that chart in a 2-d list. First is height and then width.
        """
        self.chart_locations = chart_locations
        self.frame_value = frame_value
        self.frame_size = frame_size
        frame_height = []
        frame_width = []
        for i in range(0, len(chart_locations)):
            frame_height.append(self.height)
            frame_width.append(self.width)

        for i in range(0, len(chart_locations)):
            for j in range(0, len(self.frame_value)):
                if i == self.frame_value[j]:
                    frame_height[i] = self.frame_size[j][0]
                    frame_width[i] = self.frame_size[j][1]

        file = open(f"{self.location}.html", "w")
        file.write(
            f"<html>\n<head>\n<title>\n{self.title}\n</title>\n</head>\n<body>\n<center>\n<h1>\n{self.title}\n</h1>\n</center>\n")
        for i in range(0, len(chart_locations)):
            file.write(
                f"<iframe src = '{chart_locations[i]}', width='{frame_width[i]}px', height = '{frame_height[i]}px', frameBorder='{self.frame_border}', style = 'border: {self.border}px solid {self.border_color}'>\n</iframe>\n")
        file.write("</body>\n</html>")
        file.close()

    def open(self):
        """
        Function to open the saved multiple charts.
        """
        os.system(f'start {self.location}.html')

    def print_settings(self):
        """
        Function to print the chart settings.
        """
        print(
            f"Multiple Chart - '{self.title}' settings:-\n\tChart Name:- {self.title}\n\tChart Type:- Multiple Chart\n\tChart Location:- {self.location}.html\n\tChart Height:- {self.height}\n\tChart Width:- {self.width}\n\tChart Border:- {self.border}\n\tFrame Border:- {self.frame_border}\n\tBorder Color:- {self.border_color}")
        print(f"\tSub charts:-")
        for i in range(0, len(self.chart_locations)):
            print(f"\t\t{i} -> {self.chart_locations[i]}")
        print(f"\tDifferent Size:- ")
        if len(self.frame_value) == 0:
            print('\t\tNone')
        else:
            for i in range(0, len(self.frame_value)):
                print(f"\t\t{self.frame_value[i]} -> {self.frame_size[i]}")
