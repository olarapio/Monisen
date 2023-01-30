def isPrime(number):
    if number > 1:
        for i in range(2, int(number/2) + 1):
            if number%i == 0:
                return 0
        else: return number
    else: return 0

def monisen(number):
    m = 2 ** number - 1
    if isPrime(m) != 0 and isPrime(number) != 0: return m
    else: return 0

def nth_monisen(number):
    monisen_list = []
    count = 0
    while len(monisen_list) != number:
        moni = monisen(count)
        if moni != 0:
            monisen_list.append(moni)
            
        count += 1
    return monisen_list

if __name__ == "__main__":
    
    print("WARNING: more than 7 monisen numbers will take a long time to be outputed!\n")
    number = input("how many monisen numbers do you want to display?")
    print(nth_monisen(int(number)))