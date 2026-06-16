import cv2
import numpy as np


# 문제 1.
#
# BGR 이미지를 Gray 이미지로 변환하세요.
#
# OpenCV 함수를 활용하세요.
def convert_to_gray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# 문제 2.
#
# 이미지를 지정한 크기로 변경하세요.
#
# width와 height를 사용하여
# 새로운 크기의 이미지를 반환해야 합니다.
def resize_image(
    image,
    width,
    height,
):
    return cv2.resize(image,(width,height))


# 문제 3.
#
# Gray 이미지에 Binary Threshold를 적용하세요.
#
# threshold_value를 기준으로
# Binary 이미지를 생성해야 합니다.
#
# 반환값은 Binary Image 입니다.
def apply_threshold(
    gray_image,
    threshold_value,
):
    _, binary_image = cv2.threshold(gray_image, threshold_value,255, cv2.THRESH_BINARY)
    return binary_image

# 문제 4.
#
# 이미지에서 빨간색 픽셀 개수를 계산하세요.
#
# BGR 이미지를 입력으로 받습니다.
#
# 빨간색 조건:
# R > 200
# G < 50
# B < 50
#
# 조건에 맞는 픽셀 개수를 반환하세요.
def count_red_pixels(image):
    B = image[:,:,0]
    G = image[:,:,1]
    R = image[:,:,2]
    red_mask = (R > 200) & (G < 50) & (B <50)
    red_pixel_count = np.sum(red_mask)
    return red_pixel_count
                                       

# 문제 5.
#
# Binary Mask에서 객체 중심 좌표를 계산하세요.
#
# 흰색 픽셀(255)의 평균 위치를 이용하여
# 중심 좌표를 계산합니다.
#
# 반환값:
# (cx, cy)
#
# 객체가 없으면 None 반환
def find_object_center(mask):
    y, x = np.where(mask > 0)

    if len(y) ==0 or len(x) == 0:
        return None
    
    cy = int(np.mean(y))
    cx = int(np.mean(x))

    return (cx, cy)