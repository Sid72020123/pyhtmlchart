"""
Package to create Tables from given data. To make a simple table, go to https://sid72020123.github.io/pyhtmlchart/#making-table
"""
import os
import time


class Table:
    def __init__(self, location, title='Table', table_border=5, border_color='Black', cell_padding=3, cell_spacing=0,
                 cell_horizontal_text_align='center', cell_vertical_text_align='middle', column_bg_color='Yellow',
                 data_bg_color='White', column_text_color='Black', data_text_color='Black', print_log=False):
        """
        Class to Create a Table from given data.
        :param location: The location of the table to be stored as a '.html' file.
        :param title: The Title of the Table.
        :param table_border: The Border of the table.
        :param border_color: The Border color of the table.
        :param cell_padding: The cell padding. The space between the cell contents and cell border.
        :param cell_spacing: The cell spacing. The space between the cell and table border.
        :param cell_horizontal_text_align: The horizontal align of the text in the table. The values are: 'left','center','right'.
        :param cell_vertical_text_align: The vertical align of the text in the table. The values are: 'top','bottom','center'.
        :param column_bg_color: The Background color of the column.
        :param data_bg_color: The Background color of the data.
        :param column_text_color: The text color of the column.
        :param data_text_color: The text color of the data.
        :param print_log: Set it to 'True' to see the log of making of the table.
        """
        self.location = location
        self.title = title
        self.data = []
        self.columns = []
        self.table_border = table_border
        self.border_color = border_color
        self.cell_padding = cell_padding
        self.cell_spacing = cell_spacing
        self.cell_horizontal_text_align = cell_horizontal_text_align
        self.cell_vertical_text_align = cell_vertical_text_align
        self.column_bg_color = column_bg_color
        self.data_bg_color = data_bg_color
        self.column_text_color = column_text_color
        self.data_text_color = data_text_color
        self.auto_update = False
        self.update_time = 5000
        self.wait = True
        self.print_log = print_log

    def add_data(self, data, columns):
        """
        Function to add the data to the table.
        :param data: The 2-d list of all data to be added.
        :param columns:  The 2-d list of all column data to be added. Make sure that the length of the data is equal to the length of the column list.
        """
        self.data = data
        self.columns = columns
        if self.print_log:
            print(f"'{self.title}': Creating Table.....")
        file = open(f'{self.location}.html', 'w')
        file.write(f"<html>\n<head>\n<title>\n{self.title}\n</title>\n</head>\n<body>\n<center><h1>{self.title}</h1>\n")
        file.write(
            f"<table border = '{self.table_border}' BorderColor='{self.border_color}' cellpadding='{self.cell_padding}' cellspacing='{self.cell_spacing}'>\n")
        file.write(
            f"<tr Valign='{self.cell_vertical_text_align}' bgcolor='{self.column_bg_color}' style='color: {self.column_text_color};'>\n")
        if self.print_log:
            print(f"'{self.title}': Adding Data.....")
        for i in range(0, len(columns)):
            file.write(
                f"<td align='{self.cell_horizontal_text_align}'>{columns[i]}</td>\n")
        file.write(f"</tr>\n")

        for i in range(0, len(data)):
            file.write(
                f"<tr Valign='{self.cell_vertical_text_align}' bgcolor='{self.data_bg_color}' style='color: {self.data_text_color};'>\n")
            for j in range(0, len(data[i])):
                file.write(
                    f"<td align='{self.cell_horizontal_text_align}'>{data[i][j]}</td>\n")
            file.write(f"</tr>\n")
        file.write(f"</table>\n</center>\n</body>\n</html>")
        file.close()
        if self.print_log:
            print(f"'{self.title}': Created Table!")

    def enable_auto_update(self, time=5000):
        """
        Function to enable auto update for a Table.
        :param time: The time  interval to update the data (in millisecond).
        """
        self.auto_update = True
        self.update_time = time
        if self.print_log:
            print(f"'{self.title}': Enabling Auto Update.....")
        file = open(f'{self.location}.html', 'w')
        file.write(
            f"<html>\n<head>\n<title>\n{self.title}\n</title>\n</head>\n<body onload='AutoRefresh({self.update_time})'>\n<center><h1>{self.title}</h1>\n")
        file.write(
            f"<table border = '{self.table_border}' BorderColor='{self.border_color}' cellpadding='{self.cell_padding}' cellspacing='{self.cell_spacing}'>\n")
        file.write(
            f"<tr Valign='{self.cell_vertical_text_align}' bgcolor='{self.column_bg_color}' style='color: {self.column_text_color};'>\n")
        for i in range(0, len(self.columns)):
            file.write(
                f"<td align='{self.cell_horizontal_text_align}'>{self.columns[i]}</td>\n")
        file.write(f"</tr>\n")

        for i in range(0, len(self.data)):
            file.write(
                f"<tr Valign='{self.cell_vertical_text_align}' bgcolor='{self.data_bg_color}' style='color: {self.data_text_color};'>\n")
            for j in range(0, len(self.data[i])):
                file.write(
                    f"<td align='{self.cell_horizontal_text_align}'>{self.data[i][j]}</td>\n")
            file.write(f"</tr>\n")
        file.write(f"</table>\n</center>\n</body>\n")
        file.write('<script>\nfunction AutoRefresh(t){\nsetInterval("location.reload(true);",' +
                   str(self.update_time) + ')\n}\n</script>')
        file.write("\n</html>")
        file.close()
        if self.print_log:
            print(f"'{self.title}': Auto Update Enabled!")

    def disable_auto_update(self):
        """
        Function to disable auto update to the Table.
        """
        self.auto_update = False
        if self.print_log:
            print(f"'{self.title}': Disabling Auto Update.....")
        file = open(f'{self.location}.html', 'w')
        file.write(f"<html>\n<head>\n<title>\n{self.title}\n</title>\n</head>\n<body>\n<center><h1>{self.title}</h1>\n")
        file.write(
            f"<table border = '{self.table_border}' BorderColor='{self.border_color}' cellpadding='{self.cell_padding}' cellspacing='{self.cell_spacing}'>\n")
        file.write(
            f"<tr Valign='{self.cell_vertical_text_align}' bgcolor='{self.column_bg_color}' style='color: {self.column_text_color};'>\n")
        for i in range(0, len(self.columns)):
            file.write(
                f"<td align='{self.cell_horizontal_text_align}'>{self.columns[i]}</td>\n")
        file.write(f"</tr>\n")

        for i in range(0, len(self.data)):
            file.write(
                f"<tr Valign='{self.cell_vertical_text_align}' bgcolor='{self.data_bg_color}' style='color: {self.data_text_color};'>\n")
            for j in range(0, len(self.data[i])):
                file.write(
                    f"<td align='{self.cell_horizontal_text_align}'>{self.data[i][j]}</td>\n")
            file.write(f"</tr>\n")
        file.write(f"</table>\n</center>\n</body>\n</html>")
        file.close()
        if self.print_log:
            print(f"'{self.title}': Auto Update Disabled!")

    def update_data(self, data, append=False, wait=True):
        """
        Function to update the data of a Table.
        :param data: The list of data to be updated.
        :param append:  If 'True' then it appends the new data with the previous data and shows the Table.
        :param wait: Wait for the data to update. Set it to 'True' to wait for the given time and then update the data or else set it to 'False' to update the data continuously.
        """
        self.wait = wait
        self.auto_update = True
        if self.print_log:
            print(f"'{self.title}': Updating Data.....")
        if append:
            self.data += data
        else:
            self.data = data
        if self.wait:
            time.sleep(self.update_time / 1000)
        file = open(f'{self.location}.html', 'w')
        file.write(
            f"<html>\n<head>\n<title>\n{self.title}\n</title>\n</head>\n<body onload='AutoRefresh({self.update_time})'>\n<center><h1>{self.title}</h1>\n")
        file.write(
            f"<table border = '{self.table_border}' BorderColor='{self.border_color}' cellpadding='{self.cell_padding}' cellspacing='{self.cell_spacing}'>\n")
        file.write(
            f"<tr Valign='{self.cell_vertical_text_align}' bgcolor='{self.column_bg_color}' style='color: {self.column_text_color};'>\n")
        for i in range(0, len(self.columns)):
            file.write(
                f"<td align='{self.cell_horizontal_text_align}'>{self.columns[i]}</td>\n")
        file.write(f"</tr>\n")

        for i in range(0, len(self.data)):
            file.write(
                f"<tr Valign='{self.cell_vertical_text_align}' bgcolor='{self.data_bg_color}' style='color: {self.data_text_color};'>\n")
            for j in range(0, len(self.data[i])):
                file.write(
                    f"<td align='{self.cell_horizontal_text_align}'>{self.data[i][j]}</td>\n")
            file.write(f"</tr>\n")
        file.write(f"</table>\n</center>\n</body>\n")
        file.write('<script>\nfunction AutoRefresh(t){\nsetInterval("location.reload(true);",' +
                   str(self.update_time) + ')\n}\n</script>')
        file.write("\n</html>")
        file.close()
        if self.print_log:
            print(f"'{self.title}': Data Updated!")

    def open(self):
        """
        Function to open the table automatically.
        """
        if self.print_log:
            print(f"'{self.title}': Opening Table.....")
        os.system(f'start {self.location}.html')
        if self.print_log:
            print(f"'{self.title}': Table Opened!")

    def print_settings(self):
        print(f"Table '{self.title}' settings:-")
        print(
            f"\tTable Name:- {self.title}\n\tTable Location:- {self.location}.html\n\tTable Border:- {self.table_border}\n\tBorder Color:- {self.border_color}\n\tCell padding:- {self.cell_padding}\n\tCell Spacing:- {self.cell_spacing}\n\tHorizontal Text Align:- {self.cell_horizontal_text_align}\n\tVertical Text Align:- {self.cell_vertical_text_align}\n\tColumn Background Color:- {self.column_bg_color}\n\tData Background Color:- {self.data_bg_color}\n\tColumn Font Color:- {self.column_text_color}\n\tData Font Color:- {self.data_text_color}\n\tPrint Log:- {self.print_log}")
