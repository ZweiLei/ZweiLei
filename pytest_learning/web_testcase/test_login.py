import time
import pytest

class TestLogin:

    age = 18

    @pytest.mark.smoke # mark this case as a 'smoke' test.
    @pytest.mark.run(order=3)
    def test_01_ein(self):
#        time.sleep(3)
        print('Tester ein')

    @pytest.mark.skip(reason='test skip a case')  #skip this case directly.
    @pytest.mark.run(order=2)
    def test_02_zwei(self):
#        time.sleep(3)
        print("Tester Zwei")
#        assert 1==2

    @pytest.mark.skipif(age >= 18, reason='this is an adult.') #skip this case conditionally.
    def test_03_dra(self):
        print("Tester Dra")

    @pytest.mark.usermanage # mark this case as a 'usermanage' test.
    @pytest.mark.run(order=1) #Execute this case in 1st order.
    def test_04_four(self):
        print("Tester Four")