# Recoil-Script
![GitHub last commit](https://img.shields.io/github/last-commit/Bboddy/Recoil-Script) ![GitHub all releases](https://img.shields.io/github/downloads/Bboddy/Rust-Recoil-Script/total) <br>
<h3>Controls recoil from <a href="https://rust.facepunch.com/" target="_blank">Rust</a>, with smoothing and randomization.</h3>

![Untitled](https://user-images.githubusercontent.com/43559704/143996297-681039bf-a738-40e5-9881-5c50638ef14b.gif)

## Warning

* Use At Your Own Risk
  - Using this on EAC may result in a ban
  - Only randomization is within the smoothing

## For Personal Use
* Fov is best at 90
  - Best sense is 0.5
* Dont Use Overlay
  - Its a top most and unnecessary
  - Remove start_overlay() inside run() under #Startup Functions
* No need to setup the Loader
  - This was built for fun and to send to some friends
* Best to Change these lines with some more randomization 
  ![carbon (1)](https://user-images.githubusercontent.com/43559704/143992047-9b11df27-b16c-4975-a11a-26b3767d5ebf.png)

## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com) and [Python 3.9](https://www.python.org/downloads/release/python-399/)


Clone this repository
```bash
$ git clone https://github.com/Bboddy/Recoil-Script
```

Go into the repository
```bash
$ cd Recoil-Script
```

Install Packages
```bash
$ python -m pip install requirements.txt
```

Run the app
```bash
$ python Recoil.py
```

## How To Use Loader

You will need a Database setup as such

![Screenshot_2](https://user-images.githubusercontent.com/43559704/144000003-438599a5-c66d-4976-a2b9-066804bde567.png)

![Screenshot_3](https://user-images.githubusercontent.com/43559704/144000073-04d12840-4a7f-4ec8-a6f7-b890c037e85c.png)

I am using PHPmyadmin setup on Cpanel

Next you will need your DB info

![carbon (2)](https://user-images.githubusercontent.com/43559704/144000309-ab9ed88e-24e7-48b2-af2f-3ccb40e3fc2b.png)

I decided to encrypt all of my connection strings before hand using cryptography.fernet

![carbon (3)](https://user-images.githubusercontent.com/43559704/144001009-7113d64f-6ef4-410a-9964-10dc887b5412.png)

Repeat this for your DB, Username, Password

Once encrypted put them into there respective spots in Loader.py

## Credits

- [awhall56](https://www.unknowncheats.me/forum/rust/390615-paste-recoil-script.html) - A start on how everything works
- [absolutenothing](https://www.unknowncheats.me/forum/rust/335162-gun-recoil-tables-crouched-standing.html) - Some of the Recoil Tables
- [RandyShanks](https://www.unknowncheats.me/forum/rust/386523-rust-recoil-tables-pixel.html) - Some of the Recoil Tables
- [UC](https://www.unknowncheats.me/forum/rust/) - Everything else
