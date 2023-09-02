from django.core.management.base import BaseCommand
from transaction.models import Category
import random

class Command(BaseCommand):
    help = 'Заполняет базу данных категориями'

    def handle(self, *args, **options):
        parent_income = Category.objects.create(name="Приход")
        parent_expense = Category.objects.create(name="Расход")

        income_categories = [
            "Зарплата",
            "Инвестиции",
            "Партнерские программы",
            "Аренда недвижимости",
            "Продажи",
            "Подарки",
            "Страхование",
            "Дивиденды",
            "Пенсия",
            "Авторские права",
            "Продажа ненужных вещей",
            "Подработки",
            "Сдача в аренду",
            "Онлайн-курсы",
            "Фриланс",
            "Краудфандинг",
            "Вклады",
            "Рентный доход",
            "Премии",
            "Гонорары",
        ]

        expense_categories = [
            "Аренда",
            "Еда",
            "Транспорт",
            "Одежда",
            "Здоровье",
            "Развлечения",
            "Путешествия",
            "Образование",
            "Коммунальные платежи",
            "Техника",
            "Автомобиль",
            "Ремонт",
            "Красота",
            "Подарки",
            "Спорт",
            "Рестораны",
            "Кафе",
            "Сотовая связь",
            "Дети",
            "Домашние животные",
        ]

        for category_name in income_categories:
            Category.objects.create(name=category_name, parent_category=parent_income)

        for category_name in expense_categories:
            Category.objects.create(name=category_name, parent_category=parent_expense)

        self.stdout.write(self.style.SUCCESS('Категории успешно созданы'))    