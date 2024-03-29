import email
import imaplib

from resources import mail_config


class MailUtils:
    @staticmethod
    def delete_all_emails(mail_model):
        with imaplib.IMAP4_SSL(mail_config.host, mail_config.port) as mail:
            mail.login(mail_model.login, mail_model.password)
            mail.select("Inbox")
            typ, data = mail.search(None, 'ALL')
            mail_ids = data[0]
            id_list = mail_ids.split()
            for num in id_list:
                mail.store(num, '+FLAGS', '\\Deleted')
            mail.expunge()

    @staticmethod
    def get_first_message(mail_model):
        with imaplib.IMAP4_SSL(mail_config.host, mail_config.port) as mail:
            mail.login(mail_model.login, mail_model.password)
            mail.select("Inbox")
            typ, data = mail.search(None, 'ALL')
            mail_ids = data[0]
            id_list = mail_ids.split()
            if len(id_list) > 0:
                result, data = mail.fetch(id_list[0], "(RFC822)")
                raw_email = data[0][1]
                raw_email_string = raw_email.decode('utf-8')
                email_message = email.message_from_string(raw_email_string)
                return MailUtils.get_text_block(email_message)
            else:
                raise RuntimeError("There is no emails in box")

    @staticmethod
    def get_text_block(email_message_instance):
        maintype = email_message_instance.get_content_maintype()
        if maintype == 'multipart':
            for part in email_message_instance.get_payload():
                if part.get_content_maintype() == 'text':
                    return part.get_payload(decode=True)
        elif maintype == 'text':
            return email_message_instance.get_payload()

    @staticmethod
    def is_mail_sent(mail_model):
        try:
            MailUtils.get_first_message(mail_model)
            return True
        except RuntimeError:
            return False
