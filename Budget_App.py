class Category:
    def __init__(self,category):
        self.category = category
        self.ledger = []

    def __str__(self):
        s = self.category.center(30,"*") + "\n"
        for item in self.ledger:
            temp = f"{item['description'][:23]:23}{item['amount']:7.2f}"
            s += temp + "\n"

        s += "Total: " + str(self.get_balance())
        return s   

    def deposit(self,amount,description = ""):
        self.ledger.append({"amount":amount, "description": description})

    def withdraw(self,amount,description = ""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        total_balance = 0;
        for balance in self.ledger:
            total_balance += balance["amount"] 
        return total_balance

    def transfer(self,amount,obj):
        if self.check_funds(amount):
            # widthdraw from self
            self.withdraw(amount,"Transfer to "+ obj.category)

            # deposite to obj
            obj.deposit(amount,"Transfer from "+ self.category)
            return True
        else:
            return False

    def check_funds(self,amount):
        if amount > self.get_balance():
            return False
        else:
            return True

def create_spend_chart(categories):
  spend = []
  for category in categories:
    temp = 0
    for item in category.ledger:
      if item['amount'] < 0:
        temp += abs(item['amount'])
    spend.append(temp)
  
  total = sum(spend)
  percentage = [i/total * 100 for i in spend]

  s = "Percentage spent by category"
  for i in range(100, -1, -10):
    s += "\n" + str(i).rjust(3) + "|"
    for j in percentage:
      if j > i:
        s += " o "
      else:
        s += "   "
    # Spaces
    s += " "
  s += "\n    ----------"

  cat_length = []
  for category in categories:
    cat_length.append(len(category.category))
  max_length = max(cat_length)

  for i in range(max_length):
    s += "\n    "
    for j in range(len(categories)):
      if i < cat_length[j]:
        s += " " + categories[j].category[i] + " "
      else:
        s += "   "
    # Spaces
    s += " "

  return s

food = Category("Food")
food.deposit(1000,"deposite")
food.withdraw(10.15,"groceries")
food.withdraw(15.89,"resturant")
clothing = Category("Clothing")
food.transfer(50,clothing)
print(food)