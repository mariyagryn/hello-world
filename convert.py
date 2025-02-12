import nbformat as nbf

script_file = "python_practice_1.py"  # Файл, який конвертуємо
notebook_file = "python_practice_1.ipynb"  # Вихідний ноутбук

# Створюємо новий Jupyter Notebook
notebook = nbf.v4.new_notebook()

try:
    with open(script_file, "r", encoding="utf-8") as f:
        code = f.read().strip()
        if not code:
            raise ValueError("Файл порожній!")

        notebook.cells.append(nbf.v4.new_code_cell(code))  # Додаємо код у ноутбук

    # Зберігаємо .ipynb файл
    with open(notebook_file, "w", encoding="utf-8") as f:
        nbf.write(notebook, f)

    print(f"Файл {notebook_file} створено успішно!")

except FileNotFoundError:
    print(f"Помилка: файл {script_file} не знайдено!")
except ValueError as e:
    print(f"Помилка: {e}")
