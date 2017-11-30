In this exercise we covered various concepts of openCV like 

- primitive data types(structures)
 
  a) CvPoint (x,y) integers  
  
  b) CvPoint2D32f(x,y) floating points numbers 
  
  c) CvPoint3D32f(x,y,z) floating point numbers
  
  d) CvSize (w,h) integers
  
  e) CvSize2D32f (w,h) floating point numbers
  
  f) CvRect (x,y,w,h) integers
  
  g) CvScalar (val) pointer to an array (containing upto 4 double precision flaoting point numbers)

- constructors

  a) cvSize() for (a)to (f) above
  
  b) for CvScalar we have 3 constructors
  
   i) cvScalar (upto four arguments and assigned to respective member of val)
   
  ii) cvRealScalar ( one argument for first member of val and others as 0)
  
 iii) cvScalarAll (one argument set to all four members)
 
- when we need a vector
 
   use of cvMat (one column multiple rows or vice versa for conjugate/transpose)
   
- Colorspaces

    a)CIE - LAB(L=black/white, A=green/magenta, B=blue/yellow)
    
    b)RGB 
    
    c)YUV (YCbCr)
    
    d)HSL/HSV (hue, saturation, value)
    
    e)CMYK
    
- Smoothing (to reduce noise or camera artifacts, or to reduce resolution)

  a) LPF ( to reduce noises like Gaussian noise, Salt-and-pepper noise, 
  Poisson noise and Speckle noise)
    
    i) Box Filter - CV_BLUR simplest one ( mean of pixels around the input)
   
   ii) Gaussian Filter - most useful though not the fastest (sum of inputs arranged in an array)
   
  iii) Median Filter - (median of pixels around the input)
  
  b) HPF - to find the edges in an image

- Thresholding

a) cvThreshold() - keeps the values above or below a defined limit

b) cvAdaptiveThreshold() - uses two threshold parameters (block size, constant)

- Template Matching

  Algorithm
  
  a) Slide the template image on the source image
   
  b) Calculate NCC at each sliding position

  c) Best match: where NCC is maximum

- Object Tracking

  a) Dense Optical flow
  
  b) Kalman Filtering
  
  c) Meanshift and Camshift
  
  d) Single object trackers
  
  e) Multiple object track finding algorithms
   
 
 
