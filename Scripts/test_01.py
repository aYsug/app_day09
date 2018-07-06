import allure
class Test_01:
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="测试步骤001")
    def test_01(self):
        allure.attach('描述', '我是测试步骤001的描述～～～')
        assert 0