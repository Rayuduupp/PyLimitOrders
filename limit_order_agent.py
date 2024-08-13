from execution_client import ExecutionClient,ExecutionException
from price_listener import PriceListener




class LimitOrderAgent(PriceListener):

    def __init__(self, execution_client: ExecutionClient) -> None:
        """

        :param execution_client: can be used to buy or sell - see ExecutionClient protocol definition
        """
        self.execution_client=execution_client
        self.new_orders=[]
        self.processed_orders=[]
        super().__init__()

    #Function for adding new orders
    def add_order(self,flag,product_id,amount,boundary_limit):
        if amount<=0 or boundary_limit<=0:
            raise ValueError("Order Amount/limit cannot be 0,please provide value greater than 0")
        if flag not in {"buy","sell"}:
            raise ValueError("flag should contain either buy or sell method")
        self.new_orders.append((flag,product_id,amount,boundary_limit))
        
    
       
    # Function for buying and selling orders based on current market trend
    def on_price_tick(self, product_id: str, price: float):
        # see PriceListener protocol and readme file
        print("The current market price of",product_id,"is",price)
        current_price=price
        
        for orders in self.new_orders[:]:
            flag,product_id,amount,boundary_limit=orders
            
            if product_id==product_id:
                
                
                try:
                
                    if flag=='buy' and  current_price<=boundary_limit:
                        self.execution_client.buy(product_id,amount)
                        print(orders, "order Processed successfully")
                        self.new_orders.remove(orders)
                        
                      
                
                      
                    elif flag=='sell' and current_price>=boundary_limit:  
                        self.execution_client.sell(product_id,amount)
                        print(orders, "order Processed successfully")
                        self.new_orders.remove(orders)
                    else:
                        print(orders,"Order cannot", flag," as the price is not within the limit")
                        continue
                
                except ExecutionException as e:
                        
                        print(f"Order execution failed: {e}")
            
        
        






        
        
            
        
        
            
            




           

        
            
                    





    
