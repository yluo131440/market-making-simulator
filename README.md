Market-Making Simulator

A Python-based market-making simulator exploring bid-ask spreads, inventory management, execution probabilities, and Monte Carlo PnL analysis.

Overview

This project implements a simplified market-making model to study how a market maker’s quotes, inventory, and cash balance evolve when processing customer orders.

The simulator uses Monte Carlo experiments to evaluate the distribution of profit and loss (PnL) under a specified set of model parameters.

Features

* Bid-ask quote calculation: Computes bid and ask prices from a reference price and a specified spread.
* Inventory management: Updates inventory based on customer buy and sell orders.
* Cash accounting: Tracks cash changes resulting from executed trades.
* Inventory-aware quoting: Adjusts the quote center according to deviations from a target inventory.
* Execution probability: Models the probability of an order being filled as a function of the spread.
* Monte Carlo simulation: Runs repeated simulations and calculates average PnL, the proportion of profitable runs, and PnL standard deviation.

Model Assumptions

The current implementation is intentionally simplified:

* The reference market price remains fixed during each simulation.
* The customer order sequence and order sizes are predetermined.
* Execution probability depends on the quoted spread.
* The model does not yet include transaction costs, dynamic market prices, or a realistic limit order book.

These assumptions make the simulator useful for exploring basic market-making mechanics, but its results should not be interpreted as evidence of a real-world trading strategy’s profitability.

How to Run

Requirements: Python 3.

Run the script from a terminal:

python market-making-simulator.py

The script runs 1,000 Monte Carlo simulations using the configured parameters and reports:

* Number of simulations
* Average PnL
* Proportion of profitable runs
* PnL standard deviation

Implementation

The project is organized around several core functions:

* calculate_quotes()
* calculate_fill_probability()
* execute_trade()
* execute_cash()
* adjust_mid_price()
* run_simulation()
* calculate_pnl()

Future Improvements

* Compare multiple bid-ask spread settings.
* Introduce stochastic market price dynamics.
* Compare alternative inventory-management strategies.
* Add unit tests and reproducible experiments.
* Visualize PnL distributions and risk metrics.

Disclaimer

This is an educational simulation project. It is not intended for live trading or investment advice.
