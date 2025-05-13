import random  # For generating random numbers, used for the sleep duration.
import time  # For time-related functions, specifically to pause the script.
import requests  # For making HTTP requests to fetch data from the Coinbase API.

# --- Constants and Parameters ---
INITIAL_INVESTMENT = 1000000  # The initial amount of British Pounds (GBP) for the trading portfolio.
PERCENTAGE_OF_FUNDS = 0.1  # The percentage (10%) of the available GBP balance to use for each buy or sell order.
API_URL_BUY = 'https://api.coinbase.com/v2/prices/BTC-GBP/buy'  # The API endpoint to get the current buying price of Bitcoin (BTC) in GBP from Coinbase.
API_URL_SELL = 'https://api.coinbase.com/v2/prices/BTC-GBP/sell'  # The API endpoint to get the current selling price of Bitcoin (BTC) in GBP from Coinbase.
SLEEP_MIN = 10  # The minimum number of seconds the script will sleep between each trading cycle.
SLEEP_MAX = 20  # The maximum number of seconds the script will sleep between each trading cycle.

class CryptoPortfolio:
    """
    A class to represent and manage a cryptocurrency trading portfolio, specifically for GBP and Bitcoin (BTC).

    Attributes:
    - gbp_balance (float): The current balance of British Pounds in the portfolio.
    - btc_balance (float): The current balance of Bitcoin in the portfolio.
    - btc_purchase_price (float): The most recently fetched purchase price of Bitcoin.
    - btc_sale_price (float): The most recently fetched sale price of Bitcoin.
    - purchase_threshold (float): The price below which the bot will consider buying Bitcoin.
    - sale_threshold (float): The price above which the bot will consider selling Bitcoin.
    - transaction_history (list): A list to keep track of all buy and sell transactions.
    """
    
    def __init__(self, initial_investment):
        """
        Initializes the CryptoPortfolio with a starting GBP balance and sets initial values for other attributes.

        Parameters:
        - initial_investment (float): The initial amount of GBP to start with.
        """
        self.gbp_balance = initial_investment
        self.btc_balance = 0.0
        self.btc_purchase_price = 0.0
        self.btc_sale_price = 0.0
        self.purchase_threshold = 0.0
        self.sale_threshold = 0.0
        self.transaction_history = []

    def fetch_btc_values(self):
        """
        Fetches the current Bitcoin buying and selling prices from the Coinbase API.
        It also calculates and updates the purchase and sale thresholds based on these prices.
        """
        try:
            # Make HTTP GET requests to the Coinbase API to get buying and selling prices.
            buying_response = requests.get(API_URL_BUY)
            selling_response = requests.get(API_URL_SELL)

            # Raise an exception for bad status codes (e.g., 404, 500) if the API request fails.
            buying_response.raise_for_status()
            selling_response.raise_for_status()

            # Parse the JSON response from the API to extract the price data.
            buying_data = buying_response.json()
            selling_data = selling_response.json()

            # Extract the Bitcoin purchase price in GBP.
            self.btc_purchase_price = float(buying_data['data']['amount'])
            # Extract the Bitcoin sale price in GBP.
            self.btc_sale_price = float(selling_data['data']['amount'])

            # Set the purchase threshold to 1% below the current purchase price.
            self.purchase_threshold = self.btc_purchase_price * 0.99
            # Set the sale threshold to 1% above the current sale price.
            self.sale_threshold = self.btc_sale_price * 1.01

            # Print the fetched Bitcoin prices and the calculated thresholds for monitoring.
            print(f'🔄 BTC purchase price: £{self.btc_purchase_price:.2f}, Sale price: £{self.btc_sale_price:.2f}')
            print(f'📉 Purchase threshold: £{self.purchase_threshold:.2f}, 📈 Sale threshold: £{self.sale_threshold:.2f}\n')

        except requests.exceptions.RequestException as e:
            print(f'❌ Error: Could not fetch BTC values - {e}')
        except (KeyError, ValueError, TypeError) as e:
            print(f'❌ Error: Invalid API response - {e}')

    def buy_bitcoin(self, percentage_of_funds):
        """
        Buys Bitcoin if the current purchase price is at or below the purchase threshold,
        using a specified percentage of the available GBP balance.

        Parameters:
        - percentage_of_funds (float): The percentage of the GBP balance to use for buying.
        """
        # Check if the current Bitcoin purchase price is at or below the set purchase threshold.
        if self.btc_purchase_price <= self.purchase_threshold:
            # Calculate the amount of GBP to invest based on the specified percentage.
            gbp_to_invest = self.gbp_balance * percentage_of_funds
            # Calculate the amount of Bitcoin that can be bought with the GBP to invest.
            btc_to_buy = gbp_to_invest / self.btc_purchase_price

            # Check if there is enough GBP balance to make the purchase.
            if gbp_to_invest <= self.gbp_balance:
                # Update the Bitcoin and GBP balances after the purchase.
                self.btc_balance += btc_to_buy
                self.gbp_balance -= gbp_to_invest

                # Record the buy transaction details in the transaction history.
                self.transaction_history.append({
                    'type': 'buy',
                    'btc_amount': btc_to_buy,
                    'gbp_amount': gbp_to_invest,
                    'btc_price': self.btc_purchase_price
                })

                # Print a confirmation message for the buy transaction.
                print(f'🚀 Bought {btc_to_buy:.8f} BTC for £{gbp_to_invest:.2f}')
                print(f'💼 BTC portfolio: {self.btc_balance:.8f} BTC\n')
            else:
                print("⚠️ Insufficient GBP balance to buy.")

    def sell_bitcoin(self, percentage_of_funds):
        """
        Sells a portion of the current Bitcoin balance if the current sale price is at or above the sale threshold,
        based on the specified percentage of the Bitcoin holdings.

        Parameters:
        - percentage_of_funds (float): The percentage of the BTC balance to sell.
        """
        # Check if the current Bitcoin sale price is at or above the set sale threshold and if there is Bitcoin to sell.
        if self.btc_sale_price >= self.sale_threshold and self.btc_balance > 0:
            # Calculate the amount of Bitcoin to sell based on the specified percentage.
            btc_to_sell = self.btc_balance * percentage_of_funds
            # Calculate the amount of GBP to be earned from selling the Bitcoin.
            gbp_earned = btc_to_sell * self.btc_sale_price

            # Check if there is enough Bitcoin balance to sell.
            if btc_to_sell <= self.btc_balance:
                # Update the Bitcoin and GBP balances after the sale.
                self.btc_balance -= btc_to_sell
                self.gbp_balance += gbp_earned

                # Record the sell transaction details in the transaction history.
                self.transaction_history.append({
                    'type': 'sell',
                    'btc_amount': btc_to_sell,
                    'gbp_amount': gbp_earned,
                    'btc_price': self.btc_sale_price
                })

                # Print a confirmation message for the sell transaction.
                print(f'💰 Sold {btc_to_sell:.8f} BTC for £{gbp_earned:.2f}')
                print(f'💼 BTC portfolio: {self.btc_balance:.8f} BTC\n')
            else:
                print("⚠️ Insufficient BTC balance to sell.")

    def display_portfolio_status(self, initial_investment):
        """
        Displays the current status of the portfolio, including the balances of GBP and BTC,
        and calculates any earnings or losses compared to the initial investment.

        Parameters:
        - initial_investment (float): The initial GBP investment amount.
        """
        # Print the current Bitcoin balance.
        print(f'📊 You have {self.btc_balance:.8f} BTC')
        # Print the current GBP balance.
        print(f'💷 Your GBP balance is: £{self.gbp_balance:.2f}\n')

        # Calculate and display earnings if the current GBP balance is higher than the initial investment.
        if self.gbp_balance > initial_investment:
            earnings = self.gbp_balance - initial_investment
            print(f'🤑 Earnings so far: £{earnings:.2f}\n')
        # Calculate and display losses if the current GBP balance is lower than the initial investment.
        elif self.gbp_balance < initial_investment:
            loss = initial_investment - self.gbp_balance
            print(f'🥺 Running at a loss of: £{loss:.2f}\n')
        # Display a break-even message if the current GBP balance is equal to the initial investment.
        else:
            print(f'😎 Break even - you\'re still in the game.\n')


