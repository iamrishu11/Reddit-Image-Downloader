# Reddit Image Downloader

A Python package for downloading images from Reddit posts and comments. This tool fetches images from a given Reddit post URL and stores them in a ZIP archive.

## Features

- Downloads images from Reddit comments.
- Handles images from both top-level comments and nested replies.
- Provides a progress spinner during the download process.
- Configurable via a `config.json` file.

## Installation

To install the package, clone the repository and use pip to install the dependencies:

```bash
git clone https://github.com/iamrishu11/Reddit-Image-Downloader.git
cd reddit-image-downloader
pip install -r requirements.txt
```

Alternatively, you can install the package directly from PyPI:

```bash
pip install reddit-image-downloader
```

## Configuration

Create a config.json file in the project root directory with the following structure:

```json
{
  "REDDIT_CLIENT_ID": "your_client_id",
  "REDDIT_SECRET": "your_client_secret",
  "REDDIT_USER_AGENT": "your_user_agent"
}
```
Replace the placeholders with your Reddit API credentials.

## Project directory

This is how your project directory should look like.

```plaintext
Reddit-Image-Downloader/
│
├── reddit_image_downloader/
│   ├── __init__.py
│   ├── main.py
│   └── spinner.py
│   
├── tests/
│   └── test_main.py
│
├── .gitignore
├── LICENSE
├── MANIFEST.in
├── README.md
├── requirements.txt
├── images.zip             # Created at Runtime
├── setup.py
└── config.json
```

## Usage

You can use the package either as a command-line tool or import it into your Python scripts.

### Command line tool

Run the following command to start downloading images from a Reddit post:

```bash
python -m reddit_image_downloader.main
```

You will be prompted to enter the Reddit post URL. The images will be saved to images.zip.

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

## Testing

```bash
python -m unittest discover -s tests
```

This will run all test cases defined in the tests directory.

## Use cases

1. **Archiving Reddit Media:** If you are archiving images from a particular Reddit post or thread for research or personal collection, this script automates the process, saving time and effort.

2. **Content Analysis:** Researchers or analysts might need to collect images from Reddit for analyzing content trends or for training machine learning models.

3. **Backup:** Users who want to back up images from interesting Reddit threads can use this script to download and store them conveniently.

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