# IsoPass

## Introduction
IsoPass is a secure password generator and manager. Given a input of a master password and a application string, IsoPass generate a app-specific password for the application.  

Example input of IsoPass:  
``abc123`` (master password)  
``gmail.com`` (application string)  

Corresponding output of IsoPass:  
``5uhVuonhGETj``  
(for now the output is a 12 char string, but in future updates of IsoPass, the length of output can be customized)  

Then you can use the generated output as your gmail.com login password.

-----
## Philosophy
IsoPass aim to be a secure and convenient password solution. IsoPass, as a password generator and manager, never save your password. Instead, IsoPass generate your passwords upon your requests with the master password provided. Since your passwords are never saved, they would never be stolen or leaked.  

-----
## Features

1. ### Open source  
First and foremost, credibility is indispensable especially in security software. Thus, we open source all of the IsoPass libraries and distributions. Plus, according to GNU GPLv3, all derivatives of IsoPass must also disclose their source codes. Currently, the IsoPass library contains only 150 lines of codes. We encourage you to inspect the codes.

2. ### Irreversible master password  
In cases where specific generated passwords are leaked and fallen into unwanted hands, you have the confidence that the attackers have no way to reverse engineer your master password. And you can save the hassle of changing all your passwords.    

3. ### No storage of sensitive information  
IsoPass eliminates the need for storing password in a secure place. IsoPass also eliminates the risk of password storage being compromised.   

4. ### App-specific passwords  
For different applications, IsoPass generate different passwords that are mathematically unrelated. Remembering only one master password, you can isolate your passwords. Have one million website logins to remember? No worry, IsoPass got you covered. You only need a master password.  

-----
## Planed Features (to be implemented in future updates)

1. ### Native software on all mainstream platforms  
IsoPass is designed to be undemanding on hardware and storage space, which means it is designed to be run on every mobile devices and computers. Linux, macOS, Windows, iOS, Android or even Web... Use IsoPass with the confidence that we got you covered whichever the device you are using.   

1. ### Save application strings  
Application strings like ``gmail.com``, ``nyu.edu`` can be saved locally for user's convenience. To generate app password from saved application strings, user simply select the application and input master password.  

1. ### Multiple profile  
User can have multiple profile with different master passwords. Multiple profile ensures isolation between different applications and offers different level of security. For example, a user can have profiles for his finance, academic, social, nonessential and excreta applications. In such case the user may use easy-to-remember master password for his nonessential applications and type the master password more often on unsecured public computers, and he may use more complex master password for his finance application and type the password on computers with more security infrastructures.  

1. ### Cloud sync of application strings and profiles  
Non-sensitive data like application strings and profiles can be encrypted and synced through our server.
