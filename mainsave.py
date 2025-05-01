import os
from multiprocessing import Process
import Tests.login_test as LoginTest
import Tests.deposit_test as DepositTest
import Tests.bet_placement_test as BetPlacementTest
import Tests.register_test as RegisterTest


def core():

    loginresult = 'Not Checked'
    depositresult = 'Not Checked'
    betplaceresult = 'Not Checked'
    registerResult = 'Not Checked'


    test = LoginTest.Test01Login()
    test.setup_method(None)
    loginresult = test.test_01Login()
    test.teardown_method(None)

    test = DepositTest.test_02Deposit()
    test.setup_method(None)
    depositresult = test.test_02Deposit()
    test.teardown_method(None)

    test = BetPlacementTest.test_03BetPlacement()
    test.setup_method(None)
    betplaceresult = test.test_03BetPlacement()
    test.teardown_method(None)

    # test = RegisterTest.test_04Register()
    # test.setup_method(None)
    # registerResult = test.test_04Register()
    # test.teardown_method(None)

    result = {
    "Login": str(loginresult),
    "Deposit": str(depositresult),
    "BetPlacement": str(betplaceresult)
    }
    print(result)

if __name__ == '__main__':
    core()