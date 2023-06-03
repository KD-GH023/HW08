import view, mobel

def starts():
    view.graetings()
    while True:
        view.menu()
        answer = input('Введите команду: ')
        if answer == '1':
            date = mobel.get_date()
            view.show_contacts(date)
        elif answer == '2':
            contact = input('Введите данные контакта через пробел: ')
            res = mobel.add_contacts(contact)
            if res:
                view.success(res)
            else:
                view.not_success(res)
        elif answer == '3':
            contact = input('Ввкдите данные контакта для поиска: ')
            result = mobel.find(contact)
            view.show_c0ntact(result)
        elif answer == '4':
            view.error()



