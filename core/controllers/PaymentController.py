import json
from core.models import PaymentLog
from core.serializers import PaymentLogSerializer


class PaymentController():
    @staticmethod
    def payment(request):
        request = json.loads(request.body)
        payment=PaymentLog()
        payment.setDataOfPayment(request)
        payment=PaymentLogSerializer(data=payment.getDataOfPayment())
        payment.save()
        
        

        

    