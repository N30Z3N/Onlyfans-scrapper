<p align="center">
	<img src="Only/assets/min_logo.png" style="max-width: 55%;" alt="video working" />
</p>

# Onlyfans downloader

Script to download media and posts from creators on OnlyFans (no payment media if not subscribe).

<p align="center">
	<img src="Only/assets/run.gif" style="max-width: 55%;" alt="video working" />
</p>

<h3>DISCLAIMERS:</h3>
<ul>
    <li>
        This tool is not affiliated, associated, or partnered with OnlyFans in any way. We are not authorized, endorsed, or sponsored by OnlyFans. All OnlyFans trademarks remain the property of Fenix International Limited.
    </li>
    <li>
        This is a theoritical program only and is for educational purposes. If you choose to use it then it may or may not work. You solely accept full responsability and indemnify the creator, hostors, contributors and all other involved persons from any any all responsability.
    </li>
<h3>

## Requirement

* python [3.9](https://www.python.org/downloads/release/python-390/)
* openssl [site](https://slproweb.com/products/Win32OpenSSL.html)

## Installation for WIN

* requirement for library of python

```bash
	pip install -r requirement.txt
```

## Features

* get all_post()
* get_last_post()
* get_all_media()
* get_last_media()
* get_stories()
* get_archived()
* get_streams()
* get_chat()                  #NEW
* get_buttons()               #NEW
* click_on_subscrive()        #NEW
* get_profile_photo()         #NEW
* get_avatar_photo()          #NEW


## ERROR [NO MEDIA]
TO FIX NOT ALL MEDIA FIND: go to util\api.py find function "scroll_to_end" and change variable "sleep_load" until he can get to the bottom of the page, after that go to only.py and change driver.create(False) to driver.create (True) to remove headless of browser to test it and see what it do.


## Old tutorial not valid
https://www.youtube.com/watch?v=e6h13W3mVhA&t=48s

## Authors

- [@Ghost6446](https://www.github.com/Ghost6446)
