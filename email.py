import os
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import smtplib


class _mail_constructor():

    msg = MIMEMultipart('alternative')

    def _mail_subject(self, subject: str):
        self.msg['Subject'] = f'{subject}'

    def _header(self, header_path: str) -> None:

        with open(fr'{header_path}', 'rb') as header:

            mimeh = MIMEBase(
                'image', 'png', filename='Header.png')
            mimeh.add_header('Content-Disposition',
                             'attachment', filename='img1.png')
            mimeh.add_header('X-Attachment-Id', 'header')
            mimeh.add_header('Content-ID', '<header>')
            mimeh.set_payload(header.read())
            encoders.encode_base64(mimeh)

            self.msg.attach(mimeh)

    def _images(self, img_dir: list) -> None:

        img_list = []
        img_list.append([i.replace(' ', '_') for i in os.listdir(img_dir)])
        img_list = img_list[0]

        if not img_list:
            pass
        else:
            for path in os.listdir(img_dir):
                with open((img_dir + '\\' + path), 'rb') as img_file:
                    img = MIMEBase('image', 'png', filename=f'{path}')
                    img.add_header('Content-Disposition',
                                   'attachment', filename=f'{path}')

                    path = os.path.basename(path).replace(
                        ' ', '_').replace('.png', '')

                    img.add_header('X-Attachment-Id', f'<{path}>')
                    img.add_header('Content-ID', f'<{path}>')
                    img.set_payload(img_file.read())
                    encoders.encode_base64(img)
                    self.msg.attach(img)

        return self.msg

    def _mail_body(self, body_path: str):
        body = MIMEText(open(body_path).read(), 'html')
        self.msg.attach(body)

    def _sendmail(self, to: list, host: str, port: int, smtp_user: str, smtp_pass: str, msg_from: str):

        self.msg['To'] = ','.join(to)

        smtp = smtplib.SMTP(host, port)
        smtp.starttls()
        smtp.login(smtp_user, smtp_pass)
        smtp.ehlo()
        smtp.sendmail(msg_from, to, self.msg.as_string())
        smtp.quit()
