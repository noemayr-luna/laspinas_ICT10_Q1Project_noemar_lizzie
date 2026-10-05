from pyscript import display, document


def SKU_generator():

    document.getElementById("sku_output").innerHTML = ""

    category = document.getElementById("category").value

    product_name = document.getElementById("product_name").value

    stock_qty = document.getElementById("quantity").value

    sku = (
        category[:3].upper()
        + "-"
        + product_name[:4].upper()
        + "-"
        + str(stock_qty)
    )

    display(
        "SKU: " + sku,
        target="sku_output"
    )


def create_order():

    prod1 = document.getElementById("item1")
    prod2 = document.getElementById("item2")
    prod3 = document.getElementById("item3")
    prod4 = document.getElementById("item4")
    prod5 = document.getElementById("item5")


    subtotal = (
        float(prod1.value) * prod1.checked
        + float(prod2.value) * prod2.checked
        + float(prod3.value) * prod3.checked
        + float(prod4.value) * prod4.checked
        + float(prod5.value) * prod5.checked
    )


    tax_rate = 0.12

    tax = subtotal * tax_rate

    total = subtotal + tax


    receipt = f"""
    <h3>==== Receipt ====</h3>

    <p>Subtotal: ₱{subtotal:.2f}</p>

    <p>VAT: ₱{tax:.2f}</p>

    <p>Total: ₱{total:.2f}</p>
    """


    document.getElementById("show").innerHTML = receipt
