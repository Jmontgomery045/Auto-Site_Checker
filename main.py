import multiprocessing
import Tests.login_test as LoginTest
import Tests.deposit_test as DepositTest
import Tests.bet_placement_test as BetPlacementTest
import Tests.in_play_bet_placement_test as InPlayBetPlacementTest
import Tests.games_spin_spribe_test as GamesSpinSpribeTest
import Tests.tote_bet_placement_test as ToteBetPlacementTest
import Tests.horse_racing_bet_placement_test as HorseRacingBetPlacementTest
import Tests.virtuals_bet_placement_test as VirtualsBetPlacementTest
import Tests.lotto_bet_placement_test as LottoBetPlacementTest
import Tests.bet_history_test as BetHistoryTest
import Tests.transaction_history_test as TransactionHistoryTest
import pprint
import tkinter as tk
import time

# import Tests.register_test as RegisterTest  # Still commented out
    

def run_login(result_dict):
    test = LoginTest.Test01Login()
    start_time = time.time()
    test.setup_method(None)
    result_dict["Login"] = test.test_01Login()
    end_time = time.time()
    elapsed_time = end_time - start_time
    result_dict["Login"] = str(result_dict["Login"]) + f" - {elapsed_time:.2f} seconds"
    print(f"Login test took {elapsed_time:.2f} seconds")
    test.teardown_method(None)

def run_deposit(result_dict):
    test = DepositTest.test_02Deposit()
    start_time = time.time()
    test.setup_method(None)
    result_dict["Deposit"] = test.test_02Deposit()
    end_time = time.time()
    elapsed_time = end_time - start_time
    result_dict["Deposit"] = str(result_dict["Deposit"]) + f" - {elapsed_time:.2f} seconds"
    print(f"Deposit test took {elapsed_time:.2f} seconds")
    test.teardown_method(None)

def run_bet_placement(result_dict):
    test = BetPlacementTest.test_03BetPlacement()
    start_time = time.time()
    test.setup_method(None)
    result_dict["BetPlacement"] = test.test_03BetPlacement()
    end_time = time.time()
    elapsed_time = end_time - start_time
    result_dict["BetPlacement"] = str(result_dict["BetPlacement"]) + f" - {elapsed_time:.2f} seconds"
    print(f"Bet Placement test took {elapsed_time:.2f} seconds")
    test.teardown_method(None)

def run_inplay_bet_placement(result_dict):
    test = InPlayBetPlacementTest.test_04InPlayBetPlacement()
    start_time = time.time()
    test.setup_method(None)
    result_dict["InPlayBetPlacement"] = test.test_04InPlayBetPlacement()
    end_time = time.time()
    elapsed_time = end_time - start_time
    result_dict["InPlayBetPlacement"] = str(result_dict["InPlayBetPlacement"]) + f" - {elapsed_time:.2f} seconds"
    print(f"InPlay Bet Placement test took {elapsed_time:.2f} seconds")
    test.teardown_method(None)

def run_games_spin_spribe(result_dict):
    test = GamesSpinSpribeTest.test_05GamesSpinSpribe()
    start_time = time.time()
    test.setup_method(None)
    result_dict["GamesSpin_Spribe"] = test.test_05GamesSpinSpribe()
    end_time = time.time()
    elapsed_time = end_time - start_time
    result_dict["GamesSpin_Spribe"] = str(result_dict["GamesSpin_Spribe"]) + f" - {elapsed_time:.2f} seconds"
    print(f"Games Spin Spribe test took {elapsed_time:.2f} seconds")
    test.teardown_method(None)

def run_horse_racing_bet_placement(result_dict, showtimevar=False):
    test = HorseRacingBetPlacementTest.test_04HorseRacingBetPlacement()
    start_time = time.time()
    test.setup_method(None)
    result_dict["HorseRacingBetPlacement"] = test.test_04HorseRacingBetPlacement()
    end_time = time.time()
    elapsed_time = end_time - start_time
    result_dict["HorseRacingBetPlacement"] = str(result_dict["HorseRacingBetPlacement"]) + f" - {elapsed_time:.2f} seconds"
    print(f"Horse Racing Bet Placement test took {elapsed_time:.2f} seconds")
    test.teardown_method(None)

def run_virtuals_bet_placement(result_dict):
    test = VirtualsBetPlacementTest.test_04VirtualsBetPlacement()
    start_time = time.time()
    test.setup_method(None)
    result_dict["VirtualsBetPlacement"] = test.test_04VirtualsBetPlacement()
    end_time = time.time()
    elapsed_time = end_time - start_time
    result_dict["VirtualsBetPlacement"] = str(result_dict["VirtualsBetPlacement"]) + f" - {elapsed_time:.2f} seconds"
    print(f"Virtuals Bet Placement test took {elapsed_time:.2f} seconds")
    test.teardown_method(None)

def run_tote_bet_placement(result_dict):
    test = ToteBetPlacementTest.test_04ToteBetPlacement()
    start_time = time.time()
    test.setup_method(None)
    result_dict["ToteBetPlacement"] = test.test_04ToteBetPlacement()
    end_time = time.time()
    elapsed_time = end_time - start_time
    result_dict["ToteBetPlacement"] = str(result_dict["ToteBetPlacement"]) + f" - {elapsed_time:.2f} seconds"
    print(f"Tote Bet Placement test took {elapsed_time:.2f} seconds")
    test.teardown_method(None)

