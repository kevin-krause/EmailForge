# EmailForge - construtor de emails html

Class _mail_constructor:

```
mail = _mail_constructor()

mail._mail_subject(subject = 'Exemplo)
mail._header(header_path = 'Header.jpg') # if your email has a header
mail._images(img_dir = 'public/images') # if your email has images
mail._mail_body(body_path = 'index.html')
mail._sendmail(to = [], host = smtp_host, port = smtp_port, smtp_user = user, smtp_pass = password, msg_from = 'exemplo_mail@motormac.com.br')

```

Para a func _images:

faz um loop dentro do diretório das imagens criando uma cid pra cada arquivo dentro da pasta, substituindo ' ' por '_' e retirando a extenção da imagem.

ex: img 1.png >> cid:img_1
