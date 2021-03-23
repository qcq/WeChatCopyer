# The basic flow to copy e-book
*many ideas current in my mind, also updated time by time. Below is current one*

take Qt in project to hold the fixed size window,
1. take the user to main page
2. check if the user login, if not go to 3, or to 4
3. by scan the code to login
4. after login, show the bookstore belongs to that user
5. the user type in the book which want to copy
6. open that book, start to copy the whole book
7. put the content to one file
8. after the process finished, notify the user by one way


## copy current chapter of opened e-book

  1. with the help pynput, move the mouse to one open place.
  2. click the left mouse once to activate the chrome
  3. press the keybord ctrl + shift + i to open dev tools
  4. release above 3 keys
  5. press the ctrl + shift + p to open search dialog
  6. relese above 3 keys
  5. type in "Capture full size screenshot"
  6. press the enter
  7. release the enter
  8. press the keybord ctrl + shift + i to close dev tools
  9. release above 3 keys
  10. after the above setps, can save the current chapter

## click "Next Chapter"

  1. scroll the mouse *can define random sleep for scroll, that means can be used auto reader*
  2. capture fixed size picture which the "next chapter" should exist
  3. ocr step 2 picture, then check if the "next chapter" exist, if yes go 4, or back to step 1
  4. to the end of webpage, click the "next chapter"
  5. wait some time and scpture the current screen
  6. ocr the step captured picture, if that exist characters in it go 7, or go 5
  7. end, can capture the full webpage again.

## stop copy operation
  1. the current page has no "next chapter"
  2. the script notify the user and exit

## OCR to convert the picture to text
  1. after get the full webpage for specifc chapter
  2. cut of the header, footer, sider
  3. with the help pf cnocr to conver the picture
  4. after finish one chapter, then go back step 1

