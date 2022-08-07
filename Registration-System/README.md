## Description

* Register system is used by almost application. It is normally the first step to use the application.
* We use Python Web Server implement a Register system. 
* We also want provide this system to remote access.

## Related Theory
* Simple HTTP Server With CGI Scripts Enabled
* Sending Emails With Python
* Let anyone in the world to access your Web Server set up at home
* Database Access with Python

## How to use NGRok to map a local private address to a public address(for mac)

You download and run a program on your computer and provide it the port (e.g., 8000) for the computer's a web server.
Run NGRok program on the computer to connect to the NGRok cloud service which accepts traffic on a public address and relays that traffic through to the NGRok process running on your computer and then on to the local address you specified.

**Step 1. go to https://dashboard.ngrok.com/get-started register your own account**

**Step 2. download the ngrok package**

**Step 3. go to the location of the file and run**
```
$ ./ngrok authtoken 82dEPiAPk6GLxWj335LXk_5vBjkFenjSphF1cKo4Sjr
```

## How run the project

**Step 1. download the repo.**
```
$ git clone https://github.com/ling67/Web-Project.git
```
    
Step 6: Test NGRok: Let people access your web server

**Step 2. go to project folder**
```
$ cd $WORD_DIR/html/cgi-bin
```

**Step 3. change the permission**
```
$ chmod a+x *.py
```

**Step 4.  **
```
$ python3 -m http.server –cgi
```

**Step 5.  **
```
Open a browser and enter this URL: http://localhost:8000/regist.html
```

**Step 6. open another terminal, and type**
```
$ ./ngrok http 8000
```

**Step 7. Test NGRok: Let people access your web server**

Now you can access your website based on NGRok provide public address 

## Detail Design Presentation
[Registration_System_Ling_Chen](https://docs.google.com/presentation/d/1fKrEHRzQL_7SV7ZmFwpuIFqvs5zGvqN0Bel_uh_A2tg/edit#slide=id.g25f6af9dd6_0_0)


