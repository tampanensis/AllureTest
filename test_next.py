import allure


class TestNext:
    @allure.title('Test third')
    def test_next(self):
        assert 2 > 3
