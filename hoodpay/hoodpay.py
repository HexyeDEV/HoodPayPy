import requests, aiohttp
from typing import Union, Optional
from datetime import datetime
from .types.payment import Payment


class HoodPay:
    """Represents a HoodPay API client."""

    def __init__(self, api_key: str, business_id: int):
        """Initialize the HoodPay API client.
        
        Parameters
        ----------
        api_key: `str`
            The API key for your HoodPay account.
        business_id: `int`
            The business ID for your HoodPay account."""
        self.api_key = api_key
        self.business_id = business_id
        self.base_url = "https://api.hoodpay.com/v1"
        self.base_headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
    
    def get_payments(self, page_number: Optional[int] = None, page_size: Optional[int] = None, from_time: Optional[int] = None, status: Optional[str] = None, payment_method: Optional[str] = "DIRECT_CRYPTO", from_amount: Optional[float] = None, to_amount: Optional[float] = None, search_string: Optional[str] = None) -> dict:
        """Get a list of payments that belong to a specific business.
        
        Parameters
        ----------
        page_number: `Optional[int]`
            The page number to get. Defaults to None.
        page_size: `Optional[int]`
            The number of payments to get per page. Defaults to None.
        from_time: `Optional[int]`
            The time to get payments from. Defaults to None.
        status: `Optional[str]`
            The status of the payments to get. Defaults to None.
        payment_method: `Optional[str]`
            The payment method to get payments for. Defaults to "DIRECT_CRYPTO".
        from_amount: `Optional[float]`
            The minimum amount of the payments to get. Defaults to None.
        to_amount: `Optional[float]`
            The maximum amount of the payments to get. Defaults to None.
        search_string: `Optional[str]`
            The search string to use to filter payments. Defaults to None."""
        params = {
            "pageNumber": page_number,
            "pageSize": page_size,
            "fromTime": from_time,
            "status": status,
            "paymentMethod": payment_method,
            "fromAmount": from_amount,
            "toAmount": to_amount,
            "searchString": search_string
        }
        r = requests.get(f"{self.base_url}/businesses/{self.business_id}/payments", params=params, headers=self.base_headers).json()
        try:
            r["data"][0]["id"]
            result = []
            for payment in r["data"]:
                result.append(Payment(payment))
            return result
        except:
            raise Exception(f"Error: {r['message']}")
    
    async def get_payments_async(self, page_number: Optional[int] = None, page_size: Optional[int] = None, from_time: Optional[datetime] = None, status: Optional[str] = None, payment_method: Optional[str] = "DIRECT_CRYPTO", from_amount: Optional[float] = None, to_amount: Optional[float] = None, search_string: Optional[str] = None) -> dict:
        """Get a list of payments that belong to a specific business asynchronously.

        Parameters
        ----------
        page_number: `Optional[int]`
            The page number to get. Defaults to None.
        page_size: `Optional[int]`
            The number of payments to get per page. Defaults to None.
        from_time: `Optional[datetime]`
            The time to get payments from. Defaults to None.
        status: `Optional[str]`
            The status of the payments to get. Defaults to None.
        payment_method: `Optional[str]`
            The payment method to get payments for. Defaults to "DIRECT_CRYPTO".
        from_amount: `Optional[float]`
            The minimum amount of the payments to get. Defaults to None.
        to_amount: `Optional[float]`
            The maximum amount of the payments to get. Defaults to None.
        search_string: `Optional[str]`
            The search string to use to filter payments. Defaults to None."""
        params = {
            "pageNumber": page_number,
            "pageSize": page_size,
            "fromTime": from_time,
            "status": status,
            "paymentMethod": payment_method,
            "fromAmount": from_amount,
            "toAmount": to_amount,
            "searchString": search_string
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.base_url}/businesses/{self.business_id}/payments", params=params, headers=self.base_headers) as r:
                r = await r.json()
                try:
                    r["data"][0]["id"]
                    result = []
                    for payment in r["data"]:
                        result.append(Payment(payment))
                    return result
                except:
                    raise Exception(f"Error: {r['message']}")
    
    def create_payment(self, currency: str, amount: float, name: Optional[str] = None, description: Optional[str] = None, customer_email: Optional[str] = None, customer_ip: Optional[str] = None, customer_user_agent: Optional[str] = None, redirect_url: Optional[str] = None, notify_url: Optional[str] = None) -> dict:
        """Create a payment.
        
        Parameters
        ----------
        currency: `str`
            The currency of the payment.
        amount: `float`
            The amount of the payment.
        name: `Optional[str]`
            The name of the payment. Defaults to None.
        description: `Optional[str]`
            The description of the payment. Defaults to None.
        customer_email: `Optional[str]`
            The email of the customer. Defaults to None.
        customer_ip: `Optional[str]`
            The IP address of the customer. Defaults to None.
        customer_user_agent: `Optional[str]`
            The user agent of the customer. Defaults to None.
        redirect_url: `Optional[str]`
            The URL to redirect the customer to after payment. Defaults to None.
        notify_url: `Optional[str]`
            The URL to notify after payment. Defaults to None."""
        data = {
            "currency": currency,
            "amount": amount,
            "name": name,
            "description": description,
            "customerEmail": customer_email,
            "customerIp": customer_ip,
            "customerUserAgent": customer_user_agent,
            "redirectUrl": redirect_url,
            "notifyUrl": notify_url
        }
        r = requests.post(f"{self.base_url}/businesses/{self.business_id}/payments", json=data, headers=self.base_headers).json()
        return r
    
    async def create_payment_async(self, currency: str, amount: float, name: Optional[str] = None, description: Optional[str] = None, customer_email: Optional[str] = None, customer_ip: Optional[str] = None, customer_user_agent: Optional[str] = None, redirect_url: Optional[str] = None, notify_url: Optional[str] = None) -> dict:
        """Create a payment asynchronously.
        
        Parameters
        ----------
        currency: `str`
            The currency of the payment.
        amount: `float`
            The amount of the payment.
        name: `Optional[str]`
            The name of the payment. Defaults to None.
        description: `Optional[str]`
            The description of the payment. Defaults to None.
        customer_email: `Optional[str]`
            The email of the customer. Defaults to None.
        customer_ip: `Optional[str]`
            The IP address of the customer. Defaults to None.
        customer_user_agent: `Optional[str]`
            The user agent of the customer. Defaults to None.
        redirect_url: `Optional[str]`
            The URL to redirect the customer to after payment. Defaults to None.
        notify_url: `Optional[str]`
            The URL to notify after payment. Defaults to None."""
        data = {
            "currency": currency,
            "amount": amount,
            "name": name,
            "description": description,
            "customerEmail": customer_email,
            "customerIp": customer_ip,
            "customerUserAgent": customer_user_agent,
            "redirectUrl": redirect_url,
            "notifyUrl": notify_url
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{self.base_url}/businesses/{self.business_id}/payments", json=data, headers=self.base_headers) as r:
                r = await r.json()
                return r
    
    def get_payment(self, payment_id: int) -> dict:
        """Get a payment by its ID.
        
        Parameters
        ----------
        payment_id: `int`
            The ID of the payment."""
        r = requests.get(f"{self.base_url}/businesses/{self.business_id}/payments/{payment_id}", headers=self.base_headers).json()
        return r

    async def get_payment_async(self, payment_id: int) -> dict:
        """Get a payment by its ID asynchronously.
        
        Parameters
        ----------
        payment_id: `int`
            The ID of the payment."""
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.base_url}/businesses/{self.business_id}/payments/{payment_id}", headers=self.base_headers) as r:
                r = await r.json()
                return r
    
    def select_payment_method(self, payment_id: int, payment_method: str) -> dict:
        """Select a payment method for a payment.
        
        Parameters
        ----------
        payment_id: `int`
            The ID of the payment.
        payment_method: `str`
            The payment method to select."""
        data = {
            "direct_Crypto": payment_method
        }
        r = requests.post(f"{self.base_url}/public/payments/hosted-page/{payment_id}/select-payment-method", json=data, headers=self.base_headers).json()
        return r
    
    async def select_payment_method_async(self, payment_id: int, payment_method: str) -> dict:
        """Select a payment method for a payment asynchronously.
        
        Parameters
        ----------
        payment_id: `int`
            The ID of the payment.
        payment_method: `str`
            The payment method to select."""
        data = {
            "direct_Crypto": payment_method
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{self.base_url}/public/payments/hosted-page/{payment_id}/select-payment-method", json=data, headers=self.base_headers) as r:
                r = await r.json()
                return r
    
    def fill_customer_email(self, payment_id: int, email: str) -> dict:
        """Fill the customer email for a payment.
        
        Parameters
        ----------
        payment_id: `int`
            The ID of the payment.
        email: `str`
            The email to fill."""
        data = {
            "email": email
        }
        r = requests.post(f"{self.base_url}/public/payments/hosted-page/{payment_id}/customer_email", json=data, headers=self.base_headers).json()
        return r
    
    async def fill_customer_email_async(self, payment_id: int, email: str) -> dict:
        """Fill the customer email for a payment asynchronously.

        Parameters
        ----------
        payment_id: `int`
            The ID of the payment.
        email: `str`
            The email to fill."""
        data = {
            "email": email
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{self.base_url}/public/payments/hosted-page/{payment_id}/customer_email", json=data, headers=self.base_headers) as r:
                r = await r.json()
                return r
    
    def cancel_payment(self, payment_id: str) -> dict:
        """Cancel a payment.
        
        Parameters
        ----------
        payment_id: `str`
            The ID of the payment."""
        r = requests.post(f"{self.base_url}/public/payments/hosted-page/{payment_id}/cancel", headers=self.base_headers).json()
        return r

    async def cancel_payment_async(self, payment_id: str) -> dict:
        """Cancel a payment asynchronously.
        
        Parameters
        ----------
        payment_id: `str`
            The ID of the payment."""
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{self.base_url}/public/payments/hosted-page/{payment_id}/cancel", headers=self.base_headers) as r:
                r = await r.json()
                return r
    
    def get_webhooks(self) -> dict:
        "Receives the webhooks settings for the business"
        r = requests.get(f"{self.base_url}/dash/businesses/{self.business_id}/settings/developer/webhooks", headers=self.base_headers).json()
        return r

    async def get_webhooks_async(self) -> dict:
        "Receives the webhooks settings for the business asynchronously"
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.base_url}/dash/businesses/{self.business_id}/settings/developer/webhooks", headers=self.base_headers) as r:
                r = await r.json()
                return r
    
    def create_webhook(self, url: Optional[str] = None, description: Optional[str] = None, events: Optional[list] = None) -> dict:
        """Creates a webhook for the business.
        
        Parameters
        ----------
        url: `Optional[str]`
            The URL to send the webhook to. Defaults to None.
        description: `Optional[str]`
            The description of the webhook. Defaults to None.
        events: `Optional[list]`
            The events to send the webhook for. Defaults to None."""
        data = {
            "url": url,
            "description": description,
            "events": events
        }
        r = requests.post(f"{self.base_url}/dash/businesses/{self.business_id}/settings/developer/webhooks", json=data, headers=self.base_headers).json()
        return r

    async def create_webhook_async(self, url: Optional[str] = None, description: Optional[str] = None, events: Optional[list] = None) -> dict:
        """Creates a webhook for the business asynchronously.
        
        Parameters
        ----------
        url: `Optional[str]`
            The URL to send the webhook to. Defaults to None.
        description: `Optional[str]`
            The description of the webhook. Defaults to None.
        events: `Optional[list]`
            The events to send the webhook for. Defaults to None."""
        data = {
            "url": url,
            "description": description,
            "events": events
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{self.base_url}/dash/businesses/{self.business_id}/settings/developer/webhooks", json=data, headers=self.base_headers) as r:
                r = await r.json()
                return r
    
    def reset_webhook_secret(self) -> dict:
        "Resets the webhook secret for the business"
        r = requests.post(f"{self.base_url}/dash/businesses/{self.business_id}/settings/developer/webhooks/reset-secret", headers=self.base_headers).json()
        return r
    
    async def reset_webhook_secret_async(self) -> dict:
        """Resets the webhook secret for the business asynchronously."""
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{self.base_url}/dash/businesses/{self.business_id}/settings/developer/webhooks/reset-secret", headers=self.base_headers) as r:
                r = await r.json()
                return r
    
    def delete_webhook(self, webhook_id: int) -> dict:
        """Deletes a webhook for the business.
        
        Parameters
        ----------
        webhook_id: `int`
            The ID of the webhook."""
        r = requests.delete(f"{self.base_url}/dash/businesses/{self.business_id}/settings/developer/webhooks/{webhook_id}", headers=self.base_headers).json()
        return r

    async def delete_webhook_async(self, webhook_id: int) -> dict:
        """Deletes a webhook for the business asynchronously.
        
        Parameters
        ----------
        webhook_id: `int`
            The ID of the webhook."""
        async with aiohttp.ClientSession() as session:
            async with session.delete(f"{self.base_url}/dash/businesses/{self.business_id}/settings/developer/webhooks/{webhook_id}", headers=self.base_headers) as r:
                r = await r.json()
                return r
    
    def get_businesses(self) -> dict:
        """Returns a list of businesses for the authenticated user."""
        r = requests.get(f"{self.base_url}/dash/businesses", headers=self.base_headers).json()
        return r

    async def get_businesses_async(self) -> dict:
        """Returns a list of businesses for the authenticated user asynchronously."""
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.base_url}/dash/businesses", headers=self.base_headers) as r:
                r = await r.json()
                return r