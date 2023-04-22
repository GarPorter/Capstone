import numpy as np
import streamlit as st

def boundPoints(lines):
  points=[]
  xmin = min(st.session_state.pointsArr[:, 0])*0.8
  ymin = min(st.session_state.pointsArr[:, 1])*0.8
  xmax = max(st.session_state.pointsArr[:, 0])*1.2
  ymax = max(st.session_state.pointsArr[:, 1])*1.2

  lines=np.array(lines)

  # Plot the Voronoi lines and seed points
  for i, line in enumerate(lines):
      x, y = zip(*line)
      x1=x[0]
      x2=x[1]
      y1=y[0]
      y2=y[1]
      slope = (y2-y1)/(x2-x1)
      intercept=y1-slope*x1

      # Clip the line to the boundary of the area
      if x1 < xmin:
          y1 = slope * xmin + intercept
          x1 = xmin
      elif x1 > xmax:
          y1 = slope * xmax + intercept
          x1 = xmax

      if x2 < xmin:
          y2 = slope * xmin + intercept
          x2 = xmin
      elif x2 > xmax:
          y2 = slope * xmax + intercept
          x2 = xmax

      if y1 < ymin:
          x1 = (ymin - intercept) / slope
          y1 = ymin
      elif y1 > ymax:
          x1 = (ymax - intercept) / slope
          y1 = ymax

      if y2 < ymin:
          x2 = (ymin - intercept) / slope
          y2 = ymin
      elif y2 > ymax:
          x2 = (ymax - intercept) / slope
          y2 = ymax
      points.append([(x1, y1), (x2, y2)])
  return points