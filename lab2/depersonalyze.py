import datetime
import re
import pandas
def maskerization_passport(passport: str) -> str:
    return passport[:2] + re.sub(r"\d", "*", passport[2:])


def generalization_doctor(doctor: str) -> str:
    doctor_types = [
        [
            "Дерматолог",
            "Офтальмолог",
            "Иммунолог",
            "Аллерголог",
            "Травматолог",
            "Физиотерапевт",
            "Неонатолог",
            "Гериатр",
            "Педиатр",
            "Лор",
            "Оториноларинголог",
            "Неонатолог-патолог",
            "Косметолог",
            "Ортопед",
            "Эндокринолог",
            "Эндоскопист",
            "Эндоскопист-лапароскопиолог",
            "Генетик",
            "Офтальмолог-окулист",
            "Эндокринолог-диабетолог",
            "Гематолог",
            "Ревматолог",
            "Ревматолог-фармаколог",
            "Фтизиатр",
            "Нефролог",
            "Нефролог-гипертолог",
        ],
        [
            "Кардиолог",
            "Кардиоревматолог",
            "Кардиолог-кардиохирург",
            "Кардиоревматолог-гистолог",
            "Онколог",
        ],
        [
            "Гастроэнтеролог",
            "Гастроэнтеролог-вирусолог",
            "УЗИ-специалист",
            "Гастроэнтеролог-этиолог",
            "Диетолог",
            "Гастроэнтеролог-морфолог",
            "Гепатолог",
        ],
        [
            "Уролог",
            "Онкоуролог",
            "Онкогинеколог",
            "Онкодерматолог",
        ],
        [
            "Пульмонолог",
            "Пульмонолог-тораколог",
        ],
        [
            "Психиатр",
            "Невролог",
            "Психотерапевт",
            "Невропатолог",
        ],
        [
            "Стоматолог",
            "Ортодонт",
        ],
    ]

    for i, t in enumerate(doctor_types):
        if doctor in t:
            if i == 0:
                return f"Терапевтическое отделение"
            if i == 1:
                return f"Кардиологическое отделение"
            if i == 2:
                return f"Гастроэнтерологическое отделение"
            if i == 3:
                return f"Урологическое/Гинекологическое отделение"
            if i == 4:
                return f"Пульмонологическое отделение"
            if i == 5:
                return f"Неврологическое отделение"
            if i == 6:
                return f"Стоматологическое отделение"

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
    df = df.drop("Symptoms", axis=1)
    df = df.drop("Analysis", axis=1)

    df["Doctor"] = df["Doctor"].apply(generalization_doctor)

    df["DateStart"] = df["DateStart"].apply(generalization_date_start)
    df = df.drop("DateEnd", axis=1)

    df["Price"] = df["Price"].apply(aggregation_price)
    df["Card"] = df["Card"].apply(generalization_card)

    return df


def calc_k_anonymity(df: pandas.DataFrame, cols):
    k = 1
    if len(df) < 51000:
        k = 6
        #k = 10
    elif len(df) < 105000:
        k = 6
        #k = 7
    elif len(df) < 260000:
        k = 6

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
