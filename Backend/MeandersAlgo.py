import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d as inter
import random

def createPlot(pt):
    """Creates the figure object for the meanders plot

    Args:
        pt (int): number of intersection points

    Returns:
        plot (object): figure object for meanders plot
        firstx (int): x coordinate of first intersection
    """
    plt.close()
    plot = plt.figure(figsize=(8, 8))

    # Creates the intersection points and horizontal line
    pts=[0.05*i + x - 5 for i, x in enumerate(sorted(random.sample(range(10), pt)))]
    firstx=pts[0]
    for x in pts: plt.scatter(x, 0, s=20, c='#FF0000', zorder=3)
    plt.plot((-5, 5), (0, 0), 'gray', zorder=2)
    pts.sort()
    plt.xticks([])
    plt.yticks([])

    # arr is an array from 1 to n where n is the number of points
    arr=list(range(1, pt))
    ord=[0]
    i=0

    # Creates the array ord which is the order of the intersections
    while len(arr) > 0:
      g=arr[int(np.random.rand()*(len(arr)))]
      if np.abs(g - ord[i]) % 2 == 1:
        ord.append(g)
        del arr[arr.index(g)]
        i+=1

    ally=[]
    xnew=[]

    def find_intersection(f1):
      """Find if the curve intersects any of the other curves

      Args:
          f1 (function): interpolation function for each curve

      Returns:
          float: value that indicates if there is an intersection
      """
      x1 = max(min(xnew[i]), min(xnew[i-2*j]))
      x2 = min(max(xnew[i]), max(xnew[i-2*j]))
      if x1 >= x2:
        return None
      elif x1 == min(xnew[i]) and x2 == max(xnew[i]) or x1 == min(xnew[i-2*j]) and x2 == max(xnew[i-2*j]):
        return None
      elif np.isnan(f1((x2-x1)/2 + x1)):
        return None
      else:
        return (x2-x1)/2 + x1, f1((x2-x1)/2 + x1)

    # Creates the interpolation between each point with height depending on distance
    # and calls the function above to check for intersection, if none displays plot
    # otherwise creates a new plot
    for i in range(len(ord)-1):
      if i % 2 == 0: h = -1*np.abs((pts[ord[i+1]]-pts[ord[i]])/2)
      else: h=1*np.abs((pts[ord[i+1]]-pts[ord[i]])/2)
      x = (pts[ord[i]], (pts[ord[i+1]]-pts[ord[i]])/2 + pts[ord[i]], pts[ord[i+1]])
      y = (0, h, 0)
      f2 = inter(x, y, kind = 'quadratic', bounds_error=False)
      ally.append(f2)
      xnew.append(np.linspace(pts[ord[i]], pts[ord[i+1]], 40))
      if (i%2==1 and i>2) or (i%2==0 and i>1):
        for j in range(1, i//2+1):
          intersect = find_intersection(ally[i])
          if intersect is not None and abs(intersect[1]) > 0:
            return createPlot(pt)
      plt.plot(xnew[i], f2(xnew[i]), 'k', zorder=1)

    return plot, firstx