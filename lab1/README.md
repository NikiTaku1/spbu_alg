2 Вариант (Платная поликлиника)

A. Сгенерировать датасет в котором будут следующие наборы свойств:

1. ФИО - Иванов Иван Иванович
2. Паспортные данные - 1234 123456
3. СНИЛС - 123-456-789 12
4. Симптомы - боль в горле
5. Выбор врача - лор6. Дата посещения врача- 2020-01-22T08:30+03:00
7. Анализы - мазок на ковид
8. Дата получения анализов - 2020-01-24T09:30+03:00
9. Стоимость анализов - 2000 руб.
10. Карта оплаты - “1234 5678 1234 5678”

B. Дополнительная информация по каждому свойству:

1. ФИО - словарь по ФИО.
2. Паспортные данные - уникальные значения
3. СНИЛС - уникальные значения
4. Симптомы - ”Словарь” по возможным симптомам
5. Выбор врача - ”Словарь” по возможным специальностям которые могутработать в поликлинике
6. Дата посещения врача- определенный вариант генерации данных.
7. Анализы - ”Словарь” по возможным анализам
8. Дата получения анализов - после посещения врача
9. Стоимость анализов - свободный вариант генерации данных.
10. Карта оплаты - возможность настраивать датасет и вероятность какогобанка (Сбербанк и тд), через какую платежную систему (Visa и тд)производится оплата. Оплачивать могут несколько раз с одной карты.

C. Ограничения датасета:

1. Всего строк в датасете - минимум 50 000.
2. ФИО - словарь должен состоять только из славянских ФИО
3. Паспортные данные - только русские, белорусские и казахскиепаспорта должны быть.
4. СНИЛС - уникальный, но привязан к клиенту (ФИО и паспортныеданные), которые могут повторяться при повторном посещение.
5. Симптомы - ”Словарь” должен состоять минимум из 5000 симптомов.То есть можем быть комбинация итоговых симптомов (не более 10штук)
6. Выбор врача - ”Словарь” должен состоять минимум из 50 врачей.
7. Дата посещения врача - В рабочие время и дни недели. Повторноепосещение может быть к врачу минимально через 24 часа послеполучения анализов.
8. Анализы - ”Словарь” должен состоять минимум из 250 анализов. Тоесть можем быть комбинация итоговых симптомов (не более 5 штук)
9. Дата получения анализов - В рабочие время и дни (через 24-72 часа).
10. Стоимость анализов - только в рублях.11. Карта оплаты - максимальное количество повторов - 5 раз