def run_lotto_bet_placement(result_dict):
    test = LottoBetPlacementTest.test_04LottoBetPlacement()
    start_time = time.time()
    test.setup_method(None)
    result_dict["LottoBetPlacement"] = test.test_04LottoBetPlacement()
    end_time = time.time()
    elapsed_time = end_time - start_time
    result_dict["LottoBetPlacement"] = str(result_dict["LottoBetPlacement"]) + f" - {elapsed_time:.2f} seconds"
    print(f"Lotto Bet Placement test took {elapsed_time:.2f} seconds")
    test.teardown_method(None)

def run_bet_history(result_dict):
    test = BetHistoryTest.test_04BetHistory()
    start_time = time.time()
    test.setup_method(None)
    result_dict["BetHistory"] = test.test_04BetHistory()
    end_time = time.time()
    elapsed_time = end_time - start_time
    result_dict["BetHistory"] = str(result_dict["BetHistory"]) + f" - {elapsed_time:.2f} seconds"
    print(f"Bet History test took {elapsed_time:.2f} seconds")
    test.teardown_method(None)

def run_transaction_history(result_dict):
    test = TransactionHistoryTest.test_04TransactionHistory()
    start_time = time.time()
    test.setup_method(None)
    result_dict["TransactionHistory"] = test.test_04TransactionHistory()
    end_time = time.time()
    elapsed_time = end_time - start_time
    result_dict["TransactionHistory"] = str(result_dict["TransactionHistory"]) + f" - {elapsed_time:.2f} seconds"
    print(f"Transaction History test took {elapsed_time:.2f} seconds")
    test.teardown_method(None)

def core():
    test_options = [
        ("Login", run_login),
        ("Deposit", run_deposit),
        ("Bet Placement", run_bet_placement),
        ("InPlay Bet Placement", run_inplay_bet_placement),
        ("Games Spin Spribe", run_games_spin_spribe),
        ("Horse Racing Bet Placement", run_horse_racing_bet_placement),
        ("Virtuals Bet Placement", run_virtuals_bet_placement),
        ("Lotto Bet Placement", run_lotto_bet_placement),
        ("Bet History", run_bet_history),
        ("Transaction History", run_transaction_history),
    ]

    checkbox_vars = []
    def run_tests():
        run_button.config(state=tk.DISABLED)
        window.update()
        try:
            selected_tests = [
                func for var, (label, func) in zip(checkbox_vars, test_options) if var.get()
            ]
            if not selected_tests:
                print("No tests selected.")
                return

            manager = multiprocessing.Manager()
            result_dict = manager.dict()
            processes = [
                multiprocessing.Process(target=func, args=(result_dict,))
                for func in selected_tests
            ]

            batch_size = int(batch_size_entry.get())
            for i in range(0, len(processes), batch_size):
                batch = processes[i:i + batch_size]
                for p in batch:
                    p.start()
                for p in batch:
                    p.join()

            result = {k: str(v) for k, v in result_dict.items()}
            # Only include results for tests that were run
            output = {}
            for key in result:
                if key == "Login":
                    output["Login"] = result["Login"]
                elif key == "Deposit":
                    output["Deposit"] = result["Deposit"]
                elif key == "BetHistory":
                    output["BetHistory"] = result["BetHistory"]
                elif key == "TransactionHistory":
                    output["TransactionHistory"] = result["TransactionHistory"]
                elif key in [
                    "BetPlacement",
                    "InPlayBetPlacement",
                    "GamesSpin_Spribe",
                    "LottoBetPlacement",
                    "HorseRacingBetPlacement",
                    "VirtualsBetPlacement",
                ]:
                    if key == "BetPlacement":
                        output["Sports"] = result[key]
                    elif key == "InPlayBetPlacement":
                        output["InPlay"] = result[key]
                    elif key == "GamesSpin_Spribe":
                        output["Games"] = result[key]
                    elif key == "LottoBetPlacement":
                        output["Lotto"] = result[key]
                    elif key == "HorseRacingBetPlacement":
                        output["HorseRacing"] = result[key]
                    elif key == "VirtualsBetPlacement":
                        output["Virtuals"] = result[key]
            
            pprint.pprint(output)
        finally:
            # Add a message to the output text box
            output_text.config(state=tk.NORMAL)
            output_text.delete(1.0, tk.END)
            output_text.insert(tk.END, "Test Results:\n")
            output_text.insert(tk.END, pprint.pformat(output))
            output_text.config(state=tk.DISABLED)
            # Re-enable the button
            run_button.config(state=tk.NORMAL)

    window = tk.Tk()
    window.title("Auto Site Checker")

    for label, _ in test_options:
        var = tk.BooleanVar(value=True)
        cb = tk.Checkbutton(window, text=label, variable=var)
        cb.pack(anchor="w", padx=20)
        checkbox_vars.append(var)

    # Add an output text box
    output_text = tk.Text(window, height=15, width=50)
    output_text.pack(padx=20, pady=20)
    output_text.insert(tk.END, "Test Results will be displayed here...\n")
    output_text.config(state=tk.DISABLED)

    # Input for batch size
    batch_size_label = tk.Label(window, text="Batch Size:")
    batch_size_label.pack(padx=20, pady=5)
    batch_size_entry = tk.Entry(window)
    batch_size_entry.pack(padx=20, pady=5)
    batch_size_entry.insert(0, "1")  # Default value

    run_button = tk.Button(window, text="Run", command=run_tests, width=20, height=2)
    run_button.pack(padx=20, pady=20)

    window.mainloop()

    

if __name__ == '__main__':
    multiprocessing.set_start_method('spawn') 
    core()
