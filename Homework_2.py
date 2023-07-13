#zad1
def sum_of_min_and_max(arr):
    return min(arr) + max(arr)
print(sum_of_min_and_max([5, 2, 3, 4, 13, 8, 23]))
print(sum_of_min_and_max([-20, 5, 18, 24]))
print(sum_of_min_and_max([1]))
#zad2
def sum_of_divisors(n):
    result = 0
    for i in range(1, n+1):
        if n %i == 0:
            result = result + i
    return result
print(sum_of_divisors(16))
#zad3
def is_prime(n):
    if n == 1:
        False
    for itr in range(4, n):
        if n%itr ==0:
            return False
        return True
    print (is_prime(4))    
#zad4 
def is_int_palindrome(n):
    n_str = str (n)
    reversed_str = n_str[::-1]
    return n_str == reversed_str
print(is_int_palindrome(1561))
#zad5
def contains_digit(number, digit):
    number_str = str (number)
    digit_str = str(digit)
    return digit_str in number_str
print(contains_digit(42, 2))
#zad6
def contains_digits(num, digits):
    for digit in digits:
        if str(digit) not in str(num):
            return False
        else:
            return True
print(contains_digits(4565436, [5, 6, 4]))
#zad7
def count_substrings(haystack, needle):
    count_substrings = 0
    for char in haystack:
        if char  == needle:
            count_substrings = count_substrings + 1

    return count_substrings
result = count_substrings("Python is an awesome language to program in!", "o")
print(result)
#zad8
def biggest_difference(arr):
    min = arr[0]
    max = arr[0]
    for num in arr:
        if num < min:
            min = num
        if num > max:
           max = num
    return max - min
print(biggest_difference([2, 6, 18, 3, 9, 20]))       
#zad9
def slope_style_score(scores):
    scores.sort()
    scores = scores[1:-1]
    average = sum(scores) / len(scores)
    final_score = round(average, 2)
    return final_score


print(slope_style_score([94, 95, 95, 95, 90]))
#zad10
def what_is_my_sign(day, month):
      
    if month == 'december':
        astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'
          
    elif month == 'january':
        astro_sign = 'Capricorn' if (day < 20) else 'aquarius'
          
    elif month == 'february':
        astro_sign = 'Aquarius' if (day < 19) else 'pisces'
          
    elif month == 'march':
        astro_sign = 'Pisces' if (day < 21) else 'aries'
          
    elif month == 'april':
        astro_sign = 'Aries' if (day < 20) else 'taurus'
          
    elif month == 'may':
        astro_sign = 'Taurus' if (day < 21) else 'gemini'
          
    elif month == 'june':
        astro_sign = 'Gemini' if (day < 21) else 'cancer'
          
    elif month == 'july':
        astro_sign = 'Cancer' if (day < 23) else 'leo'
          
    elif month == 'august':
        astro_sign = 'Leo' if (day < 23) else 'virgo'
          
    elif month == 'september':
        astro_sign = 'Virgo' if (day < 23) else 'libra'
          
    elif month == 'october':
        astro_sign = 'Libra' if (day < 23) else 'scorpio'
          
    elif month == 'november':
        astro_sign = 'scorpio' if (day < 22) else 'sagittarius'
          
    print(astro_sign)
      
if __name__ == '__main__':
    day = 26
    month = "june"
    what_is_my_sign(day, month)
#zad11