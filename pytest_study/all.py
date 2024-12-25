import pytest

if __name__ == "__main__":
#    pytest.main(['-vs'])
#    pytest.main(['-vs', 'test_login.py', 'test_product.py'])
#   pytest.main(['-vs', './web_testcase', '-n=2']) 
   pytest.main(['-vs', './web_testcase/test_login.py', '--reruns=2'])
#    pytest.main(['-vs', './interface_testcase/test_interface.py::test_04_func'])
#    pytest.main(['-vs', './interface_testcase/test_interface.py::TestInterface::test_03_dra'])
### pytest -vs ./web_test/test_login.py -n 2 --reruns 2 -x
### pytest -vs ./web_test/test_login.py --maxfail 2
### pytest -vs ./web_test/test_login.py -k "execute cases which have some chars"