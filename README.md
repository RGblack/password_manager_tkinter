# password_manager_tkinter
Password manager with password generator program build with ui based on tkinter


## Password Manager UI
UI of the program was created using tkinter objects, and grid for placeing them. 

UI setup in main.py is divided into subsections with different object types. 

## Save Password
This section of main.py contains function which is saving password with username and website name to a "saved_passwords.txt" file. 

Saving of password need to be confirmed in pop-up box. 

If any of entry boxes is empty, there will pop-up info and password will not be saved. 

## Password Generator
This function will generate random password containing letters, symbols and numbers in random order. 

It can be used to generate strong password for almost any site. Password will be automaticly saved to clipboard, and copying of password will be confirmed with pop-up box
