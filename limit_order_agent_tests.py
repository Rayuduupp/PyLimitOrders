import unittest
from limit_order_agent import LimitOrderAgent,add_order,held_orders
from execution_client import ExecutionClient,ExecutionException

class TestLimitOrderAgent(unittest.TestCase):

    objectdata=LimitOrderAgent(ExecutionClient)
    

    def test_buy_order_execution(self):
        """Test that a buy order is executed when the price drops below the limit."""
        add_order('Y', 'IBM', 1000, 100)
        self.objectdata.on_price_tick('IBM', 99)
        
        

    def test_sell_order_execution(self):
        """Test that a sell order is executed when the price rises above the limit."""
        add_order('N', 'IBM', 500, 150)
        self.objectdata.on_price_tick('IBM', 151)
        
        

    def test_buy_order_not_executed(self):
        """Test that a buy order is not executed when the price does not reach the limit."""
        add_order('buy', 'AAPL', 200, 120)
        self.objectdata.on_price_tick('AAPL', 121)

    def test_for_held_orders(self):
        held_orders(1,'N', 'IBM', 500, 150)
                

if __name__ == "__main__":
    unittest.main()
