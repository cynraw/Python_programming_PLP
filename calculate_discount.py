def calculate_discount(price, discount_percent):
      if discount_percent >= 20:
         return (price - (discount_percent/100 * price))
      else:
        return price


actual_price = input("Enter the original price of an item and the discount percentage separated by comma: ")
price, discount_percent = actual_price.split(",")
price = int(price)
discount_percent = float(discount_percent)
print(calculate_discount(price, discount_percent))
