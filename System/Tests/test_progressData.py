from unittest import TestCase

from System.ProgressData import ProgressData


class TestProgressData(TestCase):
    def setUp(self):
        self.progress_data = ProgressData()

    def test_save_data_array(self):
        self.progress_data.save_data_array("scenes")
        assert len(self.progress_data.get_data_array("scenes")) == 0
        self.progress_data.save_data_array("scenes", "event_name")
        assert "event_name" in self.progress_data.get_data_array("scenes")
        self.progress_data.save_data_array("scenes", "event_name")
        assert len(self.progress_data.get_data_array("scenes")) == 1


def main():
    test = TestProgressData()
    test.test_save_data_array()


if __name__ == '__main__':
    main()
