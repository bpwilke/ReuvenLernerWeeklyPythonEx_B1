from collections import Counter

visits = dict()             # initialize global dict()

def collect_places():
    visits.clear()
    inputText = 'init'
    while len(inputText) != 0:
        inputText = input("Tell me where you went: ").strip()
        if ', ' not in inputText and inputText is not None:
            if len(inputText) != 0:
                print("That's not a legal city, country combination")
        else:
            city = inputText.split(", ")[0]          # extract city from input
            country = inputText.split(", ")[1]       # extract country from input
            if country not in visits.keys():         # check if country exists as key in visit dict
                visits[country] = list()             # if it doesn't create the key and empty list
                visits[country].append(city)         # add our first city to that list
            else:                                    # else country already exists as key in visit dict
                visits[country].append(city)         # so add a new city to the list

def display_places():
    print("You visited:")
    for country in sorted(visits.keys()):                   # for each country
        print(country)                                      # print the country
        countedCity = Counter(visits[country])              # get counts 
        for city, count in sorted(countedCity.items()):     # for each city with counts
            if count > 1:                                   # if count is more than 1
                print('    {0} ({1})'.format(city, count))  # print city with count in (n) format
            else:
                print('    {}'.format(city))                # otherwise 1, just print city name

if __name__ == '__main__':
	collect_places()
	display_places()



