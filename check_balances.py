from bitcoinlib.services.services import Service
from tqdm import tqdm

def check_bitcoin_balance(address):
    service = Service()
    address_info = service.getbalance(address)
    return address_info

def format_satoshis(satoshis):
    return f"{satoshis:,}"

def process_addresses(input_file, output_file):
    with open(input_file, 'r') as infile:
        total_addresses = sum(1 for line in infile)

    max_address_length = 0
    with open(input_file, 'r') as infile:
        for line in infile:
            address = line.strip()
            max_address_length = max(max_address_length, len(address))

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        pbar = tqdm(total=total_addresses, unit="address")

        for line in infile:
            address = line.strip()
            try:
                balance = check_bitcoin_balance(address)
                formatted_balance = format_satoshis(balance)
                outfile.write(f"{address:<{max_address_length}}  {formatted_balance:>15} satoshis\n")
            except Exception as e:
                outfile.write(f"{address:<{max_address_length}}  {'Error:':<15} {str(e)}\n")
            
            pbar.update(1)

        pbar.close()

input_file = "addresses.txt"            # contain file you desire to check
output_file = "bitcoin_balances.txt"    # result of checking file
process_addresses(input_file, output_file)
print(f"Processing complete. Results written to {output_file}")
