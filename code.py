import unittest
# Step 1: Define the menu with dining options and prices
menu = {
    'Hamburguesa': 5.0,
    'Alitas': 10.0,
    'Lasagna': 8.0,
    'Chef\'s Special 1': 25.0,
    'Chef\'s Special 2': 30.0,
}

# Step 2: Function to get meal selection and quantity from the user
def get_user_order():
    order = {}
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: ${price}")

    while True:
        meal = input("Enter meal name (type 'done' to finish): ")
        if meal.lower() == 'done':
            break

        quantity = int(input("Enter quantity: "))
        while quantity <= 0:
            quantity = int(input("Invalid quantity. Enter a positive integer greater than zero: "))
        
        if meal in menu:
            order[meal] = quantity
        else:
            print("Meal not available. Please re-select.")
    
    return order

# Step 3: Function to calculate the total cost
def calculate_total_cost(order):
    total_quantity = sum(order.values())
    total_cost = sum([menu[meal] * quantity for meal, quantity in order.items()])
    
    if total_quantity > 5:
        total_cost = total_cost - (total_cost*0.10)  # 10% discount for more than 5 meals
    if total_quantity > 10:
        total_cost = total_cost - (total_cost*0.20)  # Additional 20% discount for more than 10 meals

    # Check for special meal category and apply surcharge
    special_meals = [meal for meal in order.keys() if 'Chef\'s Special' in meal]
    if special_meals:
        total_cost = total_cost - (total_cost*0.05) # 5% surcharge for special meals
    
    # Check for special offer discounts
    if total_cost > 100:
        total_cost -= 25
    elif total_cost > 50:
        total_cost -= 10
    
    return total_cost

# Step 4: Function to validate and finalize the order
def confirm_order(order):
    print("Selected meals and quantities:")
    for meal, quantity in order.items():
        print(f"{meal}: {quantity}")

    total_cost = calculate_total_cost(order)
    print(f"Total cost: ${total_cost}")

    confirmation = input("Confirm the order (Y/N)? ")
    if confirmation.lower() == 'y':
        return total_cost
    else:
        return -1

# Step 5: Putting it all together
def dining_experience_manager():
    print("Welcome to the Dining Experience Manager!")
    while True:
        order = get_user_order()
        if not order:
            print("Order canceled.")
            return -1
        
        if sum(order.values()) > 100:
            print("Maximum order quantity exceeded. Please re-enter quantities.")
            continue
        
        total_cost = confirm_order(order)
        if total_cost >= 0:
            print("Order confirmed.")
            return total_cost
        else:
            print("Order canceled. Please make changes to the selections.")

if __name__ == "__main__":
    total_cost = dining_experience_manager()
    if total_cost >= 0:
        print(f"Total cost of the dining experience: ${total_cost}")

class TestDiningExperienceManager(unittest.TestCase):

    def test_calculate_total_cost_base_case(self):
        order = {'Hamburguesa': 2, 'Alitas': 3}
        total_cost = calculate_total_cost(order)
        self.assertAlmostEqual(total_cost, 40.0, places=2)

    def test_calculate_total_cost_discount_10(self):
        order = {'Lasagna': 6, 'Chef\'s Special 1': 5, 'Alitas': 4}
        total_cost = calculate_total_cost(order)
        self.assertAlmostEqual(total_cost, 204.0, places=2)

    def test_calculate_total_cost_discount_20(self):
        order = {'Chef\'s Special 2': 12}
        total_cost = calculate_total_cost(order)
        self.assertAlmostEqual(total_cost, 288.0, places=2)

    def test_calculate_total_cost_special_surcharge(self):
        order = {'Chef\'s Special 1': 3, 'Chef\'s Special 2': 2}
        total_cost = calculate_total_cost(order)
        self.assertAlmostEqual(total_cost, 160.5, places=2)

    def test_calculate_total_cost_special_offer_discount(self):
        order = {'Alitas': 15, 'Lasagna': 6}
        total_cost = calculate_total_cost(order)
        self.assertAlmostEqual(total_cost, 160.0, places=2)

if __name__ == "__main__":
    unittest.main()