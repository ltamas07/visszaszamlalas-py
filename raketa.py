ora = int(input('Hány órás visszaszámlálást tervez? '))
osszora = 0
for i in range(ora):
    print(f'A kilövésig {ora-i} óra van hátra.')
    megszakit = input('Megszakítja a visszaszámlálást? ')
    if megszakit == "i":
        osszora = osszora + 1
print(f'A rakéta a visszaszámlálást követően ennyi órával indult: {osszora + ora}')