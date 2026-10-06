# Normalization Experiment

## Background

The current model uses a `DecisionTreeRegressor` with three features:

* `chapter_count`
* `paragraph_count`
* `word_count`

The baseline model was evaluated without any feature normalization.

## Experiments

I tested three commonly used normalization methods while keeping the model, training data, features, and evaluation process unchanged:

* StandardScaler
* MinMaxScaler
* RobustScaler

The normalization step was added before the existing `DecisionTreeRegressor` in the PMML pipeline.

## Results

| Method         |  Accuracy | Mean Absolute Error |
| -------------- | --------: | ------------------: |
| Baseline       | 0.7916667 |           0.2083333 |
| StandardScaler | 0.7916667 |           0.2083333 |
| MinMaxScaler   | 0.7916667 |           0.2083333 |
| RobustScaler   | 0.7916667 |           0.2083333 |

## Conclusion

None of the tested normalization methods changed the validation results.

Since normalization did not improve either accuracy or mean absolute error, I did not keep the normalization step in the final model.

This result is also consistent with the behavior of decision trees, which generally do not depend on the scale of the input features when selecting split points.
