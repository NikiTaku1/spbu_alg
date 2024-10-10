import tkinter as tk

from depersonalyze import *

cols = ["Passport", "Doctor", "Symptoms", "Analysis", "DateStart", "Price", "Card"]


def run_function():
    # Получаем значение из текстового поля
    input_file = input_entry.get()
    
    df = pandas.read_csv(input_file)
    df = anonimyze(df)
    bad, res, ones, k_anon = calc_k_anonymity(
        df, list(filter(lambda name: checkboxes_vars[name].get(), cols))
    )
    bad1 = {k: v for k, v in sorted(bad.items(), key=lambda item: item[0])}
    

    # Выводим результат
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
    result_text.insert(
        tk.END,
        f"K-anonimity: {k_anon}\n"
        + "\n".join(f"Bad value {k}: {v/len(df)*100}%" for k, v in bad1.items())
        + "\n",
    )

    result_text.insert(tk.END, f"{ones}")

    result_text.config(state=tk.DISABLED)

    res1: pandas.DataFrame
    cols1 = list(filter(lambda name: checkboxes_vars[name].get(), cols))
    res_index = res.set_index(cols1).index
    ones_index = ones.set_index(cols1).index
    mask = ~res_index.isin(ones_index)
    res1 = res.loc[mask]

    res2: pandas.DataFrame
    ones1 = ones.drop("Count", axis=1)
    df_index = df.set_index(cols1).index
    ones1_index = ones1.set_index(cols1).index
    mask = ~df_index.isin(ones1_index)
    res2 = df.loc[mask]


    res.to_csv(f"unique_types_and_counts.csv", index=False)
    ones.to_csv(f"excess.csv", index=False)
    res1.to_csv(f"types_without_excess.csv", index=False)
    res2.to_csv(f"full_without_excess.csv", index=False)

    

# Создаем главное окно
root = tk.Tk()
root.title("Tkinter Interface")

# Строка 1: Текстовое поле
input_label = tk.Label(root, text="Input")
input_label.grid(row=0, column=2, sticky=tk.W)
input_entry = tk.Entry(root)
input_entry.grid(row=0, column=4, padx=10, pady=5)

# Строка 2: Чекбоксы
checkboxes_vars = {}
for i, col in enumerate(cols):
    checkbox_var = tk.IntVar()
    checkboxes_vars[col] = checkbox_var
    checkbox = tk.Checkbutton(root, text=col, variable=checkbox_var)
    checkbox.grid(row=1, column=i, padx=5, pady=5)

# Строка 3: Кнопка "Run"
run_button = tk.Button(root, text="Run", command=run_function)
run_button.grid(row=2, column=0, columnspan=7, pady=10)

# Строка 4: Область для вывода результата
result_text = tk.Text(root, height=20, width=100, state=tk.DISABLED)
result_text.grid(row=3, column=0, columnspan=7, padx=10, pady=5)


# Запускаем главный цикл событий
root.mainloop()



## Анон -> убираем некоторые k=1 -> считаем общую k -> вывод результатов
## или
## Анон -> считаем общую k -> убираем некоторые k=1 -> вывод результатов