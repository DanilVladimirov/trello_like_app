from email_sender.senders import elasticmail
from email_sender.senders import base


class EmailSenderFactory:
    PROVIDERS = {
        "elasticmail": elasticmail.ElasticEmailSender
    }

    @classmethod
    def get_sender(cls, provider="elasticmail") -> base.BaseEmailSender:
        return cls.PROVIDERS[provider]()
