import svgpathtools

def svg_to_points(svg_file, n_points=2):
    paths, attributes = svgpathtools.svg2paths(svg_file)
    point_arrays = []
    for path in paths:
        points = []
        for segment in path:
            if isinstance(segment, svgpathtools.path.Line):
                points.append((segment.start.real, -1*segment.start.imag))
                points.append((segment.end.real, -1*segment.end.imag))
            elif isinstance(segment, svgpathtools.path.CubicBezier):
                for i in range(n_points):
                    t = i / (n_points - 1)
                    point = segment.point(t)
                    points.append((point.real, -1*point.imag))
        point_arrays.append(points)
    return point_arrays