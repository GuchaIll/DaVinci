import cv2
import numpy as np
from matplotlib import pyplot as plt

def triangulate(img):
    pass

def vectorize(img):
    pass

def thinning(img):
    pass

def convert_image(img_path):
  img = cv2.imread(img_path,cv2.IMREAD_GRAYSCALE)
  imgColor = cv2.imread(img_path)
  if img is None:
      return -1
  div = 64
  quantized = img // div * div + div // 2
  edges = cv2.Canny(img, 100, 200)
  quantized_Edge = cv2.Canny(quantized, 250, 300)
  
  sigma1 = 0.2
  sigma2 = 0.4
  
  blur1 = cv2.GaussianBlur(img, (0,0), sigma1)
  blur2 = cv2.GaussianBlur(img, (0,0), sigma2)
  
  DoG = blur1 - blur2
  threshold = 20
  edge_image = (DoG > threshold).astype(np.uint8) * 255
  
  d = 9
  sigma_color = 75
  sigma_space = 75
  
  bilateral = cv2.bilateralFilter(img, d, sigma_color, sigma_space)
  bilateral_edge = cv2.Canny(bilateral, 100,200)
  
  overexposed = cv2.addWeighted(img, 2.0, np.zeros(img.shape, img.dtype), 0, 0)
  overexposed_edge = cv2.Canny(overexposed, 100,200)
  
  plt.subplot(421),plt.imshow(img,cmap = 'gray')
  plt.title('Original Image'), plt.xticks([]), plt.yticks([])
  plt.subplot(422),plt.imshow(edges,cmap = 'gray')
  plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
  plt.subplot(423),plt.imshow(quantized,cmap = 'gray')
  plt.title('Quantized'), plt.xticks([]), plt.yticks([])
  plt.subplot(424),plt.imshow(quantized_Edge,cmap = 'gray')
  plt.title('Quantized Edge'), plt.xticks([]), plt.yticks([])
  plt.subplot(425),plt.imshow(edge_image,cmap = 'gray')
  plt.title('DoG'), plt.xticks([]), plt.yticks([])
  plt.subplot(426),plt.imshow(overexposed_edge,cmap = 'gray')
  plt.title('Overexposed_Edge'), plt.xticks([]), plt.yticks([])
  plt.subplot(427),plt.imshow(bilateral,cmap = 'gray')
  plt.title('Bilateral'), plt.xticks([]), plt.yticks([])
  plt.subplot(428),plt.imshow(bilateral_edge,cmap = 'gray')
  plt.title('Bilateral Edge'), plt.xticks([]), plt.yticks([])
  plt.show()
 
def main():
  convert_image('images/im2.jpg')


if __name__ == "__main__":
    main()