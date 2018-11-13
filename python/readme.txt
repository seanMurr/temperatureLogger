Python requires the 'requests' library http://docs.python-requests.org
requires pipenv dependency manager

pipenv installation guide
-check python3 3 is installed
- $ python3 --version

-check pip is installed
- $ pip --version

-install pipenv
 - $ pip install --user pipenv

-add ~/.local/bin to user PATH in ~/.profile
 - $ nano ~/.profile
 - add the following line to end of profile
 - PATH="$PATH:/home/pi/.local/bin"
 - save and exit nano

-restart .profile
 - $ source ~/.profile

-upgrade pipenv (at any time)
 - $ pip install --user --upgrade pipenv

-install 'requests' package
 - $ cd my/project/directory
 - $ pipenv install requests
