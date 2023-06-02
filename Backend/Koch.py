import numpy as np

def koch_snowflake(order, scale=10):
    """Return two lists x, y of point coordinates of the Koch snowflake

    Args:
        order (int): the recursion depth.
        scale (int, optional): the extent of the snowflake. Defaults to 10.
    """
    def _koch_snowflake_complex(order):
        """Returns list of coordinates corresponding to the Koch snowflake

        Args:
            order (int): the recursion depth

        Returns:
            np.array: An array of complex numbers representing the coordinates of the Koch snowflake.
        """
        if order == 0:
            # initial triangle
            angles = np.array([0, 120, 240]) + 90
            return scale / np.sqrt(3) * np.exp(np.deg2rad(angles) * 1j)
        else:
            ZR = 0.5 - 0.5j * np.sqrt(3) / 3

            p1 = _koch_snowflake_complex(order - 1)  # start points
            p2 = np.roll(p1, shift=-1)  # end points
            dp = p2 - p1  # connection vectors

            new_points = np.empty(len(p1) * 4, dtype=np.complex128)
            new_points[::4] = p1
            new_points[1::4] = p1 + dp / 3
            new_points[2::4] = p1 + dp * ZR
            new_points[3::4] = p1 + dp / 3 * 2
            return new_points

    points = _koch_snowflake_complex(order)
    x, y = points.real, points.imag
    return x, y

