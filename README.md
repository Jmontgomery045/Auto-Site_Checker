# Usage Instructions:

To install this software, we first need to open a command window and navigate to the main DS_Automation_Suite directory.

Create a Virtual Environment:<br>
<code>python -m venv venv</code><br>
<code>source venv/bin/activate</code>   # On macOS/Linux<br>
<code>venv\Scripts\activate</code>      # On Windows<br>

Install the requirements:<br>
<code>pip install -r requirements.txt</code>

Finally edit the `.env` file to include your Test Users login and password.

To run the application once installed:<br>
Run the application called 'Start-Auto-Site-Checker' via double click.
or: <code>python main.py</code>

----

# Functionality:

Currently the Auto-Site-Checker runs 3 tests.

1. Login - This check is simple. the system logs into the website using the information given in the env file, and confirms that it is logged in.
2. Deposit - In this check, the system logs into the website. before following the process to make a deposit. Although it cannot actually make a deposit, the system will confirm that the iFrame opens correctly.
3. Bet Placement - In this check, the system logs into the website, before placing a £1 bet on the first available option in 'Sports'.
4. Inplay Bet Placement - This check places a bet onto the first available market in 'In Play'
5. Games Spin Spribe - This check plaes a spin on a spribe game.
6. Horse Racing Bet Placement - This check places a bet on the first horse available.
7. Virtuals bet placement - This check places a bet on the first virtual horse available.
8. Lotto bet placement - This check places a simple lotto bet.
9. Bet History - This check accesses our bet history.
10. Transaction History - This check accesses our transaction history.
