import datetime
import re
import pandas
def maskerization_passport(passport: str) -> str:
    return passport[:2] + re.sub(r"\d", "*", passport[2:])


def generalization_doctor(doctor: str) -> str:
    doctor_types = [
        [
            "Психиатр",
            "Гастроэнтеролог",
            "Невролог",
            "Дерматолог",
            "Офтальмолог",
            "Уролог",
            "Онколог",
            "Лор",
            "Физиотерапевт",
            "Кардиолог",
        ],
        [
            "Травматолог",
            "Аллерголог",
            "Стоматолог",
            "Эндокринолог",
            "Пульмонолог",
            "Гематолог",
            "Неонатолог",
            "Гериатр",
            "Эндоскопист",
            "Онкоуролог",
        ],
        [
            "Иммунолог",
            "Гепатолог",
            "Гастроэнтеролог-морфолог",
            "Онкогинеколог",
            "Нефролог",
            "Эндоскопист-лапароскопиолог",
            "Генетик",
            "Педиатр",
            "Ревматолог",
            "Гастроэнтеролог-вирусолог",
        ],
        [
            "Онкодерматолог",
            "Невропатолог",
            "Кардиоревматолог",
            "Косметолог",
            "Диетолог",
            "Ортодонт",
            "Пульмонолог-тораколог",
            "Фтизиатр",
            "Неонатолог-патолог",
            "Ортопед",
        ],
        [
            "Оториноларинголог",
            "УЗИ-специалист",
            "Нефролог-гипертолог",
            "Гастроэнтеролог-этиолог",
            "Кардиолог-кардиохирург",
            "Офтальмолог-окулист",
            "Ревматолог-фармаколог",
            "Эндокринолог-диабетолог",
            "Психотерапевт",
            "Кардиоревматолог-гистолог",
        ],
    ]

    for i, t in enumerate(doctor_types):
        if doctor in t:
            return f"doctor_type_{i}"

def generalization_symptoms(symptom: str) -> str:
    symptom_types = [
        [
            "Депрессия",
            "Расстройство пищеварения",
            "Онемение конечностей",
            "Сыпь на коже",
            "Затуманенное зрение",
            "Частое мочеиспускание",
            "Потеря веса",
            "Нарушение слуха",
            "Ограничение подвижности суставов",
            "Повышенное давление",
        ],
        [
            "Переломы",
            "Кожные высыпания",
            "Кровоточивость десен",
            "Чрезмерная утомляемость",
            "Одышка",
            "Частые кровотечения",
            "Нарушение адаптации",
            "Проблемы с памятью",
            "Заболевания кишечника",
            "Опухоли мочевого пузыря",
        ],
        [
            "Частые простуды",
            "Желтуха",
            "Запоры",
            "Кровотечения",
            "Боли в пояснице",
            "Язвы желудка",
            "Семейный анамнез наследственных заболеваний",
            "Лихорадка",
            "Утренняя скованность",
            "Изжога",
        ],
        [
            "Злокачественные новообразования кожи",
            "Паралич",
            "Поражение сердца",
            "Акне и угревая сыпь",
            "Избыточный вес",
            "Глубокий прикус",
            "Бронхит",
            "Лихорадочное состояние",
            "Проблемы с пищеварением",
            "Боли в суставах",
        ],
        [
            "Нарушение зонтичного слуха",
            "Боли в брюшной полости",
            "Частые мочевые инфекции",
            "Рвота",
            "Аритмия",
            "Зуд",
            "Ревматоидный артрит",
            "Сахарный диабет",
            "Бессонница",
            "Поражение суставов",
        ],
    ]

    symptom = symptom.split("|")
    symptom1 = symptom[-1]

    for i, t in enumerate(symptom_types):
        if symptom1 in t:
            return f"symptom_type_{i}"
        
