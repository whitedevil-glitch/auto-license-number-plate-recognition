# auto-license-number-plate-recognition
Automatically Detects Number Plate's Numbers and Text from a Car Image using Python [OpenCV and tesseract]

## Requirements

``` pip install numpy ```

``` pip install opencv-contrib-python ```

``` pip install pytesseract```

<br>
--
<a href="http://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-setup-4.00.00dev.exe"> Link for tesseract.exe </a>
--

<br>
The installation depends on your operating system. I am using this program on Windows.

We need to add a PATH to windows system variables. Actually it’s an easy step. First we have to find and copy the root folder of the tesseract installation. That should be looking like this:

``` C:\Program Files\Tesseract-OCR ```
[It may vary depending on your installation location. Just make sure evrything is installed in the C drive, so that it's default.]

And search for `Advanced System Settings`.

### Advanced system settings > Advanced > Environment variables > PATH > New

Paste the source path which copied and save this configurations. After this step the computer must be rebooted to apply configurations.

The tesseract installation completed. You can confirm the installation from the command line. When we run ``` tesseract ``` command on the command line, it should give us information about the program.

Now You can run the program. 



## Made with ❤️ by White-Devil
