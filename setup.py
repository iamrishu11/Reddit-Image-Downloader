from setuptools import setup, find_packages

setup(
    name='reddit_image_downloader',  # Replace with your package name
    version='0.1.0',
    description='A tool to download images from Reddit comments and save them into a ZIP file.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Rishank Jain',
    author_email='rishankj749@gmail.com',
    url='https://github.com/yourusername/reddit_image_downloader',  
    packages=find_packages(),
    install_requires=[
        'praw',
        'requests',
        'tqdm',
        'spinner',
        'python-dotenv'
    ],
    entry_points={
        'console_scripts': [
            'reddit_image_downloader=reddit_image_downloader.main:main'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
