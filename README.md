# Environment File

A .env file should be created in the main `Auto-Site-Checker` directory. include the below lines.

USER=[Username here]<br>
PASS=[Password Here]

----
# Usage Instructions:

To use this software, simply ensure the .env file is present and filled in, then navigate into the main directory and run the below command.

`python main.py`

----

# Functionality:

Currently the Auto-Site-Checker runs 3 tests.

1. Login - This check is simple. the system logs into the website using the information given in the env file, and confirms that it is logged in.
2. Deposit - In this check, the system logs into the website. before following the process to make a deposit. Although it cannot actually make a deposit, the system will confirm that the iFrame opens correctly.
3. Bet Placement - In this check, the system logs into the website, before placing a £1 bet on the first available option in 'Sports'.
