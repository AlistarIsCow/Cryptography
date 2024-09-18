import random
import math

def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if (n%i) == 0:
            return False
    return True

def singleBitTest(result, keyLength):
    sumOfOnes = sum(result)
    print(f"Single Bit Test: {sumOfOnes} expected: (9725, 10275)")
    if sumOfOnes < 10275 and sumOfOnes > 9725 :
        return True
    return False

def longSeriesTest(result, keyLength):
    length = 0
    for i in range(keyLength):
        if i == 0:
            last = result[i]
            length += 1
        else:
            if result[i] != last:
                if (length > 25):
                    print(f"Long Series Test: {length} expected: <26")
                    return False
                length = 1
                last = result[i]
            else:
                length += 1
    print(f"Long Series Test: passed")
    return True

def seriesTest(result, keyLength):
    series = [0] * 6
    length = 0
    for i in range(keyLength):
        if i == 0:
            last = result[i]
            length += 1
        else:
            if result[i] != last:
                if (result[i] == 1):
                    series[length-1] += 1
                length = 1
                last = result[i]
            else:
                if length < 6:
                    length += 1
    print(f"Series test")
    print(f"Length 1: {series[0]} expected: (2315, 2685)")
    print(f"Length 2: {series[1]} expected: (1114, 1386)")
    print(f"Length 3: {series[2]} expected: (527, 723)")
    print(f"Length 4: {series[3]} expected: (240, 384)")
    print(f"Length 5: {series[4]} expected: (103, 209)")
    print(f"Length 6: {series[5]} expected: (103, 209)")
    if series[0] >= 2685 or series[0] <= 2315:
        return False
    if series[1] >= 1386 or series[1] <= 1114:
        return False
    if series[2] >= 723 or series[2] <= 527:
        return False
    if series[3] >= 384 or series[3] <= 240:
        return False
    if series[4] >= 209 or series[4] <= 103:
        return False
    if series[5] >= 209 or series[5] <= 103:
        return False
    return True

def pokerTest(result, keyLength):
    series = [0] * 16
    for i in range(0,keyLength,4):
        index = 8*result[i] + 4*result[i+1] + 2*result[i+2] + result[i+3]
        series[index] += 1
    seriesSquared = [i*i for i in series]
    x = 16/5000 * sum(seriesSquared) - 5000
    print(f"Poker test: {x} expected (2.16, 46.17)")
    if x < 2.16 or x > 46.17:
        print("Value: " + str(x))
        return False
    return True

def createFile(name, keyLength, generateRangeMin = 1, generateRangeMax = 100000):
    primes = [i for i in range(generateRangeMin, generateRangeMax) if (isPrime(i) and (i % 4 == 3))]
    p = random.choice(primes)
    q = random.choice(primes)
    while (p==q):
        q = random.choice(primes)
    N = p*q
    numbers = [i for i in range(generateRangeMin, generateRangeMax) if (i % p != 0 and i % q != 0)]
    x = random.choice(numbers)
    resultNumbers = []
    for i in range(keyLength):
        print(i)
        if (i==0):
            resultNumbers.append((x*x)%N)
        else:
            resultNumbers.append((resultNumbers[i-1]*resultNumbers[i-1])%N)
    output_file = open(name, 'w')
    for i in range(keyLength):
        LSB = resultNumbers[i]%2
        output_file.write(str(LSB))
    output_file.close()

def checkFile(name):
    file = open(name, 'r')
    key = file.read()
    file.close()
    keyLength = len(key)
    result = [int(i) for i in key]
    if(keyLength < 20000):
        print("The length is not enough: " + str(keyLength) + " (should be at least 20000)\n")
        return 
    singleTestRun = singleBitTest(result, 20000)
    seriesTestRun = seriesTest(result, 20000)
    longSeriesTestRun = longSeriesTest(result, 20000)
    pokerTestRun = pokerTest(result, 20000)
    if singleTestRun and seriesTestRun and longSeriesTestRun and pokerTestRun:
        return True
    return False



createFile("key.txt", 20000)    
checkFile("key.txt")

#1. Liczby nie wykazują korelacji między sobą
#   Liczby wyglądają jakby były równo rozłożone w podanym zakresie
#   Wygenerowane są wszystkie liczby z podanego zakresu, zanim zaczną się powtarzać
#2. Testy statystyczne, graficznie, częstotliwości, "runs test", najdłuższy "run"
#6. Generator BBS zawsze przechodzi testy dla wartości liczb pierwszych do 100 000. Oznacza to, że generator ten jest bezpieczny.