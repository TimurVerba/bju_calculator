from tabulate import tabulate


def protein_fats_carbohydrates(weight: float, are_you_doing_sport: str):
    data = []
    if are_you_doing_sport == "y":
        proteins = 2 * weight
        fats = 1.5 * weight
        carbohydrates = 2 * weight
    elif are_you_doing_sport == "n":
        proteins = 1.6 * weight
        fats = 1 * weight
        carbohydrates = 2 * weight
    data.append([proteins, fats, carbohydrates])
    return data


if __name__ == "__main__":
    print("Welcome to protein fats carbohydrates calculator")

    are_you_doing_sport = input("Do you do any sports? (y/n): ").lower()

    while are_you_doing_sport not in ["y", "n"]:
        print("Invalid input. Please enter 'y' or 'n'.")
        are_you_doing_sport = input("Do you do any sports? (y/n): ").lower()

    while True:
        try:
            weight = float(input("Enter your weight (kg): "))
            result_data = protein_fats_carbohydrates(weight, are_you_doing_sport)
            break  # Выход из цикла при успешном вводе веса и расчете
        except ValueError:
            print("Ошибка: Введено некорректное значение веса. Пожалуйста, повторите ввод веса.")


headers = ["Proteins per day", "Fats per day", "Carbohydrates per day"]
colalign = ("center", "center", "center")
table = tabulate(result_data, headers, tablefmt="grid", colalign=colalign)
print(table)


