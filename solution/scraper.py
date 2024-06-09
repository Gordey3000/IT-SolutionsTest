import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "solution.settings")
django.setup()

from ads.models import Advertisement

'''
Скрипт заполняет базу данных sqlite3 данными 12 объявлений для проверки пагинации.
'''


def scrape_and_save(titles, ad_ids, authors, views):
    for i, (title, ad_id, author, view) in enumerate(zip(titles,
                                                         ad_ids,
                                                         authors,
                                                         views), 1):
        Advertisement.objects.create(title=title, ad_id=ad_id,
                                     author=author, views=view, position=i)
    print("Данные успешно загружены.")


if __name__ == "__main__":
    titles = ["Заголовок 1", "Заголовок 2", "Заголовок 3", "Заголовок 4",
              "Заголовок 5", "Заголовок 6", "Заголовок 7", "Заголовок 8",
              "Заголовок 9", "Заголовок 10", "Заголовок 11", "Заголовок 12"]
    ad_ids = ["id1", "id2", "id3", "id4", "id5", "id6",
              "id7", "id8", "id9", "id10", "id11", "id12"]
    authors = ["Автор 1", "Автор 2", "Автор 3", "Автор 4",
               "Автор 5", "Автор 6", "Автор 7", "Автор 8",
               "Автор 9", "Автор 10", "Автор 11", "Автор 12"]
    views = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]

    scrape_and_save(titles, ad_ids, authors, views)
