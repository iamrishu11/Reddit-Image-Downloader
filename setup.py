from setuptools import setup, find_packages

setup(
    name='reddit_image_downloader',
    version='0.1.5', 
    description='A tool to download images from Reddit posts and comments and save them into a ZIP file.',
    long_description=open('setup.md').read(),
    long_description_content_type='text/markdown',
    author='Rishank Jain',
    author_email='rishankj749@gmail.com',
    license='MIT',
    url='https://github.com/iamrishu11/Reddit-Image-Downloader',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'reddit_image_downloader': ['config.json'],
    },
    install_requires=[
        'praw>=7.7.1',
        'requests>=2.28.2',
        'tqdm>=4.65.0',
        'setuptools'
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
