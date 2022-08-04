# Docker-Flask-uWSGI

Container de docker com uWSGI para aplicações de Flask em Python 3.8

## Descrição
Esta imagem de Docker é um exemplo de como criar uma aplicação web de Flask em Python 3.8 que tenha uWSGI.

É um exemplo de como criar seu próprio container e escalar os processos com o arquivo ini de uWSGI.

Repositório do git que serviu de referência: https://github.com/cirolini/Docker-Flask-uWSGI

## QuickStart

Faça o build de sua própria imagem de docker, executando no terminal: 

```
docker build -t flask-uwsgi:latest .
```

Então você pode executar o container de docker executando o seguinte comando no terminal:

OBS.: Dá para mudar a porta 5000 para qualquer outra disponível. 

```
docker run -p 5000:5007 flask-uwsgi:latest
```

E teste a aplicação com o comando curl:

```
curl -v "http://localhost:5000/"
``` 

O arquivo k8s_app.yaml pode servir de modelo em deploy da aplicação em kubernetes. 
