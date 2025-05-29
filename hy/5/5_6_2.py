def addToInventory(inventory, addedItems):  # inventory为字典，战利品总数，addedItems为列表，新获得的战利品
    for i in addedItems:  # 遍历战利品列表
        inventory.setdefault(i, 0)  # 如果战利品字典中没有该物品，则添加该物品，数量为0
        inventory[i] += 1  # 战利品字典里的物品数量加1


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

addToInventory(inv, dragonLoot)


def displayInventory(inventory):  # 5_6_1.py中的遍历
    print('Invebtory:')
    item_total = 0
    for key, value in inventory.items():
        item_total += value
        print(str(value) + ' ' + str(key))
    print('Total number of items: ' + str(item_total))


displayInventory(inv)
