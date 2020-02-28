
<img src="https://user-images.githubusercontent.com/18649504/66263084-9c64c700-e7c3-11e9-86dd-253fcd1c7292.png" width = "400">

## 🤖 EXPA Bot

<img src="https://user-images.githubusercontent.com/18649504/66263309-f87d1a80-e7c6-11e9-8162-8e9c4c066b33.png" width = "600">


## 📚  Description

   EXPA Bot was created to get information from <b>EXPA System</b> through an <b>API GraphQL</b> and to save on <b>PostgreSQL's Database</b> where International AIESEC give us a specific <b>TOKEN</b> to access that.<br>
    Then the bot use start date and end date of event to get information about approved,accepted,realized and applications of Exchange Participant from AIESEC. If bot to take any information that already there is on our database, it will <b>update</b> the information else it will <b>insert</b> new information.<br>

## 📊 Dashboards 

With all information that I've been collected,  I've done 2 dashboards for AIESEC to follow their KPI (Key Performance Indicator) and MOS(measures of success).<br>
OGX - Outgoing Exchange - http://bit.ly/apdsogxv1<br>
ICX - Incoming Exchange - http://bit.ly/apdsicxv1<br>

## 🚀 Technologies have used 

<img src="https://user-images.githubusercontent.com/18649504/66262823-725cd600-e7be-11e9-9cea-ea14305079db.png" width = "100">
<img src="https://user-images.githubusercontent.com/18649504/66262824-74bf3000-e7be-11e9-9485-45eac5577165.png" width = "100">
<img src ="https://user-images.githubusercontent.com/18649504/66262910-11ce9880-e7c0-11e9-870e-9f9809cdd193.png" width = "100">
<img src ="https://user-images.githubusercontent.com/18649504/66262944-91f4fe00-e7c0-11e9-979d-2f370d1ebbbc.png" width = "100">

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

## 🌏 Hosting

   Expa bot has been hosted on AWS Server by AIESEC in Brazil<br>

## 📢 How to use

Required:

Token AIESEC<br>
Python 3.7.5 or more<br>
Node 10x<br>
PostgreSQL's Database or other( But you will need change a lib to use your data base)<br>

Tips about Linux's Environment:<br>
Before everything you need to rum this command:
```bash 
sudo apt update
```
Install Python 3:
```bash 
sudo apt-get install python3
```
Install pip 3:
```bash 
sudo apt-get install python3-pip
```
Install Node:
```bash 
sudo apt install nodejs
```
Install npm:
```bash 
sudo apt install npm
```
Create specific tables in your database,executing script below:
```bash 
script_bd.sql
```
Install all python's dependencies with script below:  

```bash 
pip install  -r requiriments.txt
pip3 install  -r requiriments.txt(linux)
 ```  
Install lib "pm2" on your node.js with NPM:

```bash 
npm install -g pm2
```
After every installations you can execute the bot,at directory's project with console CMD:  
```bash 
pm2  start  _get_accepted_.py
pm2  start  _get_applications_.py
pm2  start   _get_approved_.py
pm2  start    _get_realized_.py
```
if your linux has other versions installed, you need to use:  
```bash 
pm2  start  _get_accepted_.py --interpreter python3
pm2  start  _get_applications_.py --interpreter python3
pm2  start   _get_approved_.py --interpreter python3
pm2  start    _get_realized_.py --interpreter python3
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
There are many commands on PM2 you can see at all in its documentation https://www.npmjs.com/package/pm2.

## 🔓 Licença 
MIT © [Paulo Mota](https://www.linkedin.com/in/paulo-mota-955218a2/)
