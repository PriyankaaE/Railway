import math

import numpy as np

from structures.predict import make_prediction


def test_make_prediction(sample_input_data):
    # Given
    # expected_first_prediction_value = 113422
    # expected_no_predictions = 1449

    # When
    result = make_prediction(input_data=sample_input_data)

    # Then
    predictions = list(result.get("predictions"))
    print('****** \n\n\n*******',predictions[0])
    assert isinstance(predictions, list)
    # assert isinstance(predictions[0], np.float32)
    assert result.get("errors") is None
    # assert len(predictions) == expected_no_predictions
    # assert math.isclose(predictions[0], expected_first_prediction_value, abs_tol=100)
