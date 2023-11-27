import os
import pandas as pd
from dotenv import load_dotenv


def calculate_stake_size(history_sum, multiplier, desired_profit=5):
    return (desired_profit + history_sum) / (multiplier - 1)


def game_series_generator(pool_of_money, multiplier, earnings_expected):
    counter = 1
    lost = 0

    while pool_of_money > 0:
        current = calculate_stake_size(lost, multiplier, earnings_expected)
        if current > pool_of_money:
            current = pool_of_money
        yield "round: %d, current stake : %f, lost: %f" % (counter, current, lost)
        counter += 1
        lost += current
        pool_of_money -= current


def main():
    load_dotenv()
    df = pd.read_csv(os.getenv('DATA_PATH'))
    debt = 10        #losses
    max_debt = 0    #max loss
    round = 0
    wins = 0
    for row in df.itertuples():
        mult = row.Multiplier
        is_win = row.isWin
        debt += calculate_stake_size(debt, mult, 20)

        round += 1
        if debt > max_debt:
            max_debt = debt

        print("round {} - current debt: {}, max debt: {} ".format(round, debt, max_debt))
        
        if is_win:
            debt = 0
            round = 0
            wins += 1


    print(wins)
if __name__ == "__main__":
    main()
