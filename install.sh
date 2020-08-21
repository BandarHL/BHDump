apt-get update
if ($( python3 --version > /dev/null )); then
  apt-get install wget org.swift.libswift com.modmyi.libswift4 curl
else
  apt-get install wget org.swift.libswift com.modmyi.libswift4 python3.7 curl
fi

if ($( pip3 --version > /dev/null )) ; then
 pip3 install color-it
else
  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
  python3 ./get-pip.py
  rm ./get-pip.py
  pip3 install color-it
fi


wget https://github.com/JohnCoates/.
flexdecrypt/releases/download/1.1/flexdecrypt.deb
dpkg -i ./flexdecrypt.deb
rm ./flexdecrypt.deb