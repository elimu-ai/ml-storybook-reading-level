MIN_ACCURACY_SCORE = 0.75


def validate_accuracy_score(accuracy_score, min_accuracy_score=MIN_ACCURACY_SCORE):
    if accuracy_score < min_accuracy_score:
        raise ValueError(
            f'Accuracy score {accuracy_score:.4f} is below the minimum required score '
            f'of {min_accuracy_score:.4f}'
        )
