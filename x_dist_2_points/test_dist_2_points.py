# from x_dist_2_points.x_dist_2_points import dist, dist_points
import x_dist_2_points
from x_dist_2_points.x_dist_2_points import dist, dist_points

def test_dist():
    p1 = (0,0)
    p2 = (3,4)
    expected = 5

    result = dist(p1,p2)
    assert expected == result

def test_dist_points():
    _points = [(0,0),(1,1), (2,2), (3,3), (4,4), (5,5)]
    _min_expected =  1.4142

    result, _dist_points = dist_points(_points)
    assert _min_expected == round(result,4)
