import pytest
from examples.teaching_ratio import ratio


def test_ratio_uses_both_inputs():
    assert ratio(3, 4) == pytest.approx(0.75)
    assert ratio(1, 2) == pytest.approx(0.5)


def test_undefined_denominator_is_not_zero_performance():
    assert ratio(0, 0) is None
    assert ratio(1, 0) is None