# Main Trading Logic
def main():
    """
    The main function that initializes the trading portfolio, fetches Bitcoin prices,
    and runs the continuous trading loop based on the defined thresholds.
    """
    # Create an instance of the CryptoPortfolio class with the initial investment.
    portfolio = CryptoPortfolio(INITIAL_INVESTMENT)
    # Fetch the initial Bitcoin prices and set the initial buy/sell thresholds.
    portfolio.fetch_btc_values()

    # Continue the trading loop as long as there is a positive GBP balance to trade with.
    while portfolio.gbp_balance > 0:
        # Fetch the latest Bitcoin prices and update the buy/sell thresholds in each iteration.
        portfolio.fetch_btc_values()

        # Attempt to buy Bitcoin based on the current price and the purchase threshold.
        portfolio.buy_bitcoin(PERCENTAGE_OF_FUNDS)
        # Attempt to sell Bitcoin based on the current price and the sale threshold.
        portfolio.sell_bitcoin(PERCENTAGE_OF_FUNDS)

        # Display the current status of the portfolio after potential trades.
        portfolio.display_portfolio_status(INITIAL_INVESTMENT)

        # Generate a random sleep duration within the defined range to simulate real-world market activity.
        sleep_duration = random.randint(SLEEP_MIN, SLEEP_MAX)
        print(f'⏳ Sleeping for {sleep_duration} seconds...\n')
        # Pause the script for the randomly determined duration.
        time.sleep(sleep_duration)

    # Print an exit message when the GBP balance reaches zero, indicating the end of the trading simulation.
    print('🚪 Exiting...')

# Ensure that the main function is executed only when the script is run directly (not when imported as a module).
if __name__ == '__main__':
    main()