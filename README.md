# BHDump
Python project that dump any ios application (IPA), based in [flexdecrypt](https://github.com/JohnCoates/flexdecrypt).

# Installation:
## automatic:
  - atfer downloading/clone this repo run 'install.sh' with Terminal/Newterm:
  ```shell
  cd {BHDump project path}
  ./install.sh
  ```
## manually:
  - **Create Folder in /var/mobile/Documents with this name (Apps) and inside it make another folder with name (Payload)**.
  - download libswift & libswift (stable).
  - download Python 3.7 & curl & wget from [sam repo](https://apt.bingner.com/).
  - installing pip:
  ```shell
  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
  python3 ./get-pip.py
  ```
  - install the requirements of BHDump project with pip:
  ```shell
  pip3 install color-it
  ```
  - Finally, download lasted version of flexdecrypt.deb from https://github.com/JohnCoates/flexdecrypt/releases and install it.
  
  # How to use:
  - First, you need to get .app path of application from filza, and open Terminal/Newterm, locate project path with cd and use BHDump like that:
  ```shell
  cd {BHDump project path}
  python3 app.py -p {.app path}
  ```
  - Finally, the IPA will produce in this path /var/mobile/Documents/Apps **(if this path not exists BHDump will not save IPA)**.
  ## example:
  ```shell
  cd /var/mobile/Documents/BHDump
  python3 app.py -p /var/containers/Bundle/Application/19C239DA-BC21-4335-9891-F368D6E51327/BbStudent.app
  ```
  
  # note:
  - By default, BHDump will produce IPA with **iOS 12 Minimum Version** of you want change that open [application.py](https://github.com/BandarHL/BHDump/blob/master/application.py#L49) and on line 49 change 12 with any version you want **(but that not mean the IPA will work with this version)**.
