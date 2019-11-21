from super_dan_app.dataset import get_data
from super_dan_app.dataset import pre_processing


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
        data_for_training = pre_processing.main()
        assert data_for_training.shape[1] == 7

    def test_target_class_number(self):
        """
        Check for nans or other funky business on the target variable
        """
        data_for_training = pre_processing.main()
        class_numb = data_for_training.Statute_Text.nunique(dropna=False)

        assert class_numb == 2
