"""A basic mathematical teaching utility, not a project audit implementation."""


def ratio(numerator: float, denominator: float) -> float | None:
    """Return a ratio, or None when the denominator is zero.

    This deliberately tiny example doesn't validate data types, units,
    population membership, or real source quality. Henry defines those rules
    and their tests for his own analytical work.
    """
    if denominator == 0:
        return None
    return numerator / denominator
