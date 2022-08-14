index_to_struct = {}
name_to_index = {}
symptoms = {}
remedies = [
    ['niacin'],
    ['nac'],
    ['ginko'],
    ['quercetin'],
    ['nattokinase', 'natto'],
    ['zinc'],
    ['probiotics'],
    ['prebiotics'],
    ['antihistamines']
]

class RemedyClass:
    def __init__(self, name, index):
        self.names = [name]
        self.index = index
        self.count = 0
        self.scores = []

for i in range(len(remedies)):
    for k, v in enumerate(remedies[i]):
        if k == 0:
            struct = RemedyClass(v, i)
            index_to_struct[i] = struct
        else:
            index_to_struct[i].names.append(v)
        name_to_index[v] = i