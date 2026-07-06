import math

# MIN_ACCURACY_SCORE = 0.75
MIN_ACCURACY_SCORE = 0.80

def validate_accuracy_score(accuracy_score, min_accuracy_score=MIN_ACCURACY_SCORE):
    if isinstance(accuracy_score, bool) or not isinstance(accuracy_score, (int, float)) or not math.isfinite(accuracy_score):
        raise ValueError('Accuracy score must be a finite number')
    if not 0.0 <= accuracy_score <= 1.0:
        raise ValueError(f'Accuracy score {accuracy_score:.4f} must be between 0.0000 and 1.0000')
    if accuracy_score < min_accuracy_score:
        raise ValueError(
            f'Accuracy score {accuracy_score:.4f} is below the minimum required score '
            f'of {min_accuracy_score:.4f}'
        )
