# Onlyfans downloader

Script to download media and posts from creators on OnlyFans.

<h3>DISCLAIMERS:</h3>
<ul>
    <li>
        This tool is not affiliated, associated, or partnered with OnlyFans in any way. We are not authorized, endorsed, or sponsored by OnlyFans. All OnlyFans trademarks remain the property of Fenix International Limited.
    </li>
    <li>
        This is a theoritical program only and is for educational purposes. If you choose to use it then it may or may not work. You solely accept full responsability and indemnify the creator, hostors, contributors and all other involved persons from any any all responsability.
    </li>
<h3>

## Installation

Install requirement

```bash
    pip install -r requirement.txt
```

## Run Locally

Clone the project

```bash
  python Run.py
```

## Usage/Examples

```python
    [START]
    from Only import Only
    on = Only("creator_name")
    # Only of first launch -> on.make_login()

    [OTHER FUNC]
    on.get_all_post()
    on.get_last_post()
  
    on.get_all_media()
    on.get_last_media()

    on.get_stories()
    on.get_archived()
    on.get_streams()
    on.get_buttons()

```

## Authors

- [@Ghost6446](https://www.github.com/Ghost6446)
