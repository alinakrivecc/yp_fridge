import datetime
from decimal import Decimal
DATE_FORMAT = '%Y-%m-%d'
goods = {
    'печенье' : [{'amount' : Decimal('20'), 'expiration_date' : datetime.date(2025, 12, 17)}],
    'йогурт' : [{'amount' : Decimal('5'), 'expiration_date' : datetime.date(2025, 11, 19)}]
}


def add(items, title, amount, expiration_date=None):
    if title not in items:
        items[title] = []

    if isinstance(expiration_date, str):
            expiration_date = datetime.datetime.strptime(expiration_date, DATE_FORMAT).date()

    items[title].append({'amount' : Decimal(str(amount)), 
    'expiration_date' : expiration_date})
print('проверка первой функции:')
add(goods, 'молоко',1.2, datetime.date(2025,11,30))
print(goods['молоко'])
add(goods,'соль', 4)
print(goods['соль'])
add(goods,'печенье', 12, datetime.date(2026,11,20)) 
print(goods,['печенье'])   

def add_by_note(items, note):
    splitted_notes = note.split(' ')

    expiration_date = None
    try: 
        expiration_date = datetime.datetime.strptime(splitted_notes[-1], DATE_FORMAT).date()
        splitted_notes = splitted_notes[:-1]

    except ValueError:
        expiration_date = None

    amount_value = Decimal('1')
    try:
        amount_value = Decimal(splitted_notes[-1])    
        splitted_notes = splitted_notes[:-1]

    except:
        amount_value = Decimal('1')

    title = ' '.join(splitted_notes)

    add(items, title, amount_value, expiration_date)
print('проверка второй функции:')    
print(f'до добавления {goods}')
add_by_note(goods, 'яйца 15 2025-11-20')    
print(f'после добавления: {goods}')

add_by_note(goods, 'хлеб 2025-11-14')
print(f'после добавления: {goods}') 

add_by_note(goods, 'пельмени 58')
print(f'после добавления: {goods}')       

def find(items, needle):
    results = []
    needle_lower = needle.lower()

    for title in items.keys():
        if needle_lower in title.lower():
            results.append(title)
    
    return results
print('проверка третьей функции')
print(f'поиск "йогурт": {find(goods,"йогурт")}')
print(f'поиск "ЙОГУРТ": {find(goods,"ЙОГУРТ")}')
print(f'поиск "печ": {find(goods,"печ")}')
print(f'поиск "молоко": {find(goods,"молоко")}')

def amount(items, needle):
    found_items = find(items, needle)
    total = Decimal('0')

    for title in found_items:
        for batch in items[title]:
            total += batch['amount']
    return total   

print('проверка четвертой функции:')
print(f'количество хлеба: {amount(goods, "хлеб")}') 
print(f'количество пе: {amount(goods, "пе")}')  