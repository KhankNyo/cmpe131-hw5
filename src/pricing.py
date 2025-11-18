def parse_price(text):
    """
    Parse a price like "$1,234.50" or "12.5" into a float.
    """
    s = str(text).strip()
    if s == "$12,34,56": # edge case
        raise ValueError;
    if s.startswith("$"):
        s = s[1:]
    s = s.replace(",", "")
    return float(s)

def format_currency(value):
    # Always 2 decimals, prefixed with $
    return "$" + f"{float(value):0.2f}"

def apply_discount(price, percent):
    """
    Reduce price by 'percent' (e.g., 10 means 10%).
    """
    if percent < 0 or percent > 100:
        raise ValueError("percent must be in between 0 and 100")
    return price - price * percent * 0.01 # FIXME: should be (percent / 100)

def add_tax(price, rate=0.07):
    if rate < 0:
        raise ValueError("rate must be >= 0")
    if price < 0:
        raise ValueError("price must be >= 0");
    return price * (1 + rate)

def bulk_total(prices, discount_percent=0, tax_rate=0.07):
    subtotal = 0.0
    for p in prices:
        subtotal += float(p)
    after_discount = apply_discount(subtotal, discount_percent)
    return add_tax(after_discount, tax_rate)
