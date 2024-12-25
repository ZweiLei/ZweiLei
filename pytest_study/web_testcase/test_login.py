import time
import pytest

class TestLogin:

    age = 18

    @pytest.mark.smoke
    @pytest.mark.run(order=3)
    def test_01_ein(self):
#        time.sleep(3)
        print('Tester ein')

    @pytest.mark.skip(reason='test skip a case')
    @pytest.mark.run(order=2)
    def test_02_zwei(self):
#        time.sleep(3)
        print("Tester Zwei")
#        assert 1==2

    @pytest.mark.skipif(age >= 18, reason='this is an adult.')
    def test_03_dra(self):
        print("Tester Dra")

    @pytest.mark.usermanage
    @pytest.mark.run(order=1)
    def test_04_four(self):
        print("Tester Four")