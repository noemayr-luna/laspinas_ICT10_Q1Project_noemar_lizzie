
from pyscript import display, document


def SKU_generator(*args):
    category = document.getElementById("category").value.strip()
    product_name = document.getElementById("product_name").value.strip()
    stock_qty = document.getElementById("quantity").value.strip()

    output = document.getElementById("sku_output")

    if not category or not product_name or not stock_qty:
        output.innerHTML = (
            '<p class="error">Please fill in all fields.</p>'
        )
        return

    try:
        quantity = int(stock_qty)

        if quantity < 0 or quantity > 999:
            output.innerHTML = (
                '<p class="error">Quantity must be between 0 and 999.</p>'
            )
            return

    except ValueError:
        output.innerHTML = (
            '<p class="error">Enter a whole-number quantity.</p>'
        )
        return

    # Create an 8-character alphanumeric SKU:
    # 2 category characters + 3 product characters + 3 quantity digits

    category_part = "".join(
        char for char in category.upper() if char.isalnum()
    )[:2]

    product_part = "".join(
        char for char in product_name.upper() if char.isalnum()
    )[:3]

    category_part = category_part.ljust(2, "X")
    product_part = product_part.ljust(3, "X")

    quantity_part = f"{quantity:03d}"

    sku = category_part + product_part + quantity_part

    output.innerHTML = ""
    display("SKU: " + sku, target="sku_output")


def create_order(*args):
    products = [
        document.getElementById("item1"),
        document.getElementById("item2"),
        document.getElementById("item3"),
        document.getElementById("item4"),
        document.getElementById("item5"),
    ]

    names = [
        "Americano",
        "Spanish Latte",
        "Iced Tea",
        "Cold Brew",
        "Caramel Macchiato",
    ]

    subtotal = 0.0
    selected_items = []

    for product, name in zip(products, names):
        if product.checked:
            price = float(product.value)
            subtotal += price

            selected_items.append(
                f"<li>{name} - ₱{price:.2f}</li>"
            )

    tax = subtotal * 0.12
    total = subtotal + tax

    if selected_items:
        items_html = "".join(selected_items)
    else:
        items_html = "<li>No products selected.</li>"

    receipt = f"""
    <div class="receipt-card">
        <h3>==== RECEIPT ====</h3>

        <strong>Items:</strong>
        <ul>{items_html}</ul>

        <p>
            <span>Subtotal:</span>
            <strong>₱{subtotal:.2f}</strong>
        </p>

        <p>
            <span>VAT (12%):</span>
            <strong>₱{tax:.2f}</strong>
        </p>

        <hr>

        <p class="total">
            <span>Total:</span>
            <strong>₱{total:.2f}</strong>
        </p>
    </div>
    """

    document.getElementById("show").innerHTML = receipt
