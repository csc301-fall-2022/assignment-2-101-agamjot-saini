import unittest
# from flask.testing import TestCase


item_list = []
before_tax = 0.0
after_tax = 0.0
i = 0

# SAME FUNCTION AS IN SERVER.PY, except attributes are passed in as parameters for easy testing.
def Calculate(name, price, quantity, discount, tax):

    name = str(name)
    price = float(price)
    quantity = int(quantity)
    discount = float(discount)
    tax = float(tax)

    item_cost_before_tax = round(quantity*round(( price - (price)*(discount/100) ), 2 ), 2)
    item_cost_after_tax = round(item_cost_before_tax * (1 + (tax/100)), 2)


    item = []
    item.append(name)
    item.append(price)
    item.append(quantity)
    item.append(item_cost_before_tax)
    item.append(item_cost_after_tax)


    if item not in item_list:
        global before_tax
        before_tax += round(item_cost_before_tax, 2)
        global after_tax
        after_tax += round(item_cost_after_tax, 2)

        global i 
        i += 1
        item_list.append(item)

    return item_list, round(before_tax, 2), round(after_tax, 2)


# SAME FUNCTION AS IN SERVER.PY, except return item_list, before_tax, after_tax for testing.
def clear():
    global item_list
    item_list = []

    global before_tax
    before_tax = 0.0
    global after_tax 
    after_tax = 0.0

    global i
    i = 0
    return item_list, before_tax, after_tax

class TestCalculate(unittest.TestCase):
    def test_calculate(self):
        # print(Calculate("agam", 5, 2, 0, 10))
        self.assertAlmostEqual(Calculate("agam", 5, 2, 0, 10), ([["agam", 5, 2, 10, 11]], 10, 11))

class TestClear(unittest.TestCase):
    def test_clear(self):
        global item_list 
        item_list.append(["agam", 5, 2, 0, 10])
        self.assertAlmostEqual(clear(), ([], 0.0, 0.0))
    


if __name__ == "__main__":
    unittest.main()
