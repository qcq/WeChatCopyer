## WeChatCopyer

### Purpose
This project is intended for download the e-book by wechat read web app

---

### Install

#### Requirments
* python3
* pip --- manage for the python library
* pynput --- which for control the mouse(click, scroll)
* cnocr --- ocr the chinese words from picture
* pyscreenshot -- take screenshot of specific area
* pyyaml --- parse the raml conf file

```
# by execute below command to install requirments

python3 -m venv venv
source venv/bin/activate
pip install -r requiremnts.txt
```



#### run ut
```
# install current project as develoment/editable mode
pip install -e .
# under root folder, execute below can do unitest
pytest
```

#### run code
```
cd src
python3 main.py
```

#### Configuration
because this tool not direct operate the html or js file, which simulate the manner of peopele.
so, need to let the tools knows some basic info.

like :
* where is the "next chapter" button located <x, y>
* how quick scroll the mouse whell
* .etc

#### How
* open the r.qq.com in browser(in manual)
* open one book which want to copy(in manual)
* execute the script

---

### Explain
*how the tools worked*

1. how to capture the full screen

    **do have many ways, current worked by the help of chrome dev tools**
    * python pair with selenium [reference](https://stackoverflow.com/questions/41721734/take-screenshot-of-full-page-with-selenium-python-with-chromedriver)  <not test>

        * Disadvantage
            * need to deal with the url directly which will not full control

    * merge small sheet together [reference](https://raywoodcockslatest.wordpress.com/2017/02/23/merge-screenshots/)  <not test>

        * Disadvantage
            * should research one way to detect overlap when merge the sheets
            * which makes complicated for scroll control, how long should one step

    * by the help of chrome itself by sent command with the keyboard [reference](https://chiamakaikeanyi.dev/winning-with-chrome-devtools-how-to-capture-full-page-screenshots/)  <favor way>
        ```
        # can use this feature by below commands
        Ctrl+Shift+I
        Ctrl+Shift+P
        Type Scre???
        Choose ???Capture full size screenshot???*
        ```

        * Disadvantage
            * need to detect how to cut the header/footer/side of the full size webpage

2. .etc

### NOTE

1. Captured full size webpage can also be as file to be used as final book
2. This app also can be as the auto reader which for long time online needed

### limit

#### current limits with the help of the PC own host chrome

1. the biggest limits is the project is releate with the screen Display
include the size of the pix of the screen, my cureent pc is 2015 13.3 inch of macbook pro,
which means, before use this project, should use the embed in tools to detect some place of
the screen

2. has releationship with the chrome in full screen or not

