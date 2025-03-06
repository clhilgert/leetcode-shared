from src.day2.best_time_to_buy_and_sell_stock import best_time_to_buy

def test_best_time_to_buy():
    prices1 = [10,1,5,6,7,1]
    prices2 = [10,8,7,5,2]
    assert(best_time_to_buy(prices1)) == 6
    assert(best_time_to_buy(prices2)) == 0
