"""
A Python module to make Google Charts. This module is made by Siddhesh Chavan! The module's version is 1.0!
This module can create a Line chart, Column Chart, Area Chart, Bar Chart, Pie Chart, Table and multiple charts.
Import Statement:
    import pyhtmlchart

Documentation(Tutorial):
    For documentation go to https://sid72020123.github.io/pyhtmlchart/

History:
    24/05/2021(v0.0.0.1) --> First made the module.
    25/05/2021(v0.0.1) --> Made and updated the 'line_chart' package.
    26/05/2021(v0.1.5) --> Made the auto update structure in 'line_chart' package.
    27/05/2021(v0.2.9) --> Fixed many bugs.
    28/05/2021(v0.5.0) --> Made the 'multiple_charts' package and updated it.
    29/05/2021(v0.6.0) --> Made the 'column_chart' package and updated it.
    30/05/2021(v0.9.0) --> Made the 'area_chart','bar_chart', 'pie_chart' and 'table' packages and updated them.
    31/05/2021(v0.9.8) --> Fixed the color issue and updated all packages.
    01/06/2021(v0.9.8.5) --> Fixed the errors of 'multiple_charts' package.
    02/06/2021(v0.9.7) --> Fixed the errors of 'multiple_charts' package and added 'print_settings()' function.
    05/06/2021(v0.9.8) --> Added 'background_color' property to all the charts.
    06/06/2021(v0.9.9) --> Updated 'multiple_chart' package.
    13/06/2021(v1.0) --> First Release!
Credits:
    All code credits to Siddhesh Chavan
    Special thanks to Google Charts.
Information:
    Module made by:- Siddhesh Chavan
    Age:- 15 (as of 2021)
    Email:- siddheshchavan2020@gmail.com
    YouTube Channel:- Siddhesh Chavan (Link: https://www.youtube.com/channel/UCWcSxfT-SbqAktvGAsrtadQ)
    Scratch Account:- @Sid72020123 (Link: https://scratch.mit.edu/users/Sid72020123/)
    My self-made Website: https://Sid72020123.github.io/
"""
import pyhtmlchart.line_chart
import pyhtmlchart.column_chart
import pyhtmlchart.area_chart
import pyhtmlchart.bar_chart
import pyhtmlchart.pie_chart
import pyhtmlchart.table
import pyhtmlchart.multiple_charts

__name__ = "pyhtmlchart"
__version__ = 1.0
__documentation__ = "https://sid72020123.github.io/pyhtmlchart/"
__developer__ = "Siddhesh Chavan"
print(f"{__name__} v{__version__} - {__documentation__}")
