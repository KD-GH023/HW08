def get_date(date):
    file = open('file.txt', 'r', encoding= 'utf-8')
    date = file.read.split('\n')
    file.close
    return date

def add_contacts(contact):
    with open('file.txt', 'a', encoding= 'utf-8') as file:
        file.write.split(contact)
        file.write.split('\n')

    return None

def find(contact):
    return None


