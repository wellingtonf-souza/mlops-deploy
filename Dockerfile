FROM python:3.7-slim
# ARG permite a definicao de uma variavel durante a criacao do docker 
# auxiliando a nao deixar usuario e senha explicitos no codigo
ARG USERNAME_CREATE_ARG
ARG PASSWORD_CREATE_ARG

ENV BASIC_AUTH_USERNAME=$USERNAME_CREATE_ARG
ENV BASIC_AUTH_PASSWORD=$PASSWORD_CREATE_ARG

# copiando o arquivo requirements para a pasta usr
COPY ./requirements.txt /usr/requirements.txt

# definindo o diretorio usr, igual a um cd usr/
WORKDIR /usr

RUN pip3 install -r requirements.txt

COPY ./src /usr/src
COPY ./models /usr/models

ENTRYPOINT [ "python3" ]
CMD [ "src/api/main.py" ]