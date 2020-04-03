from super_dan_app.dataset import get_data
from super_dan_app.dataset import pre_processing as pp


class TestGetData:

    def test_crime_data_request_status(self):
        """
        Check that response returns 200 status
        """
        test_request = get_data.crime_data_request(get_data.REQUEST_URL)

        assert test_request.status_code == 200

    def test_crime_data_request_elapsed_time(self):
        """
        Check that elapsed time is less than 10,000
        """
        test_request = get_data.crime_data_request(get_data.REQUEST_URL)

        assert test_request.elapsed.total_seconds() < 10000


class TestPreProcessData:

    def test_column_count(self):
        """
        Check number of features
        """
        get_data.main()
        data_for_training = pp.main()
        assert data_for_training.shape[1] == 12

    def test_target_class_number(self):
        """
        Check for nans or other funky business on the target variable
        """
        data_for_training = pp.main()
        class_numb = data_for_training.Statute_Text.nunique(dropna=False)

        assert class_numb == 2

    def test_drop_na(self):
        """
        Check the number of NA rows
        """
        data_frame_roc_crimes = pp.read_data()
        features_target = pp.setting_features_and_target(data_frame_roc_crimes)
        features_target = pp.dummy_location_type_variable(features_target)

        row_count_before_na = features_target.shape[0]
        features_target = pp.na_values(features_target)
        row_count_after_na = features_target.shape[0]

        assert row_count_before_na - row_count_after_na < 100
