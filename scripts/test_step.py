import allure


class TestSetup:
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step("我是测试步骤")
    def test_01(self):
        allure.attach("我是附件的内容", "我是附件")

    @allure.severity(allure.severity_level.CRITICAL)
    def test_02(self):
        assert False

    @allure.severity(allure.severity_level.NORMAL)
    def test_03(self):
        assert True

    @allure.severity(allure.severity_level.MINOR)
    def test_04(self):
        assert True

    @allure.severity(allure.severity_level.TRIVIAL)
    def test_05(self):
        assert True
