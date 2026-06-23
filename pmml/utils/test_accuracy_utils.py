import pytest

from accuracy_utils import MIN_ACCURACY_SCORE
from accuracy_utils import validate_accuracy_score


def test_validate_accuracy_score_accepts_scores_at_threshold():
    validate_accuracy_score(MIN_ACCURACY_SCORE)


def test_validate_accuracy_score_accepts_scores_above_threshold():
    validate_accuracy_score(0.95)


def test_validate_accuracy_score_rejects_scores_below_threshold():
    with pytest.raises(ValueError, match='below the minimum required score'):
        validate_accuracy_score(0.74)
