# EmailForge - construtor de emails html

Class _mail_constructor:

```
mail = _mail_constructor()

mail._mail_subject(subject = 'Exemplo')
mail._header(header_path = 'Header.jpg') # if your email has a header
mail._images(img_dir = 'public/images') # if your email has images
mail._mail_body(body_path = 'index.html')
mail._sendmail(to = [], host = smtp_host, port = smtp_port, smtp_user = user, smtp_pass = password, msg_from = 'exemplo_mail@motormac.com.br')

```
