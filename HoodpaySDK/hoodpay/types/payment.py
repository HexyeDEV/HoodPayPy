from datetime import datetime
from .directcryptocharge import DirectCryptoCharge

class Payment:
    """Represents a HoodPay payment.
    
    Attributes
    ----------
    id: `int`
        The ID of the payment.
    end_amount: `float`
        The amount of the payment.
    currency: `str`
        The currency of the payment.
    description: `str`
        The description of the payment.
    customer_email: `str`
        The email of the customer.
    created_at: `datetime`
        The time the payment was created.
    status: `str`
        The status of the payment.
    selected_payment_method: `str`
        The payment method used for the payment.
    direct_crypto_charge: `DirectCryptoCharge`
        The direct crypto charge of the payment.
    """

    def __init__(self, data: dict):
        self.id = data["id"]
        self.end_amount = data["endAmount"]
        self.currency = data["currency"]
        self.description = data["description"]
        self.customer_email = data["customerEmail"]
        self.created_at = datetime.fromtimestamp(data["createdAt"])
        self.status = data["status"]
        self.selected_payment_method = data["selectedPaymentMethod"]
        self.direct_crypto_charge = DirectCryptoCharge(data["directCryptoCharge"])