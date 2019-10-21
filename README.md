
![1_7g5hEDbnq7GbpUwPnd02qQ](https://user-images.githubusercontent.com/18649504/66263084-9c64c700-e7c3-11e9-86dd-253fcd1c7292.png)

## 🤖 EXPA Bot

![Robô](https://user-images.githubusercontent.com/18649504/66263309-f87d1a80-e7c6-11e9-8162-8e9c4c066b33.png)


## 📚  Description

EXPA Bot was created to get information from EXPA System through an API GraphQL and to save on Postgre's Data Base where International Aiesec give us a specific token to access.<br>
Então o robô basicamente pega os dados pelo um range de data (inicio e fim) e verifique se houve  aprovados ,aceitos ,realizações e aplicações de intercâmbistas no EXPA , se houve, o robo atualiza ou insere os dados <br>
Then the bot use start date and end date of event to get information about apporved,accepted,realized and applications of Exchange Participant from AIESEC. If bot to take any information that already there is on our database, it will update the information else it insert new information.<br>


<br><br>
## 🚀 Tecnologies have used 

<img src="https://user-images.githubusercontent.com/18649504/66262823-725cd600-e7be-11e9-9cea-ea14305079db.png" width = "100">
<img src="https://user-images.githubusercontent.com/18649504/66262824-74bf3000-e7be-11e9-9485-45eac5577165.png" width = "100">
<img src ="https://user-images.githubusercontent.com/18649504/66262910-11ce9880-e7c0-11e9-870e-9f9809cdd193.png" width = "100">
<img src ="https://user-images.githubusercontent.com/18649504/66262944-91f4fe00-e7c0-11e9-979d-2f370d1ebbbc.png" width = "100">

<br><br>
## Structure's Project 📌
    |-- api
         |--graphqlconsume.py
         |--querygraphql.py
    |-- controller
         |--RobotRotine.py
    |-- database
         |--conexao.py
    |-- _get_accepted_.py
    |-- _get_applications_.py
    |-- _get_approved_.py
    |-- _get_realized_.py

<br><br>
## 🌏 Hosting

   Expa bot has been hosted on AWS Server by AIESEC in Brazil<br>

<br><br>
## 📢 How to use

Required:

Python 3.6<br>
Node 10x<br>
PostgreSQL or other( But you will need change libs to your data base)<br>

Criar as tabelas em seu banco de dados com o script:
Create specific tables in your database,executing script below:
```bash 
script_bd.sql
```
Install all python's dependences with script below:  

```bash 
pip install  -r requiriments.txt
 ```  
Install lib "pm2" on your node.js with NPM:

```bash 
npm install -g pm2
```
After every instalations you can execute the bot,at directory's project with console CMD:  
```bash 
pm2  start  _get_accepted_.py
pm2  start  _get_applications_.py
pm2  start   _get_approved_.py
pm2  start    _get_realized_.py
```
![image](https://user-images.githubusercontent.com/18649504/66263916-a2fa3b00-e7d1-11e9-902b-07ccce624de3.png)

#TIPS PM2#

List all bots:
```bash 
pm2  list
```
Stop a bot:
```bash 
pm2  stop _get_realized_.py
```
Show bot's log:
```bash 
pm2  logs _get_realized_.py
```
There are many comands on PM2 you can see at all in its documentation https://www.npmjs.com/package/pm2.

## 🔓 Licença 
MIT © [Paulo Mota](https://www.linkedin.com/in/paulo-mota-955218a2/)
