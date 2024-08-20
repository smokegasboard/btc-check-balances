# btc-check-balances
python script to check bitcoin balances


## Bitcoin Balance Checker

This Python script efficiently checks Bitcoin balances for a list of addresses provided in a text file. 
It leverages `tqdm` to display a progress bar during processing and formats the output for better readability.

**Key Features:**

- **Efficient:** Uses `tqdm` for progress visualization.
- **Informative:** Formats satoshi balances and handles errors with informative messages.

**Usage:**

1. **Prerequisites:**
    - Python 3.x (see badge above)
    - `bitcoinlib` library (`pip install bitcoinlib`)
    - `tqdm` library (`pip install tqdm`)
2. **Prepare your addresses:**
    - Create a text file named `addresses.txt` containing each Bitcoin address on a separate line.
3. **Run the script:**
    ```bash
    python check_balance.py
    ```

**Output:**

The script will generate a file named `bitcoin_balances.txt` containing the processed addresses and their corresponding balances (in satoshis) or error messages if an issue occurs.

**Example Output (bitcoin_balances.txt):**
