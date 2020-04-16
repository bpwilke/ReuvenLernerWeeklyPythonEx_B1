from collections import Counter

def average_age_under(data, under = None):
    if under:
        ages = [people['age'] for people in data if people['age'] < under]
    else:
        ages = [people['age'] for people in data]
    if not ages:
        return 0
    else:
        return (sum(ages) / len(ages))

def all_hobbies(data):
    hobbies_all = list()
    for hobbies in [people['hobbies'] for people in data]:
        for hobby in hobbies:
            hobbies_all.append(hobby)
    return set(hobbies_all)

def hobby_counter(data):
    hobbies_all = list()
    for hobbies in [people['hobbies'] for people in data]:
        for hobby in hobbies:
            hobbies_all.append(hobby)
    hobbies_counts = Counter(hobbies_all)
    return hobbies_counts

def n_most_common(data, most_common = None):
    hobbies_all = list()
    for hobbies in [people['hobbies'] for people in data]:
        for hobby in hobbies:
            hobbies_all.append(hobby)
    hobbies_counts = Counter(hobbies_all)
    return [each[0] for each in hobbies_counts.most_common(most_common)]