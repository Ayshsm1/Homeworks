#zad1
def is_anagram(fst_word, snd_word):
    fst_word = sorted(fst_word.lower())
    snd_word = sorted(snd_word.lower())
    if(fst_word == snd_word):
        return"True"
    else:
        return"False"
print(is_anagram("BRADE", "BEARD"))
#zad2
def count_words(arr):
    word_count = {}
    for word in arr:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count
words = ["apple", "banana", "apple", "orange", "banana", "apple", "grape"]
result = count_words(words)
print(result)
#zad3
def nan_expand(times):
    if times == 0:
        return ""
    else:
        return "Not a " + nan_expand(times - 1)
print(nan_expand(1))  
print(nan_expand(2))  
print(nan_expand(3))
#zad4
def group(items):
    result = []
    current_group = []
    for item in items:
        if not current_group or item == current_group[0]:
            current_group.append(item)
        else:
            result.append(current_group)
            current_group = [item]
    if current_group:
        result.append(current_group)
    return result

def max_consecutive(items):
    max_count = 0
    current_count = 1
    for i in range (1, len(items)):
        if items[i] == items[i-1]:
            current_count +=1
        else:
            max_count = max(max_count, current_count)
            current_count = 1
    return max(max_count, current_count)
print(max_consecutive([1, 1, 1, 2, 3, 1, 1]))
#zad5
def sum_of_numbers(st):
    sum_numbers = 0
    for i in st:
        if i.isdigit() == True:
            x = int(i)
            sum_numbers = sum_numbers + x
    return sum_numbers
print(sum_of_numbers("569hdv3134"))
print(sum_of_numbers("jhdj4852svg"))
#zad6
def gas_station(distance, tank_size, stations):
    result = []
    empty_tank = 0 + tank_size

    if tank_size > distance:
        return result
    
    for station_idx in range(0, len(stations) - 1):
        if empty_tank < stations[station_idx+1]:
            result.append(stations[station_idx])

        result.append(stations[-1])        

    return  result
print(gas_station(320, 90, [50, 80, 140, 180, 220, 290]))