import math

import pytest

try:
    from utils.accuracy_utils import MIN_ACCURACY_SCORE
    from utils.accuracy_utils import validate_accuracy_score
except ModuleNotFoundError:
    from accuracy_utils import MIN_ACCURACY_SCORE
    from accuracy_utils import validate_accuracy_score


def test_validate_accuracy_score_accepts_scores_at_threshold():
    validate_accuracy_score(MIN_ACCURACY_SCORE)


def test_validate_accuracy_score_accepts_scores_above_threshold():
    validate_accuracy_score(0.95)


def test_validate_accuracy_score_rejects_scores_below_threshold():
    with pytest.raises(ValueError, match='below the minimum required score'):
        validate_accuracy_score(0.74)


def test_validate_accuracy_score_rejects_non_finite_scores():
    for value in (math.nan, math.inf, -math.inf):
        with pytest.raises(ValueError, match='finite number'):
            validate_accuracy_score(value)


def test_validate_accuracy_score_rejects_scores_outside_unit_range():
    for value in (-0.1, 1.1):
        with pytest.raises(ValueError, match='between 0.0000 and 1.0000'):
            validate_accuracy_score(value)
