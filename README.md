<div align="center">
  <a href="https://github.com/TanimSk/Remote-Terminal">
    <img src="[Documentation/terminal.png](https://raw.githubusercontent.com/TanimSk/Remote-Terminal/server/client/Documentation/terminal.png)" alt="Logo" width="80" height="80">
  </a>
  <h3 align="center">RemoTerminal</h3>
  <p align="center">
    Remote Terminal for gaining access to a computer over the internet
    <br />
    <a href="https://remoterminal.herokuapp.com/">Website</a>
    ·
    <a href="https://github.com/TanimSk/Remote-Terminal/issues/new/choose">Report Bug</a>
    ·
    <a href="https://github.com/TanimSk/Remote-Terminal/issues">Request Feature</a>
  </p>
</div>

# Documentation

### Usage :

[Download](https://remoterminal.herokuapp.com/download  "Download") Remote Terminal Client. After running the program, this `your UUID: blahblah-blah-blah-blah-blahblahblah` will printout on the console. copy the UUID, then come back to this website. Enter (If you wanna save the UUID to browser cookie hit the 'save icon') the UUID then hit 'GO!' . Then you will receive a Browser Terminal. The commands are as same as your OS terminal commands. Theres also some special commands like send keystrokes, get files, get screenshot, get webcam image etc.

### Special Commands:

| Command | Arguments | Description |
| ------------ | ------------ | ------------ |
| **cmdList** | | Prints out all special commands |
| **getFile** | file name | Gets you the file from the target computer <br> Example `getFile abc.jpeg` |
| **getScreen** |  | Captures a screenshot of client computer and send it via websocket |
| **sendKeys** | # &#60;hotkey&#62;<br>&#60;string&#62;<br>&#124; &#60;delay&#62; | You can send keystrokes to the target.<br>For example: `hello,\|5,#enter`<br>Means, the string *hello* will be typed in the target computer, then it will pause for 5 seconds, then hit enter.<br>Notice, there's no space between commas|
| **getWebcam** |  | Captures image from webcam and send it via websocket |
| **terminate** |  | Shuts down the client program and terminates the connection |

