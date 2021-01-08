# Student’s Horizontal Id-recognizing Tool Application of MaskRCNN and CRNN
[demo slides](https://docs.google.com/presentation/d/1qMaqnTA8Do_8DLh_Mh3rbHAVy760qcUBlFEYj4VT6Yc/edit?usp=sharing)


## Motivation:
During China Wuhan virus, a.k.a. COVID-19, most teachers do a roll call to record students’ attendance. There are two common ways approaching by students: one is to scan the QR code and fill out the questionnaire, and the other is to hold the ID card against the card reader. The former way is time-consuming while the later way needs a special equipment.

## Objective:
Use DL technique to recognize ID’s photo. we can simultaneously capture the ID in a picture, and recognize the photo, name, ID.


## Quick Start
1. Clone the project
  ```
  git clone https://github.com/shangrex/Student_Id_Recognition.git
  ```
2. Install all modules with follwing command.
  ```
  pip install -r requirement.txt
  ```
3. Run the main code
  ```
  python main.py
  ```




## Demo


| demo images	 | student ID | student name |  
| -------- | -------- | -------- |
|  <img src="https://i.imgur.com/XV3kShL.png" width=300>    |  FXXXXXX   | 蔡X恩  |

different image terminal result:

<img src="https://i.imgur.com/y8A418b.png" width=300>




## Reference
* [Mask R-CNN](https://developpaper.com/mask-r-cnn/)
* [MA-CRNN: a multi-scale attention CRNN for Chinese text line recognition in natural scenes](https://link.springer.com/article/10.1007/s10032-019-00348-7)
* [Improving accuracy of the Tesseract – Limitless Data Science](https://limitlessdatascience.wordpress.com/2019/05/01/improving-accuracy-of-the-tesseract/)
* [tesseract architecture](https://limitlessdatascience.wordpress.com/2019/05/01/improving-accuracy-of-the-tesseract/)
* [CNOCR](https://github.com/breezedeus/cnocr)
* [Using Mask R-CNN with a Custom COCO-like Dataset](https://www.immersivelimit.com/tutorials/using-mask-r-cnn-on-custom-coco-like-dataset)
* [labelme](https://github.com/wkentaro/labelme)

## Future Work
- [ ] Multiple image
- [ ] Recgonition video
- [ ] Connect to database to trace
- [ ] Different school student card recognition
