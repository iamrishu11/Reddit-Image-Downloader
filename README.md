# Reddit Image Downloader

[![Downloads](https://img.shields.io/pypi/dm/reddit-image-downloader)](https://pypi.org/project/reddit-image-downloader/)
A Python package for downloading images from Reddit posts and comments. This tool fetches images from a given Reddit post URL and stores them in a ZIP archive.

## Features

- Downloads images from Reddit comments.
- Handles images from both top-level comments and nested replies.
- Provides a progress spinner during the download process.
- Configurable via a `config.json` file.

## Installation

You can install the package directly from PyPI:

```bash
pip install reddit-image-downloader
```

## Configuration

The package comes with a pre-configured config.json file that is included in the distribution. This file contains default Reddit API credentials which are used when the package is executed. To use these default credentials, you don’t need to create a separate config.json.

If you need to use different credentials or override the default configuration, you can create your own config.json in the same directory where the script is executed, with the following structure:Create a config.json file in the project root directory with the following structure:

```json
{
  "REDDIT_CLIENT_ID": "your_client_id",
  "REDDIT_SECRET": "your_client_secret",
  "REDDIT_USER_AGENT": "your_user_agent"
}
```
Replace the placeholders with your Reddit API credentials.

<div style="border-left: 3px solid black; background-color: #f9f9f9; padding: 10px;">
    <strong>Note:</strong> Although this package includes default API credentials,it's a good practice to provide your own configuration file for personal use to avoid exposing the default credentials.
</div>


## Project directory

This is how your project directory should look like.

```plaintext
Reddit-Image-Downloader/
│
├── reddit_image_downloader/
│   ├── __init__.py
│   ├── cli.py
│   ├── main.py
│   ├── spinner.py
│   └── config.json
│   
├── tests/
│   ├── __init__.py
│   └── package-test.py
│   └── test_main.py 
│
├── .gitignore
├── LICENSE
├── MANIFEST.in
├── package.md
├── README.md
├── requirements.txt
├── images.zip             # Created at Runtime
└── setup.py
```

## Usage

You can use the package either as a command-line tool or import it into your Python scripts.

### Command line tool

- To get help and see the available options:
```bash
reddit_image_downloader --help 
```

- To check the version of the installed package
```bash
reddit_image_downloader --version
```

- To check information about author and code
```bash
reddit_image_downloader --author
```

- To run the tool interactively and be prompted for a Reddit post URL and output ZIP file name:
```bash
reddit_image_downloader --run
```

- To download images from a Reddit post directly by providing the post URL and the name of the output ZIP file:
```bash
reddit_image_downloader "https://www.reddit.com/r/example/comments/example_post/" "my_images.zip"
```

### Python API

To use the functionality programmatically, import the module and call the download_images_from_post function:

```python
from reddit_image_downloader.main import download_images_from_post

# Example usage
post_url = 'https://www.reddit.com/r/example/comments/example_post/'
output_zip = 'output_images.zip'
config = {
    'REDDIT_CLIENT_ID': 'your_client_id',
    'REDDIT_SECRET': 'your_client_secret',
    'REDDIT_USER_AGENT': 'your_user_agent'
}

download_images_from_post(post_url, output_zip, config)
```

## Use cases

1. **Archiving Reddit Media:** If you are archiving images from a particular Reddit post or thread for research or personal collection, this script automates the process, saving time and effort.

2. **Content Analysis:** Researchers or analysts might need to collect images from Reddit for analyzing content trends or for training machine learning models.

3. **Backup:** Users who want to back up images from interesting Reddit threads can use this script to download and store them conveniently.

## Upcoming Updates

Features which will be added in the upcoming updates

- create a way so that you can download imgaes from n no of post in any subreddit
- update the cli for menu type system
- add a way to get images from share button link

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (git checkout -b feature/your-feature).
3. Commit your changes (git commit -m 'Add new feature').
4. Push to the branch (git push origin feature/your-feature).
5. Open a pull request on GitHub.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [PRAW](https://pypi.org/project/praw/) for interacting with the Reddit API.
- [Requests](https://pypi.org/project/requests/) for handling HTTP requests.
- [TQDM](https://pypi.org/project/tqdm/) for the progress bar
