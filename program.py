import datetime


def get_current_time() -> datetime:
    delta = datetime.timedelta(hours=3, minutes=0)
    return datetime.datetime.now(datetime.timezone.utc) + delta


name = input("Укажите свое имя: ")
print(f"""Приветствую тебя {name}!!!
Я робот DateTimer у меня ты можешь узнать текущую дату и время
    Дата: текущая дата
    Время: текущее время
    Выход: закрыть программу""")

while True:
    request = input("--> ")
    if request == "Дата":
        print(datetime.datetime.now().date())
    elif request == "Время":
        print(get_current_time().time())
    elif request == "Выход":
        print(f"До встречи {name}!")
        break
    else:
        print("Не верный запрос.")
