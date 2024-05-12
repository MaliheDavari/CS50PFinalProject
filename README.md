# Binance price provider

**Video Demo:**  <https://youtu.be/PznJXA-eqCY>

**Description:**

Cryptocurrency trading has become popular worldwide, attracting both experienced investors and curious beginners. In
this guide, we’ll explore how to create a program for buying and selling digital currencies.

This Python program prints the mean, minimum, and maximum prices of BTC and ETH in the past 10 seconds with a 2 seconds
time interval.

## Details:

The files in this program:

### Project.py:

The requirements for this program involve two inputs. First, we need to determine whether the customer wants to sell or
buy cryptocurrency. Next, we must identify the type of cryptocurrency being ordered.
The program retrieves JSON data related to the chosen cryptocurrency from the Binance website. The results obtained from
the website include a set of prices in USD. Here’s how the process works:

### Sell Request:

If the request is to sell, the program looks at the ‘bids’ section. Within ‘bids’, there are several lists. Each
list contains two numbers:
The first number represents the highest price at which the chosen currency can be sold.
The second number indicates the amount of the currency that the customer can sell at that price.
The subsequent lists include progressively lower prices for the chosen currency.
### Buy Request:

If the request is to buy, a similar process is followed. However, instead of ‘bids’, the program selects the ‘asks’
section. The first list within ‘asks’ includes the lowest price at which the customer can purchase the chosen currency.

### Results

The program saves the first price, which represents the best price for either selling or buying the cryptocurrency. It
continuously retrieves new data from the Binance website at 2-second intervals. As the number of elements in the list
reaches 5, the program calculates and prints the minimum, mean, and maximum prices observed within the past 10 seconds.
After each time interval, the oldest price is removed, and the new set of prices is printed. This process continues
until the customer decides to exit the program.
