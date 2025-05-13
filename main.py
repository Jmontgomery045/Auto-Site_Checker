import multiprocessing
import Tests.login_test as LoginTest
import Tests.deposit_test as DepositTest
import Tests.bet_placement_test as BetPlacementTest
import Tests.in_play_bet_placement_test as InPlayBetPlacementTest
import Tests.games_spin_spribe_test as GamesSpinSpribeTest
import Tests.tote_bet_placement_test as ToteBetPlacementTest
import Tests.horse_racing_bet_placement_test as HorseRacingBetPlacementTest
import Tests.virtuals_bet_placement_test as VirtualsBetPlacementTest
import pprint

# import Tests.register_test as RegisterTest  # Still commented out

def run_login(result_dict):
    test = LoginTest.Test01Login()
    test.setup_method(None)
    result_dict["Login"] = test.test_01Login()
    test.teardown_method(None)

def run_deposit(result_dict):
    test = DepositTest.test_02Deposit()
    test.setup_method(None)
    result_dict["Deposit"] = test.test_02Deposit()
    test.teardown_method(None)

def run_bet_placement(result_dict):
    test = BetPlacementTest.test_03BetPlacement()
    test.setup_method(None)
    result_dict["BetPlacement"] = test.test_03BetPlacement()
    test.teardown_method(None)

def run_inplay_bet_placement(result_dict):
    test = InPlayBetPlacementTest.test_04InPlayBetPlacement()
    test.setup_method(None)
    result_dict["InPlayBetPlacement"] = test.test_04InPlayBetPlacement()
    test.teardown_method(None)

def run_games_spin_spribe(result_dict):
    test = GamesSpinSpribeTest.test_05GamesSpinSpribe()
    test.setup_method(None)
    result_dict["GamesSpin_Spribe"] = test.test_05GamesSpinSpribe()
    test.teardown_method(None)

def run_horse_racing_bet_placement(result_dict):
    test = HorseRacingBetPlacementTest.test_04HorseRacingBetPlacement()
    test.setup_method(None)
    result_dict["HorseRacingBetPlacement"] = test.test_04HorseRacingBetPlacement()
    test.teardown_method(None)

def run_virtuals_bet_placement(result_dict):
    test = VirtualsBetPlacementTest.test_04VirtualsBetPlacement()
    test.setup_method(None)
    result_dict["VirtualsBetPlacement"] = test.test_04VirtualsBetPlacement()
    test.teardown_method(None)

def run_tote_bet_placement(result_dict):
    test = ToteBetPlacementTest.test_04ToteBetPlacement()
    test.setup_method(None)
    result_dict["ToteBetPlacement"] = test.test_04ToteBetPlacement()
    test.teardown_method(None)

def core():
    manager = multiprocessing.Manager()
    result_dict = manager.dict()

    processes = [
        multiprocessing.Process(target=run_login, args=(result_dict,)),
        multiprocessing.Process(target=run_deposit, args=(result_dict,)),
        multiprocessing.Process(target=run_bet_placement, args=(result_dict,)),
        multiprocessing.Process(target=run_inplay_bet_placement, args=(result_dict,)),
        multiprocessing.Process(target=run_games_spin_spribe, args=(result_dict,)),
        multiprocessing.Process(target=run_horse_racing_bet_placement, args=(result_dict,)),
        multiprocessing.Process(target=run_virtuals_bet_placement, args=(result_dict,))

        # Lotto bet
        # Bet History
        # Transaction History

        # multiprocessing.Process(target=run_tote_bet_placement, args=(result_dict,)),
    ]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    result = {k: str(v) for k, v in result_dict.items()}
    
    output = {
        "Login": result["Login"],
        "Deposit": result["Deposit"],
        "BetPlacement": {
            "Sports": result["BetPlacement"],
            "InPlay": result["InPlayBetPlacement"],
            "Games": result["GamesSpin_Spribe"],
            "HorseRacing": result["HorseRacingBetPlacement"],
            "Virtuals": result["VirtualsBetPlacement"]
        }
    }

    pprint.pprint(output)

if __name__ == '__main__':
    multiprocessing.set_start_method('spawn') 
    core()