def generalization_analysis(analysis: str) -> str:
    analysis_types = [
        [
            "Клиническое интервью",
            "Уровень желудочной кислоты",
            "ЭЭГ (электроэнцефалография)",
            "Мазок на флору кожи",
            "Зрение на дальность",
            "УЗИ органов мочевыделительной системы",
            "Биопсия опухоли",
            "Ринофиброларингоскопия",
            "Электромиография",
            "ЭКГ (электрокардиограмма)",
        ],
        [
            "Рентген",
            "Анализ крови на А-антитела",
            "Клинический анализ крови",
            "Анализ крови на уровень глюкозы",
            "Спирометрия",
            "Анализ крови на свертываемость",
            "Анализ амниотической жидкости",
            "Тест на деменцию",
            "Эзофагогастродуоденоскопия",
            "Цистоскопия",
        ],
        [
            "Анализ антител в крови",
            "Анализ крови на билирубин",
            "Фиброколоноскопия",
            "Анализ крови на онкомаркеры",
            "Анализ мочи на белок и альбумин",
            "Эндоскопия верхних отделов ЖКТ",
            "Кариотипирование",
            "Мазок из носоглотки",
            "Анализ крови на антитела к суставам",
            "pH-метрия",
        ],
        [
            "Биопсия кожи",
            "Электромиографическое обследование",
            "Электрокардиография",
            "Дерматоскопия",
            "Анализ крови на уровень липидов",
            "Ортопантомограмма",
            "Спирограмма",
            "Микроскопия макроты",
            "Анализ мочи на наличие метаболитов",
            "Рентген суставов",
        ],
        [
            "Аудиометрия",
            "УЗИ внутренних органов",
            "Анализ мочи на бактерии",
            "Гастроэнтероскопия",
            "ЭКГ суточное мониторирование",
            "Офтальмоскопия",
            "Ревматоидный фактор в крови",
            "Анализ крови на уровни глюкозы",
            "Интервью на тревогу",
            "Анализ крови на антитела",
        ],
    ]

    analysis1 = analysis.split("|")[-1]

    for i, t in enumerate(analysis_types):
        if analysis1 in t:
            return f"analysis_type_{i}"

def generalization_date_start(date_start: str) -> str:
    timestamp = datetime.datetime.strptime(date_start, "%Y-%m-%dT%H:%M+03:00")
    m = timestamp.month % 12
    if m <= 2:
        return "Winter"
    elif m <= 5:
        return "Spring"
    elif m <= 8:
        return "Summer"
    else:
        return "Autumn"


def aggregation_price(price: str) -> str:
    return str((int(price) // 2500) * 2500)


def generalization_card(card: str) -> str:
    code_to_bank = {
        "547948": "MC",
        "427680": "VISA",
        "220220": "MIR",
        "524468": "MC",
        "437772": "VISA",
        "220070": "MIR",
        "542104": "MC",
        "418868": "VISA",
        "220024": "MIR",
        "510126": "MC",
        "410584": "VISA",
        "220215": "MIR",
    }
    return code_to_bank[card.replace(" ", "")[:6]]

def anonimyze(df: pandas.DataFrame) -> pandas.DataFrame:
    df = df.drop("Name", axis=1)
    df["Passport"] = df["Passport"].apply(maskerization_passport)
    df = df.drop("Snils", axis=1)

    df["Doctor"] = df["Doctor"].apply(generalization_doctor)
    df["Symptoms"] = df["Symptoms"].apply(generalization_symptoms)
    df["Analysis"] = df["Analysis"].apply(generalization_analysis)

    df["DateStart"] = df["DateStart"].apply(generalization_date_start)
    df = df.drop("DateEnd", axis=1)

    df["Price"] = df["Price"].apply(aggregation_price)
    df["Card"] = df["Card"].apply(generalization_card)

    return df


def calc_k_anonymity(df: pandas.DataFrame, cols):
    k = 1
    if len(df) < 51000:
        k = 5
        #k = 10
    elif len(df) < 105000:
        k = 5
        #k = 7
    elif len(df) < 260000:
        k = 5

    values: pandas.DataFrame
    values = df.groupby(cols)
    values = values.size()
    values = values.reset_index(name="Count")

    bad_val = {"total": 0}
    k_anon = list()
    deleted = 0
    max_deletions = int(len(values) * 0.05)

    for _, v in values.iterrows():
        cnt = v["Count"]
        k_anon.append(cnt)
        if cnt == 1 and deleted < max_deletions:
            deleted += 1
            continue

        if cnt < k:
            cnt = str(cnt)
            if cnt not in bad_val:
                bad_val[cnt] = 0
            bad_val[cnt] += 1
            bad_val["total"] += 1

    to_delete = values[values["Count"] == 1].index.tolist()
    to_delete = to_delete[:max_deletions]
    for i in to_delete:
        values = values.drop(index = i, inplace=False)

    k_anon.sort()

    return (
        bad_val,
        values,
        values[values["Count"] == 1][: int(len(k_anon) * 0.05)],
        k_anon[int(len(k_anon) * 0.95)],
    )
