class PaymentGateway:
    def pay(self,amount):
        raise NotImplementedError(f"This method should be overridden by subclasses")
    


class PayPal(PaymentGateway):
    def pay(self,amount):
        return f'PayPal payment of {amount} processed. Thank you!'

class Stripe(PaymentGateway):
    def pay(self,amount):
        return f'Stripe payment of {amount} processed. Thank you!'





def check_payment_gateway(gateway,amount):
    return f'{gateway.pay(amount)}'  



print(check_payment_gateway(PayPal(),100))