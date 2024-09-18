import numpy as np
import skimage.io as io
import skimage
import random

whitePattern = [[[0,0,1,1],[0,0,1,1]],
                [[1,1,0,0],[1,1,0,0]],
                [[0,1,0,1],[0,1,0,1]],
                [[1,0,1,0],[1,0,1,0]],
                [[0,1,1,0],[0,1,1,0]],
                [[1,0,0,1],[1,0,0,1]]]

blackPattern = [[[1,0,0,1],[0,1,1,0]],
                [[0,1,1,0],[1,0,0,1]],
                [[0,0,1,1],[1,1,0,0]],
                [[1,1,0,0],[0,0,1,1]],
                [[0,1,0,1],[1,0,1,0]],
                [[1,0,1,0],[0,1,0,1]]]


def createPicture(inputPicture, outputPictureOne, outputPictureTwo, outputResult):
    img = io.imread(inputPicture, as_gray=True)
    img = img > 0.5
    h, w = img.shape
    pictures = [np.zeros((2*h, 2*w)), np.zeros((2*h, 2*w))]
    
    for r in range(h):
        for c in range(w):
            if img[r][c] == 0:
                pattern = random.choice(blackPattern)
                for i in range(2):
                    pictures[i][r*2][c*2] = pattern[i][0]
                    pictures[i][r*2+1][c*2] = pattern[i][1]
                    pictures[i][r*2][c*2+1] = pattern[i][2]
                    pictures[i][r*2+1][c*2+1] = pattern[i][3]
            else:
                pattern = random.choice(whitePattern)
                for i in range(2):
                    pictures[i][r*2][c*2] = pattern[i][0]
                    pictures[i][r*2+1][c*2] = pattern[i][1]
                    pictures[i][r*2][c*2+1] = pattern[i][2]
                    pictures[i][r*2+1][c*2+1] = pattern[i][3]
    pictures[0] = skimage.img_as_ubyte(pictures[0])
    pictures[1] = skimage.img_as_ubyte(pictures[1])
    io.imsave(outputPictureOne, pictures[0])
    io.imsave(outputPictureTwo, pictures[1])
    pictureMerge = 255 - (pictures[0] + pictures[1])
    io.imsave(outputResult, pictureMerge)

createPicture(rf"example.png", rf"example1.png", rf"example2.png", rf"example3.png")
