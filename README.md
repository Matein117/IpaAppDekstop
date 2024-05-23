# IpaDesktop_v2
## 1: install an virtual enviroment
When you unzipp the folder you should to install a virtual enviroment
- open your terminal in your project 
- used this command in your terminal
  
   `python -m venv env`
  ![image](https://github.com/Matein117/IpaAppDekstop/assets/89878803/55b473f6-0db1-41c8-bca9-b22d217669ff)

- After that you will get an extra folder in your project where we are going to run and istall some libraries.
  ![image](https://github.com/Matein117/IpaAppDekstop/assets/89878803/9ab49d1e-8ce4-4d07-b0d8-b61fcf6c5a01)


- after have our "env folder" lest start our virtual enviroment with the next command line:
   - to activate env: `env\Scripts\activate.bat`
   - to deactivate env: `env\Scripts\deactivate.bat`
  ![image](https://github.com/Matein117/IpaAppDekstop/assets/89878803/0084c7d5-c76a-4a07-8113-d7b945cdbbb5)

- As you can see to know when you are enter in the env folder you should check the terminal some like indication this in your terminal:
![image](https://github.com/Matein117/IpaAppDekstop/assets/89878803/f243ac42-8408-4c51-ad2c-2ee10afd8798)

## 2: install libraries:
- `python -m pip install --upgrade pip` : this is for update or upgrade the version in case is not installed 
- `pip install autopep8` : It is a tool that automatically formats Python code 
- `pip install requests` : this is for a projects to send HTTP requests to web servers and retrieve data or most know fetch the data from an URL. 
> [!NOTE] . to used the library "requests" you should have a Database mysql and dowloand a local host like XAMPP and some Script in PHP 
> - To dowload the DB check my other repository: [Links](https://github.com/Matein117/IPA_DB)
> - To dowload the PHP scripts check my other repository: [Links](https://github.com/Matein117/IPA_connection_db)
> - To how to download and istall XAMPP check this tutorial: [Links](https://www.youtube.com/watch?v=G2VEf-8nepc)
- After you followed the command line we have to make sure if it were installed properly `pip list` this command show all the libraries in your folder "env":
  ![image](https://github.com/Matein117/IpaAppDekstop/assets/89878803/9111907c-fb42-4b48-9716-9aba515ef89f)
- you have two option to run the project:
  - run this command in the terminal `python -m app`
  - or click this button with the symbol play on your right side on the top in your file "app.py": ![image](https://github.com/Matein117/IpaAppDekstop/assets/89878803/a6775d35-d1e1-4270-ab24-cb75951e88d7)
 
  ![image](https://github.com/Matein117/IpaAppDekstop/assets/89878803/1fcde1b6-4cd1-47d5-8782-efd93347bd59)

 






