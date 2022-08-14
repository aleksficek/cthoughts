symptoms = {}
remedies = {
    'niacin': 0,
    'nac': 1,
    'ginko': 2,
    'quercetin': 3,
    'nattokinase': 4,
    'natto': 4,
    'zinc': 5,
    'probiotics':6,
    'prebiotics':6,
    'antihistamines':7,
}

index_to_struct = {}

class RemedyClass:
    def __init__(self, name, index):
        self.names = [name]
        self.index = index

for k, v in remedies.items():
    if v not in index_to_struct:
        struct = RemedyClass(k, v)
        index_to_struct[v] = struct
    else:
        index_to_struct[v].names.append(k)