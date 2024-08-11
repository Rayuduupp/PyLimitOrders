from trading_framework.execution_client import ExecutionClient
from trading_framework.price_listener import PriceListener


class LimitOrderAgent(PriceListener):

    def __init__(self, execution_client: ExecutionClient) -> None:
        """

        :param execution_client: can be used to buy or sell - see ExecutionClient protocol definition
        """
        self.execution_client=execution_client
        super().__init__()

    def buy(self, product_id: str, amount: int):
        """
        Execute a buy order, throws ExecutionException on failure
        :param product_id: the product to buy
        :param amount: the amount to buy
        :return: None
        """
        
        number_of_orders_bought=0
        number_of_orders_bought=(amount/current_price)
        if number_of_orders_bought==0:
            raise Exception("cannot buy orders")
        return number_of_orders_bought
        

    def sell(self, product_id: str, amount: int):
        """
        Execute a sell order, throws ExecutionException on failure
        :param product_id: the product to sell
        :param amount: the amount to sell
        :return: None
        """
        number_of_sold_orders=0
        number_of_sold_orders=(amount/current_price)
        if number_of_sold_orders==0:
            raise Exception("cannot sell orders")
        return number_of_sold_orders

    def on_price_tick(self, product_id: str, price: float):
        # see PriceListener protocol and readme file
        print("The current market price of",self.product_id,"is",self.price)
        current_price=self.price
        return self.price
    
    

objectdata=LimitOrderAgent()

def add_order(flag,product_id,amount,boundary_limit):
        if flag=='Y':
            current_price=self.price
            if current_price<100:
        
                objectdata.buy("IBM",current_price)
            
        elif flag=='N':
            current_price=self.price
            if current_price<100:
                objectdata.sell("IBM",current_price)

def held_orders(held_orders,buy_sell_flag,product_id,amount):
    
    if held_orders>=1:
        
        objectdata.add_order(buy_sell_flag,product_id,amount,boundary_limit)

            
    
