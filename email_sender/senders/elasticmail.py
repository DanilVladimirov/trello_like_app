from email_sender.senders.base import BaseEmailSender


class ElasticEmailSender(BaseEmailSender):
    async def _make_request(self, data, recipients):
        # request to elastic mail
        return

    def _prepare_request_data(self, data, email_type):
        return {"data": data}
