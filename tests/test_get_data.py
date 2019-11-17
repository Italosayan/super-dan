from super_dan_app import get_data


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
