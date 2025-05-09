from crud.seed import generate_and_insert_fake_data
from crud import my_select as select




if __name__ == "__main__":
    # generate_and_insert_fake_data()

    while True:
        number = input("Подай номер запиту: (1-10) ")
        if number.lower() == 'exit':
            break
        if number == '1':
            print(select.select_1())
        elif number == '2':
            print(select.select_2(4))
        elif number == '3':
            print(select.select_3(3))
        elif number == '4':
            print(select.select_4())
        elif number == '5':
            print(select.select_5(2))
        elif number == '6':
            print(select.select_6(1))
        elif number == '7':
            print(select.select_7(2, 3))
        elif number == '8':
            print(select.select_8(2))
        elif number == '9':
            print(select.select_9(18))
        elif number == '10':
            print(select.select_10(14, 2))
        else:
            print("Виникла проблема, спройбуйте ще раз")
