import argparse
import os
from .main import load_config, download_images_from_post

def print_version():
    """Print the current version of the package."""
    # Import the version from setup.py
    from importlib.metadata import version
    package_version = version('reddit-image-downloader')
    print(f"reddit-image-downloader version {package_version}")

def run_interactively():
    """Prompt the user for input and download images."""
    post_url = input("Enter the Reddit post URL: ").strip()
    output_zip = "images.zip"
    
    # Load configuration
    config = load_config()
    
    # Download images from the specified Reddit post and save them to a ZIP file
    download_images_from_post(post_url, output_zip, config)

def main():
    parser = argparse.ArgumentParser(description='Download images from Reddit posts and comments.')
    
    # Define arguments
    parser.add_argument(
        '--run',
        action='store_true',
        help='Interactively prompt for URL and save the output in ZIP .'
    )
    
    parser.add_argument(
        '--version',
        action='store_true',
        help='Show the version of the package.'
    )
    
    parser.add_argument(
        'post_url',
        nargs='?',
        default=None,
        help='URL of the Reddit post. Required if not using --run.'
    )
    
    parser.add_argument(
        'output_zip',
        nargs='?',
        default=None,
        help='Name of the output ZIP file. Required if not using --run.'
    )
    
    args = parser.parse_args()
    
    if args.version:
        print_version()
    elif args.run:
        run_interactively()
    elif args.post_url and args.output_zip:
        # Load configuration
        config = load_config()
        
        # Download images from the specified Reddit post and save them to a ZIP file
        download_images_from_post(args.post_url, args.output_zip, config)
    else:
        parser.print_help()
        exit(1)

if __name__ == '__main__':
    main()
