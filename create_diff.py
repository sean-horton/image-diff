import cv2
import numpy as np


LR_IMG = cv2.imread('HR/sloth.bmp')
HR_IMG = cv2.imread('LR/sloth.bmp')
OUTPUT_PATH = 'diff/sloth.bmp'


def createDif(originalImg, hrImg, outputPath):
	height, width = hrImg.shape[:2]
	dim = (int(width),  int(height))
	originalImg = cv2.resize(originalImg, dim, interpolation = cv2.INTER_LINEAR)
	outputImage = np.zeros((height,width,3),np.uint8)

	for i in range(height):
	  for j in range(width):
	     aB, aG, aR = originalImg[i,j]
	     bB, bG, bR = hrImg[i,j]

	     newB = 0
	     if bB >= aB:
	     	newB = bB - aB
	     else:
	     	newB = 256 - (aB - bB)

	     newG = 0
	     if bG >= aG:
	     	newG = bG - aG
	     else:
	     	newG = 256 - (aG - bG)

	     newR = 0
	     if bR >= aR:
	     	newR = bR - aR
	     else:
	     	newR = 256 - (aR - bR)
	     	
	     outputImage[i,j] = [newB,newG,newR]

	cv2.imwrite(outputPath, outputImage)


createDif(HR_IMG, LR_IMG, OUTPUT_PATH)