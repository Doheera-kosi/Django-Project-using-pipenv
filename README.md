# Django-Project-using-pipenv

>In this project, I had the opportunity to dive into the world of Django development using Pipenv. Throughout the journey, I gained valuable insights and hands-on experience in creating a Django project from scratch. From setting up a virtual environment to running the Django server, every step contributed to my understanding of this powerful web framework. Join me as I explore the wonders of Django and unleash the potential of Pipenv for seamless development. Get ready to embark on a coding adventure filled with creativity, efficiency, and endless possibilities!


## Django Project Setup Guide

This guide will help you set up a Django project using Python, Visual Studio Code, and Pipenv. Follow the steps below to get started:

## Prerequisites

Make sure you have the following installed:

- Python (latest version)
- Visual Studio Code
- Pipenv

## Project Setup

1. Create a new directory for your project. Let's name it "LittleLemon".

2. Open your terminal and navigate to the project directory using the `cd` command.

3. Install Django in a virtual environment using Pipenv:
   ```
   pipenv install django
   ```

4. Wait for Pipenv to set up Django and create the virtual environment.

5. Activate the virtual environment by running the command:
   ```
   pipenv shell
   ```

6. Your terminal session is now within the virtual environment. You can proceed with Django project setup.

7. Use Django admin to create a new project in the current directory:
   ```
   django-admin startproject LittleLemon .
   ```

8. Your Django project is now set up. Navigate to the project directory in the terminal.

9. To create a new Django web app for your APA project, run the following command:
   ```
   python manage.py startapp LittleLemonAPI
   ```

## Running the Django Server

1. Start the Django development server:
   ```
   python manage.py runserver
   ```

2. By default, the server runs on port 8000. You can access it at http://127.0.0.1:8000/.

3. If you want to run the server on a different port, specify it in the command:
   ```
   python manage.py runserver <port_number>
   ```

## Using Virtual Environment in Visual Studio Code

1. Open Visual Studio Code and open your project directory.

2. Access the command palette by clicking on "View" and selecting "Command Palette" or using the shortcut (Command+Shift+P).

3. In the command palette, select "Python: Select Interpreter" and choose the interpreter created by Pipenv for your project.

4. This step is crucial for using the virtual environment correctly. Ensure you select the interpreter with the name of your project directory.

5. Open the integrated terminal in Visual Studio Code by selecting "Terminal" from the menu.

6. The terminal will automatically activate the virtual environment created by Pipenv for your project.

7. You can now run all the commands, such as `python manage.py runserver`, directly in the terminal without any issues.

8. If needed, you can open multiple terminal sessions by clicking the plus icon and switch between them within the terminal tab.

Congratulations! You have successfully set up your Django project using Pipenv and Visual Studio Code. You are now ready to start developing APIs with Django. Enjoy your coding journey!