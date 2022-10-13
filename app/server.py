from flask import Flask, render_template, request

app = Flask(__name__)

item_list = []

before_tax = 0.0
after_tax = 0.0

i = 0

@app.route('/', methods=['POST', 'GET'])
def Calculate():
    # items = item_list
    if request.method=='POST' and "name" in request.form \
        and "price" in request.form  \
            and "quantity" in request.form \
                and "discount" in request.form \
                    and "tax" in request.form:
    
        name = str(request.form.get("name"))
        price = float(request.form.get("price"))
        quantity = int(request.form.get("quantity"))
        discount = float(request.form.get("discount"))
        tax = float(request.form.get("tax"))

        item_cost_before_tax = quantity*round(( price - (price)*(discount/100) ), 2 )
        item_cost_after_tax = round(item_cost_before_tax * (1 + (tax/100)), 2)

        # global before_tax
        # before_tax += item_cost_before_tax
        # global after_tax
        # after_tax += item_cost_after_tax

        # item = str(name + ' ' + price + ' ' + discount + ' ' + tax)
        item = []
        item.append(name)
        item.append(price)
        item.append(quantity)
        item.append(item_cost_before_tax)
        item.append(item_cost_after_tax)

        # global before_tax
        # before_tax += item_cost_before_tax
        # global after_tax
        # after_tax += item_cost_after_tax

        # item_list.append(item)

        # str(name) + ' ' + str(item_cost_before_tax) + ' ' + str(item_cost_after_tax)
        if item not in item_list:
            global before_tax
            before_tax += round(item_cost_before_tax, 2)
            global after_tax
            after_tax += round(item_cost_after_tax, 2)

            global i 
            i += 1
            item_list.append(item)


        # item_list.append(before_tax)
        # item_list.append(after_tax)

    # item_list_index = len(item_list)

    # if i >= 5:
    return render_template('checkout.html', info=item_list, total_bill=(before_tax, after_tax))
    # else:
    #     return render_template('checkout.html')

# @app.route('/remove', methods=['POST', 'GET'])
# def removeItem(i):
#     bt = item_list[i].quantity*round(( item_list[i].price - (item_list[i].price)*(item_list[i].discount/100) ), 2 )
#     at = round(bt * (1 + (item_list[i].tax/100)), 2)
#     before_tax -= bt
#     aftertax -= at
#     item_list.pop(i)
    
#     return render_template('checkout.html', info=item_list, total_bill=(before_tax, after_tax))
# @app.route('/total', methods=['POST', 'GET'])
# def calculateTotal():
#     # total = []
#     # total.append(before_tax)
#     # total.append(after_tax)
#     return render_template('checkout.html', total_bill=(before_tax, after_tax), info=item_list)



if __name__ == "__main__":
    app.run(debug=True)