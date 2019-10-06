
![1_7g5hEDbnq7GbpUwPnd02qQ](https://user-images.githubusercontent.com/18649504/66263084-9c64c700-e7c3-11e9-86dd-253fcd1c7292.png)

## 🤖 Robô EXPA

![Robô](https://user-images.githubusercontent.com/18649504/66263309-f87d1a80-e7c6-11e9-8162-8e9c4c066b33.png)


## 📚  Descrição 

Robô desenvolvido para criar uma base de dados para AIESEC do Brasil com as informações do sistema internacional EXPA , que disponibiliza uma API GraphQL para consumo dos dados.<br>
Então o robô basicamente pega os dados pelo um range de data (inicio e fim) e verifique se houve  aprovados ,aceitos ,realizações e aplicações de intercâmbistas no EXPA , se houve, o robo atualiza ou insere os dados <br>

<br><br>
## 🚀 Tecnologias Usadas 

<img src="https://user-images.githubusercontent.com/18649504/66262823-725cd600-e7be-11e9-9cea-ea14305079db.png" width = "100">
<img src="https://user-images.githubusercontent.com/18649504/66262824-74bf3000-e7be-11e9-9485-45eac5577165.png" width = "100">
<img src ="https://user-images.githubusercontent.com/18649504/66262910-11ce9880-e7c0-11e9-870e-9f9809cdd193.png" width = "100">
<img src ="https://user-images.githubusercontent.com/18649504/66262944-91f4fe00-e7c0-11e9-979d-2f370d1ebbbc.png" width = "100">

<br><br>
## Estrutura do Projeto 📌
    |-- api
         |--graphqlconsume.py
         |--querygraphql.py
    |-- controller
         |--RobotRotine.py
    |-- database
         |--conexao.py
    |-- _get_accepted_.py
    |-- _get_applications_.py
    |-- _get_approved.py
    |-- _get_realized.py

<br><br>
## 🌏 Hospedagem 

  Hospedado em um servidor AWS disponibilizado pela AIESEC do Brazil <br>

<br><br>
## 📢 Como executar

Requisitos:
Python 3.6
Instalar todas as depedências do python usando o arquivo requiriments.txt que está no projeto:  

```bash 
pip install  -r requiriments.txt
 ```  
Instalar o pm2 do nodejs

```bash 
npm install -g pm2
```
Após a instalação para executar os robôs, só precisa abrir o cmd/Terminal  apontando para o diretorio do projeto e fazer os comandos  
```bash 
pm2  start  _get_accepted_.py
pm2  start  _get_applications_.py
pm2  start   _get_approved_.py
pm2  start    _get_realized_.py
```
![image](https://user-images.githubusercontent.com/18649504/66263916-a2fa3b00-e7d1-11e9-902b-07ccce624de3.png)

Para listar o status dos robôs:
```bash 
pm2  list
```
Para para a execução de algum dos robôs:
```bash 
pm2  stop _get_realized_.py
```
Para para ver os logs de algum dos robôs:
```bash 
pm2  logs _get_realized_.py
```
Tem varios comandos que o pm2 pode oferecer e você pode ver na documentação.

## 🔓 Licença 
MIT © [Paulo Mota](https://www.linkedin.com/in/paulo-mota-955218a2/)
