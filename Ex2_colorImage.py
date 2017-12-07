import sys
import cv2

def main():

    try:
        fn = sys.argv[1]
    except IndexError:
        fn = "baboon.png"

    src = cv2.imread(fn, 1)

    b,g,r = cv2.split(src)

   #RGB channels
    print("RGB value: ",src[20,25])
    cv2.imwrite("RED.png",r)
    cv2.imwrite("BLUE.png",b)
    cv2.imwrite("GREEN.png",g)


    #YCrCb channels
    img = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
    Y,Cr,Cb = cv2.split(img)
    print("YCrCb value: ",src[20,25])
    cv2.imwrite("Yr.png",Y)
    cv2.imwrite("Cr.png",Cr)
    cv2.imwrite("Cb.png",Cb)


    #YCrCb channels
    img = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

    H,S,V = cv2.split(img)

    print("HSV value: ",src[20,25])
    cv2.imwrite("Hue.png",H)
    cv2.imwrite("Saturation.png",S)
    cv2.imwrite("Value.png",V)


    cv2.waitKey(0)

if __name__ == '__main__':
    main()
