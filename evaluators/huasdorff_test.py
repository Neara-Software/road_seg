import pytest
from evaluators.hausdorff import HausdorffLineSegmentEvaluator
from model.point import Point


@pytest.fixture
def hausdorff():
    return HausdorffLineSegmentEvaluator()


def test_distance_between_two_points(hausdorff):
    p1 = Point(1, 2, 3)
    p2 = Point(4, 6, 8)
    actual_output = hausdorff._point_distance(p1, p2)
    assert actual_output == pytest.approx(7.071067811864, rel=1e-12)
