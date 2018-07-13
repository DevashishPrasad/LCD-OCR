# LCD-OCR
This is a tesseract based OCR to read from seven segment display. 

This is not generalized solution. The satements and parameters of some funtions will changed according to the texture,
color, lighting effect and visibility of text of image.

Tesseract is an open-sourced OCR which is capable of reading text from papers, pdfs and other clean formats. Tesseract fails when 
tried to perform OCR on noisy and dirty images (for eg. Embossed or Engraved text). The code uses opencv image filtering techniques
to filter the images as clean as possible and then feeds it to Tesseract.  

## Dependencies
  Python<br> 
  OpenCV<br>
  Tesseract<br>
  Numpy<br>
  imutils<br>

## Example
### Detecting white colored pixels
<img src="images/color.png" alt="Picture not availble in your browser"/>

#### Edged image (canny)
<img src="images/edge.png" alt="Picture not availble in your browser"/>

#### Dilated image

<img src="images/dilate.png" alt="Picture not availble in your browser"/>

#### Inverted threshold image

<img src="images/invert.png" alt="Picture not availble in your browser"/>

#### Results 

<img src="images/lcd9.png" alt="Picture not availble in your browser"/>

## Sample results - 
<img src="images/lcd2.png" alt="Picture not availble in your browser"/>
<img src="images/lcd3.png" alt="Picture not availble in your browser"/>
<img src="images/lcd4.png" alt="Picture not availble in your browser"/>
<img src="images/lcd5.png" alt="Picture not availble in your browser"/>
<img src="images/lcd6.png" alt="Picture not availble in your browser"/>
<img src="images/lcd7.png" alt="Picture not availble in your browser"/>
<img src="images/lcd8.png" alt="Picture not availble in your browser"/>

The code may fail sometimes but tuning parameters of canny and appropriate dialation may improve results. For more accuracy you need to train tesseract for LCD font. Training tesseract for your font is not difficult and it will give your ocr very high level accuracy. I have not trained my tesseract for LCD font.

