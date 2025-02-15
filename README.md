# Internet Speed Chart

## Overview
This project visualizes internet speed test data using Bokeh. It reads data from a text file (`soal_chart_bokeh.txt`), extracts timestamps and speed values, and generates a line chart displaying internet speed over time.

## Features
- Reads data from a text file.
- Extracts timestamps and speed values.
- Generates an interactive line chart using Bokeh.
- Formats the x-axis as a datetime scale.
- Automatically adjusts the chart width.

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- Bokeh

To install Bokeh, run:
```sh
pip install bokeh
```

## Usage
1. Place your data file (`soal_chart_bokeh.txt`) in the same directory as `internet-chart.py`.
2. Run the script:
```sh
python internet-chart.py
```
3. The script will generate an interactive Bokeh chart displaying internet speed over time.

## Data File Format
The script expects `soal_chart_bokeh.txt` to follow a specific format where:
- Date and time are on every 22nd line (starting from index 0).
- Speed values are on every 22nd line (starting from index 16).

Example structure:
```
... (other data)
2025-02-15 10:30:00 ...
... (other data)
Speed: 20.5 Mbps
... (other data)
```

## How It Works
1. The script reads the file content.
2. Extracts datetime values at intervals of 22 lines.
3. Extracts speed values at different intervals of 22 lines.
4. Uses Bokeh to plot a line chart.
5. Displays the interactive chart in a browser.
