class DirectCryptoCharge:
    """Represents a HoodPay direct crypto charge.
    
    Attributes
    ----------
    amount: `float`
        The amount of the charge.
    currency: `str`
        The currency of the charge."""
    
    def __init__(self, data: dict):
        self.amount = data["amount"]
        self.currency = data["currency"]