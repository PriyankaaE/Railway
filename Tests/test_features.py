from structures.config.core import config
from structures.data_processing.train_pipeline import ExtractLetterTransformer


def test_ExtractLetterTransformer(sample_input_data):
    # Given
    transformer = ExtractLetterTransformer(
        variable=config.model_param_config.cabin_vars,  # YearRemodAdd
        # reference_variable=config.model_config.ref_var,
    )
    assert sample_input_data["cabin"].iat[0] == 'B5'

    # When
    subject = transformer.fit_transform(sample_input_data)

    # Then
    assert subject["cabin"].iat[0] == 'B'
