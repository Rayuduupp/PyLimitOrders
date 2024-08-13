import unittest
from limit_order_agent import LimitOrderAgent
from execution_client import ExecutionClient

from unittest.mock import MagicMock


object1 = LimitOrderAgent(ExecutionClient)

class LimitOrderAgentTest(unittest.TestCase):

    def setUp(self):
        self.execution_client = MagicMock()
        self.new_execution_client = LimitOrderAgent(self.execution_client)

    
    def test_add_order(self):
        # Initial length of orders list
        initial_length = len(object1.new_orders)

        self.new_execution_client.add_order('buy', 'IBM', 1000, 100)
        self.assertEqual(len(self.new_execution_client.new_orders), initial_length + 1)

        self.new_execution_client.add_order('sell', 'IBM', 1001, 99)
        self.assertEqual(len(self.new_execution_client.new_orders), initial_length + 2)
    def test_add_order_details(self):
        # Verify that the order data was added successfully

        self.new_execution_client.add_order('buy', 'IBM', 1000, 154)
        
        new_order = self.new_execution_client.new_orders[-1]
        self.assertEqual(new_order[0], 'buy')
        self.assertEqual(new_order[1], 'IBM')
        self.assertIsInstance(new_order[1],str)
        self.assertEqual(new_order[2], 1000)
        self.assertEqual(new_order[3], 154)
        self.assertIsInstance(new_order[3],int)

        self.new_execution_client.add_order('sell', 'IBM', 1001, 145)
        # Verify that the order was added successfully
        
        new_order = self.new_execution_client.new_orders[-1]
        self.assertEqual(new_order[0], 'sell')
        self.assertEqual(new_order[1], 'IBM')
        self.assertIsInstance(new_order[1],str)
        self.assertEqual(new_order[2], 1001)
        self.assertEqual(new_order[3], 145)
        self.assertIsInstance(new_order[3],int)
        

    def test_on_price_tick(self):
        # Add a buy order for IBM at $100
        self.new_execution_client.add_order('buy', 'IBM', 1000, 102)
        self.new_execution_client.add_order('buy', 'IBM', 1000, 105)
        self.new_execution_client.on_price_tick('IBM', 99)
        #check if the all buy  order is processed successfully
        self.assertFalse(len(self.new_execution_client.new_orders))
        #for selling orders
        self.new_execution_client.add_order('sell', 'IBM', 1000, 130)
        self.new_execution_client.add_order('sell', 'IBM', 1000, 120)
        self.new_execution_client.on_price_tick('IBM', 150)
        #check if the sell order is processed successfully
        self.assertFalse(len(self.new_execution_client.new_orders))
        
if __name__ == "__main__":
    unittest.main()
