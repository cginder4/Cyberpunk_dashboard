from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from time import sleep
from infoFunctions import skyline
from formatFunctions import get_nmap_panel
from formatFunctions import get_sysstats_panel
from formatFunctions import get_weather_panel

console = Console()

layout = Layout()
layout.split_column(
    Layout(name='top', size=8),
    Layout(name='main'),
    Layout(name='footer', size=3)
)

layout['main'].split_row(
    Layout(name='left'),
    Layout(name='center'),
    Layout(name='right')
)

while True:
    layout['top'].update(Panel(skyline, border_style="green"))
    layout['left'].update(get_weather_panel())
    layout['center'].update(get_nmap_panel())
    layout['right'].update(get_sysstats_panel())
    layout['footer'].update(Panel('insert desired quote/text here', border_style="green"))

    console.clear()
    console.print(layout)
    sleep(1800)
