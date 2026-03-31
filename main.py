
#1
import re
text = 'В магазине 3 яблока, 15 груш и 100 вишен'

numbers = re.findall(r"\d+", text)
print(numbers)

#2
def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    if re.fullmatch(pattern, email):
        return True
    else: return False

print(is_valid_email("user.name@example.com"))
print(is_valid_email(""))

#3
text = "Привет   мир!    Как \t дела?"
clean_text = re.sub(r"\s+", " ", text)
print(clean_text)

#4
text = "Встреча назначена на 25.03.2024 в офисе"
pattern = r"\d{2}\.\d{2}\.\d{4}"

match = re.search(pattern, text)
if match:
    print(match.group())
else:
    print("дата не найдена")

#5
import csv
from io import StringIO

csv_data = '"Фамилин, А.А.", 45, "Тольятти, Есенина, 10"'

f = StringIO(csv_data)
reader = csv.reader(f)

for row in reader:
    print(row)
