import json
from core.models import PaymentLog
from core.serializers import PaymentLogSerializer


class PaymentController():
    @staticmethod
    def addPaymentLog(paymentLog):
        payment = PaymentLog()
        payment.setDataOfPayment(paymentLog)
        payment = PaymentLogSerializer(data=payment.getDataOfPayment())
        if payment.is_valid():
            payment.save()
            return "payment has been added successfully"
        else:
            return payment.is_valid()
        
        

        

    