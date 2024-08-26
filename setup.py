from setuptools import setup, find_packages

setup(
    name='reddit_image_downloader',
    version='0.1.2', 
    description='A tool to download images from Reddit posts and comments and save them into a ZIP file.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Rishank Jain',
    author_email='rishankj749@gmail.com',
    url='https://github.com/iamrishu11/Reddit-Image-Downloader',
    packages=find_packages(),
    install_requires=[
        'praw==7.7.1',
        'requests==2.28.2',
        'tqdm==4.65.0',
    ],
    entry_points={
        'console_scripts': [
            'reddit_image_downloader=reddit_image_downloader.cli:main'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
