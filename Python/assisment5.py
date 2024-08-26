def calculate_total_price(prices, taxRate):

    subtotal = sum(prices)
    tax = subtotal * taxRate
    total_price = subtotal + tax
    return total_price

# Example usage:
item_prices = [19.99, 5.49, 3.50, 12.99]  # Example item prices
taxRate = 0.07  # 7% tax

total = calculate_total_price(item_prices, taxRate)
print(f"Total price including tax: ${total:.2f}")
