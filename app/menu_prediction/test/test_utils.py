from app.menu_prediction.utils import average_prediction

class Test_average_prediction:
    def test_majority(self):
        prediction = average_prediction(['cat', 'cat', 'cat', 'dog'])

        assert prediction == 'cat'

    def test_equal(self):
        prediction = average_prediction(['cat', 'cat', 'dog', 'dog'])

        assert prediction == 'dog'