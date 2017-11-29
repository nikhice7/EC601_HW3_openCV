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
    
 - Smoothing
 - Thresholding
 - Template Macthing
 - Object Tracking
 
 
