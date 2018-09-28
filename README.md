# Prettify JSON

Скрипт, который на вход принимает путь до файла с произвольными данными в формате JSON и выводит его содержимое в консоль в удобном для чтения виде: добавляет переносы строк, отступы слева и пробелы.

# Quickstart

Example of script launch on Linux, Python 3.5:

```bash

$ python pprint_json.py bars.json

[
    {
        "Cells": {
            "Address": "улица Академика Павлова, дом 10",
            "AdmArea": "Западный административный округ",
            "ClarificationOfWorkingHours": null,
            "District": "район Кунцево",
            "IsNetObject": "да",
            "Name": "Ароматный Мир",
            "OperatingCompany": "Ароматный Мир",
            "PublicPhone": [
                {
                    "PublicPhone": "(495) 777-51-95"
                }
            ],
            "TypeService": "реализация продовольственных товаров",
            "WorkingHours": [
                {
                    "DayOfWeek": "понедельник",
                    "Hours": "09:30-22:30"
                },
                {
                    "DayOfWeek": "вторник",
                    "Hours": "09:30-22:30"
                },
                {
                    "DayOfWeek": "среда",
                    "Hours": "09:30-22:30"
                },
                {
                    "DayOfWeek": "четверг",
                    "Hours": "09:30-22:30"
                },
                {
                    "DayOfWeek": "пятница",
                    "Hours": "09:30-22:30"
                },
                {
                    "DayOfWeek": "суббота",
                    "Hours": "09:30-22:30"
                },
                {
                    "DayOfWeek": "воскресенье",
                    "Hours": "09:30-22:30"
                }
            ],
            "geoData": {
                "coordinates": [
                    37.39703804817934,
                    55.740999719549094
                ],
                "type": "Point"
            },
            "global_id": 14371450
        },
        "Id": "79742784-9ef3-4543-bc98-a219a8903c18",
        "Number": 1
    },
    {
        "Cells": {
            "Address": "улица Лескова, дом 6",
            "AdmArea": "Северо-Восточный административный округ",
            "ClarificationOfWorkingHours": null,
            "District": "район Бибирево",
            "IsNetObject": "да",
            "Name": "Массандра в Алтуфьево",
            "OperatingCompany": "Массандра",
            "PublicPhone": [
                {
                    "PublicPhone": "(499) 909-40-08"
                }
            ],
            "TypeService": "реализация продовольственных товаров",
            "WorkingHours": [
                {
                    "DayOfWeek": "понедельник",
                    "Hours": "10:00-22:00"
                },
                {
                    "DayOfWeek": "вторник",
                    "Hours": "10:00-22:00"
                },
                {
                    "DayOfWeek": "среда",
                    "Hours": "10:00-22:00"
                },
                {
                    "DayOfWeek": "четверг",
                    "Hours": "10:00-22:00"
                },
                {
                    "DayOfWeek": "пятница",
                    "Hours": "10:00-22:00"
                },
                {
                    "DayOfWeek": "суббота",
                    "Hours": "10:00-22:00"
                },
                {
                    "DayOfWeek": "воскресенье",
                    "Hours": "10:00-22:00"
                }
            ],
            "geoData": {
                "coordinates": [
                    37.59317706430676,
                    55.89772236936797
                ],
                "type": "Point"
            },
            "global_id": 14934782
        },
        "Id": "1bd07c21-05de-4015-b015-d22657168ded",
        "Number": 2
    },
    {
        "Cells": {
            "Address": "Алтуфьевское шоссе, дом 72",
            "AdmArea": "Северо-Восточный административный округ",
            "ClarificationOfWorkingHours": null,
            "District": "район Бибирево",
            "IsNetObject": "нет",
            "Name": "Соната-М",
            "OperatingCompany": null,
            "PublicPhone": [
                {
                    "PublicPhone": "(905) 791-87-13"
                }
            ],
            "TypeService": "реализация продовольственных товаров",
            "WorkingHours": [
                {
                    "DayOfWeek": "понедельник",
                    "Hours": "09:00-22:00"
                },
                {
                    "DayOfWeek": "вторник",
                    "Hours": "09:00-22:00"
                },
                {
                    "DayOfWeek": "среда",
                    "Hours": "09:00-22:00"
                },
                {
                    "DayOfWeek": "четверг",
                    "Hours": "09:00-22:00"
                },
                {
                    "DayOfWeek": "пятница",
                    "Hours": "09:00-22:00"
                },
                {
                    "DayOfWeek": "суббота",
                    "Hours": "09:00-22:00"
                },
                {
                    "DayOfWeek": "воскресенье",
                    "Hours": "09:00-22:00"
                }
            ],
            "geoData": {
                "coordinates": [
                    37.58803599964753,
                    55.89020100016689
                ],
                "type": "Point"
            },
            "global_id": 14937274
        },
        "Id": "a16c8154-09d8-4207-8e13-cb8db654e95c",
        "Number": 3
    }
]

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
