from email_sender.constants import EmailTypes


class BaseEmailSender:

    EMAIL_TEMPLATES = {
        EmailTypes.TASK_UPDATED: {
            "template": "task_updated.html",
            "subject": "Task {{ name }} updated"
        }
    }

    async def _make_request(self, data, recipients):
        pass

    def _render_template(self, email_type, data):
        template = self.EMAIL_TEMPLATES[email_type]['template']

        # template render with context = {"data": data}
        return "rendered template by jinja2"

    def _prepare_request_data(self, data, email_type):
        subject = self.EMAIL_TEMPLATES[email_type]['subject']

        return {"subject": subject.format(**data), "data": data}

    async def send(self, recipients: list[str], data: dict, email_type: EmailTypes):
        template = self._render_template(email_type, data)
        prepeared_data = self._prepare_request_data(data, template)

        await self._make_request(prepeared_data, recipients)
