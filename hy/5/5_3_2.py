allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}


def totalBrought(guests, item):  # guests是字典，客人带的东西的信息，item是字符串，表示要统计的东西
    numTotal = 0
    for k, v in guests.items():  # k是客人的名字，v是一个字典，表示这个客人带的东西
        numTotal += v.get(item, 0)  # v.get(item, 0)表示如果这个客人带了item，就加上这个数量，否则加0
    return numTotal


print('Number of things being brought:')
print(' - Apples     ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups       ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes      ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies ' + str(totalBrought(allGuests, 'apple pies')))
