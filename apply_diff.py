import cv2
import numpy as np

LR_IMG = cv2.imread('LR/sloth.bmp')
DIFF_IMG = cv2.imread('diff/sloth.bmp')
OUTPUT_PATH = 'result/sloth.bmp'

def upscale(originalImg, diffImg, outputPath):
	height, width = diffImg.shape[:2]
	dim = (int(width),  int(height))
	originalImg = cv2.resize(originalImg, dim, interpolation = cv2.INTER_LINEAR)
	outputImage = np.zeros((height,width,3),np.uint8)

	for i in range(height):
	  for j in range(width):
	     aB, aG, aR = originalImg[i,j]
	     bB, bG, bR = diffImg[i,j]

	     newB = (int(aB) + int(bB)) % 256
	     newG = (int(aG) + int(bG)) % 256
	     newR = (int(aR) + int(bR)) % 256
	     	
	     outputImage[i,j] = [newB,newG,newR]

	cv2.imwrite(outputPath, outputImage)


upscale(LR_IMG, DIFF_IMG, OUTPUT_PATH)