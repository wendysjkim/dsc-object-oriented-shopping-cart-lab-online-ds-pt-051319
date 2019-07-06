class ShoppingCart:
    # write your code here
    def __init__(self, employee_discount=None, items=[]):
      self.total = 0
      self.employee_discount = employee_discount
      self.items = items

    def add_item(self, name, price, quantity=1):
      for i in range(quantity):  
        self.items.append({"name": name, "price":price})
        self.total += price
      return self.total
 
    def mean_item_price(self):
      prices = sorted([item["price"] for item in self.items], reverse=True)
      length = len(prices)
      mean = self.total / length   
      return mean

    def median_item_price(self):
      prices = sorted([item["price"] for item in self.items], reverse=True)
      length = len(prices)  
      if length % 2 == 1:
        median = prices[length//2+1]
      else:
        median =  (prices[length//2]+ prices[length//2+1])/2            
      return median 

    def apply_discount(self):
      if self.employee_discount:
        disc_total =  self.total * (100 - self.employee_discount)/100 
        return disc_total 
      else:
        print("Sorry, there is no discount to apply to your cart :(") 

    def void_last_item(self):
      if self.items:
        removed = self.items.pop()
      else:
        return("There are no items in your cart!")
      self.total -= removed['price']
