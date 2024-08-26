import argparse
from .main import download_images_from_post, load_config

def main():
    parser = argparse.ArgumentParser(
        description="A command-line tool to download images from Reddit posts and save them into a ZIP file."
    )
    subparsers = parser.add_subparsers(dest='command')

    # Subparser for the download command
    download_parser = subparsers.add_parser('download', help='Download images from a Reddit post')
    download_parser.add_argument('post_url', help="URL of the Reddit post from which to download images.")
    download_parser.add_argument('--config', default='reddit_image_downloader/config.json', help="Path to the configuration file (default: reddit_image_downloader/config.json).")
    download_parser.add_argument('--output', default='images.zip', help="Path to the output ZIP file (default: images.zip).")

    # Subparser for the help command
    help_parser = subparsers.add_parser('help', help='Show help message')

    args = parser.parse_args()

    if args.command == 'download':
        config_path = args.config
        output_zip = args.output
        post_url = args.post_url

        config = load_config(config_path)
        download_images_from_post(post_url, output_zip, config)
    elif args.command == 'help':
        parser.print_help()
    else:
        parser.print_help()
