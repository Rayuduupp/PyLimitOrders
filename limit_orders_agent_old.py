from execution_client import ExecutionClient,ExecutionException
from price_listener import PriceListener

held_count=0
product_id="IB"
price=[60,50,40,30,55]
boundary_limit=50
amount=5000
buy_flag='Y'


class LimitOrderAgent(PriceListener):

    def __init__(self, execution_client: ExecutionClient) -> None:
        """

        :param execution_client: can be used to buy or sell - see ExecutionClient protocol definition
        """
        self.execution_client=execution_client
        self.product_id=product_id
        self.price=price
        
        super().__init__()

    
       

    def on_price_tick(self, product_id: str, price: float):
        # see PriceListener protocol and readme file
        print("The current market price of",product_id,"is",price)
        current_price=price
        return current_price
    
    

objectdata=LimitOrderAgent(ExecutionClient)


           
#Function for adding new orders
def add_order(flag,product_id,amount,boundary_limit):
        for i in range(len(price)-1):
            if price[i]!=price[i+1]:
                
                
                global current_price
                current_price=objectdata.on_price_tick(product_id,price[i])
            try:
                
                if flag=='Y':
            
                    if current_price<boundary_limit and current_price<100:

                        objectdata.execution_client.buy(product_id,amount,amount)
    
                    #objectdata.buy(product_id,amount)
                
                    else:
                        print( "Order cannot be bought as the Price value is greater than 100 or outside the limit")
            
                elif flag=='N':
            
                    if current_price>=boundary_limit:
                
                        objectdata.execution_client.sell(product_id,amount,amount)
                
            except ExecutionException as e:
                        print(f"Order execution failed: {e}")
            
                    

#Function to check held orders in queue


def held_orders(held_count,buy_sell_flag,product_id,amount,boundary_limit):
    
           
        add_order(buy_sell_flag,product_id,amount,boundary_limit)


if held_count>=1:
    print("This is a held order\n")
    held_orders(held_count,buy_flag,product_id,amount,boundary_limit)
else:
    print("This is a direct order\n")
    add_order(buy_flag,product_id,amount,boundary_limit)
    



    
  
    
