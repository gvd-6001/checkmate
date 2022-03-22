import email
import imaplib
import re

from celery import shared_task

from .models import HikNvrAlert


@shared_task(bind=True)
def fetch_post_data(self):
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    (retcode, capabilities) = mail.login('bhawnademo@gmail.com', 'Hello@0542')
    mail.list()
    mail.select('inbox')
    nvr_name = []
    event_name = []
    n = 0
    (retcode, messages) = mail.search(None, '(UNSEEN)')
    if retcode == 'OK':
        for num in messages[0].split():
            print('Processing ')
            n = n + 1
            typ, data = mail.fetch(num, '(RFC822)')
            for response_part in data:
                if isinstance(response_part, tuple):
                    original = email.message_from_bytes(response_part[1])
                    print(original['Subject'])
                    raw_email = data[0][1]
                    raw_email_string = raw_email.decode('utf-8')
                    email_message = email.message_from_string(raw_email_string)
                    for part in email_message.walk():
                        if part.get_content_type() == "text/plain":
                            body = part.get_payload(decode=True)
                            nvr_name = original['Subject'][:4]
                            print(nvr_name)
                            event_type = original['Subject'][5:]
                            print(event_type)
                            body_data = body.decode('utf-8')
                            pattern = re.search(r'NVR S/N:', body_data)
                            if pattern:
                                print("Data is found")
                                ind_of_dvr = pattern.span()[1]
                                last_index = pattern.endpos
                                value_extract = body_data[ind_of_dvr:last_index].strip(
                                )
                                print(value_extract)
                                dt = [nvr_name, event_type, value_extract]
                                HikNvrAlert.objects.create(nvrAlert=dt)
                        else:
                            continue

                    typ, data = mail.store(num, '+FLAGS', '\\Seen')
                    print(n)

    return "Done"
