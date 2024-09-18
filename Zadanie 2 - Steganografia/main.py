from PIL import Image

def toBinary(message):
        inBinary = []
        for i in message:
            inBinary.append(format(ord(i), '08b'))
        return inBinary

def modifyPixels(pix, data):
    message = toBinary(data)
    imageData = iter(pix)
 
    for i in range(len(message)):
        pix = [value for value in imageData.__next__()[:3] +
                                imageData.__next__()[:3] +
                                imageData.__next__()[:3]] 
        for j in range(0, 8):
            if (message[i][j] == '0' and pix[j]% 2 != 0):
                pix[j] -= 1
            elif (message[i][j] == '1' and pix[j] % 2 == 0):
                if(pix[j] != 0):
                    pix[j] -= 1
                else:
                    pix[j] += 1

        if (i == len(message) - 1):
            if (pix[-1] % 2 == 0):
                if(pix[-1] != 0):
                    pix[-1] -= 1
                else:
                    pix[-1] += 1
        else:
            if (pix[-1] % 2 != 0):
                pix[-1] -= 1
 
        pix = tuple(pix)
        yield pix[0:3]
        yield pix[3:6]
        yield pix[6:9]

def encode_enc(newImage, message):
    w = newImage.size[0]
    x = 0
    y = 0
    for pixel in modifyPixels(newImage.getdata(), message):
        newImage.putpixel((x, y), pixel)
        if (x == w - 1):
            x = 0
            y += 1
        else:
            x += 1

def encode():
    inputImageName = input("Enter image name: ")
    image = Image.open(inputImageName, 'r')
    outputImage = image.copy()
    message = input("Enter data to be encoded : ")
    encode_enc(outputImage, message)
    outputImage.save(inputImageName.split(".")[0] + "_hidden." + inputImageName.split(".")[1], str(inputImageName.split(".")[1].upper()))
 
def decode():
    inputImageName = input("Enter image name: ")
    image = Image.open(inputImageName, 'r')
    decryptedMessage = ''
    imageData = iter(image.getdata()) 
    while (True):
        pixels = [value for value in imageData.__next__()[:3] +
                                imageData.__next__()[:3] +
                                imageData.__next__()[:3]]
        charBinary = ''
        for i in pixels[:8]:
            if (i % 2 == 0):
                charBinary += '0'
            else:
                charBinary += '1'
        decryptedMessage += chr(int(charBinary, 2))
        if (pixels[-1] % 2 != 0):
            return decryptedMessage

x = int(input("1. Encode \n2. Decode\n"))

if (x == 1):
    encode()
elif (x == 2):
    print(decode())


#1. Nie, ponieważ można ją w relatywnie prosty sposób odszyfrować lub zniszczyć.
#2. Deszyfrowanie: metodą Brute Force można zdeszyfrować wiadomość w krótkim czasie.
#   Niszczenie: zamiana ostatniego bitu w pikselach na losowe "1" i "0".
#3. W  3 pikselach zdjęcia można ukryć 1 znak co oznacza, że w obrazie o N pikselach można ukryć wiadomość o N/3 znakach.