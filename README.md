# Personal Finance Management


Welcome to the **Personal Finance Management**! This project aims to provide a powerful API for managing personal finances and tracking financial transactions.


## Project Goals

- Financial Management: The application provides users with an effective way to manage their finances. They can track income, expenses, investments and other financial transactions in one place.

- Budgeting: Users can create budgets and spending plans to better understand where their money is going and how to improve their financial situation.

- Security: The application provides secure storage and transmission of confidential information.

- Long-term Benefit: "Personal Finance Management" helps strengthen financial stability and long-term financial independence of users.

## Technologies used

- ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) Django: Powerful Python web framework.
- ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) Django REST Framework: A library for building APIs based on Django.
- ![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white) Swagger: A tool for creating interactive API documentation.

---

## Features

1) User Authentication: Secure user registration, login and authentication to protect financial data.

2) Transaction management: the ability to add, edit and classify financial transactions, including income, expenses.

3) Budget Tracking: Create, manage and track budgets to control expenses and achieve financial goals.

4) Expense categories. Organize transactions by categories for better financial analysis.

5) Income Tracking: The ability to record and track various sources of income, including salary and investments.

6) Multiple currencies: Support for multiple currencies for international users.

## License

[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE)

---

## How to start
1) Clone the repository: 
```
git clone [https://github.com/burkhonov007/personal-finance-managment](https://github.com/burhonov007/personal-finance-managment.git)
```
2) Create a virtual environment: 
```
python -m venv .venv
```
3) Activate the virtual environment: 
```
source .venv/bin/activate
```
4) Install dependencies: 
```
pip install -r requirements.txt
```
5) Run make migrations: 
```
python manage.py makemigrations
```
6) Run migrate: 
```
python manage.py migrate
```
6) Load fixtures:
```
python manage.py load_categories
python manage.py load_currencies
python manage.py load_users
python manage.py load_wallets
python manage.py load_transactions
```
7) Run the development server: 
```
python manage.py runserver
```
Open admin panel [localhost:8000/admin](http://localhost:8000/admin)

Default admin: admin@example.com

Default password: admin

Open Swagger API documentation [localhost:8000/api/v1/swagger-ui/](http://localhost:8000/api/v1/swagger-ui/)


