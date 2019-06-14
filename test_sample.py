import allure


class TestAllure:

    @allure.title('Test first')
    def test_first(self):
        assert 1 == 2

    @allure.title('Test second')
    def test_second(self):
        assert True
