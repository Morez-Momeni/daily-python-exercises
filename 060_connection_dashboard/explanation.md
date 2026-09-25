# Problem 60: Connection Duration Dashboard

## Problem
Read a JSON log file that contains a list of connection sessions (each with an `id` and a `duration`), extract the relevant fields, and visualize the durations as a bar chart using Matplotlib.

## My Solution

I split the task into two functions:
- `extrect_data()` – reads the JSON log and returns a list of `(id, duration)` tuples.
- `plot()` – uses Matplotlib to draw a bar chart of connection durations.