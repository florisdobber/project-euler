number_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety',
1000: 'one thousand'}

def main():
    sum = 0
    for i in range(1,1000+1):
        sum += len(write_out(i).replace(" ", ""))
    print(sum)

def write_out(n):
    if n in number_dict.keys():
        return number_dict[n]
    num_hundred = n // 100
    n -= num_hundred * 100
    if n == 0:
        return number_dict[num_hundred] + ' hundred'
    if n in number_dict.keys():
        return number_dict[num_hundred] + ' hundred and ' + number_dict[n]
    num_ten = n // 10
    n -= num_ten * 10
    result = ""
    if num_hundred > 0:
        result += number_dict[num_hundred] + ' hundred and '
    return result + number_dict[num_ten * 10] + " " + number_dict[n]

main()