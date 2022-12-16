names = []
blocks = []

for i in range(len(data['BLOCKS'])):
    if data['BLOCKS'][i] != 0:
        print(data['PLAYER'][i] + " got at least 1 block")
