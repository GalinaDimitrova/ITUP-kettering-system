# Вътрешна кетъринг система
Проект на тема "Вътрешна кетъринг система" е предложена от ТехноЛогика ЕАД по курса Методи за анализ и проектиране, летен семестър 2017/2018, спец. ИТУП.

Идеята на това repo за момента е да съдържа базов скелет на бъдещата система.

## Base requirements:
    python 2.7.10
    pip 7.0.1

## Project setup and run:
    1. Clone the repo
    2. It is recommended to create a virtualenv, where to install the project requirements. To do that:
        - Check if the virtualenv is installed:
        ```
        virtualenv --version
        ```
        - Navigate to directory where the new env will be created (for example one dir above <cloned project dir>)
        - Create a virtualenv:
        ```
        virtualenv <the name of the new env>
        ```
        - activate the environment:
        ```
        source <the name of the new env>/bin/activate
        (for Windows user: source <the name of the new env>/Scripts/activate)
        ```

    3. Navigate to the directory with manage.py and requirements.txt files
    4. Install the requirements:
    ```
    pip install requirements.txt
    ```
    5. Run the migrations in order to create the local SQL db:
    ```
    python manage.py migrate
    ```
    6. Run the server locally:
    ```
    python manage.py runserver 127.0.0.1:<port>

    (With debugger: python -m pdb manage.py runserver <ip>:<port>)
    ```

## Other info:
    - After running the server, the admin panel is accessible on <ip>:<port>/admin.

    - The SQL db can be opened and modified with http://www.sqliteexpert.com/
