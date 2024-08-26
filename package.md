## Testing package locally 

1. Delete previous builds, if any

This removes any previous build artifacts to ensure that your new build is clean.

```bash
rm -rf build dist *.egg-info
```

2. Build the Package

```bash
python setup.py sdist bdist_wheel
```

This command generates distribution files (.tar.gz and .whl files) in the dist/ directory..

3. Install the Package Locally:

```bash
pip install .
```

4. Test the Command-Line Tool:

```bash
reddit_image_downloader --help
```

5. Run Your Tests: 
Ensure all your unit tests pass to verify everything works correctly:

```bash
python -m unittest discover
```

## 2. Publish Your Package

To publish your package on PyPI (Python Package Index), follow these steps:

1. Create a PyPI Account: If you don’t have a PyPI account, you need to create one at PyPI.

2. Install twine: twine is a utility to securely upload your package to PyPI.

```bash
pip install twine
```

3. Upload the Package: Use twine to upload the package to PyPI.

```bash
twine upload dist/*
```
You’ll be prompted to enter your PyPI username and password.

## Verify Installation from PyPI
After publishing, you should verify the installation from PyPI to ensure it works as expected.

1. Uninstall the Local Version:

```bash
pip uninstall reddit_image_downloader
```

2. Install the Package from PyPI:

```bash
pip install reddit_image_downloader
```

3. Test the command-line tool again:

```bash
reddit_image_downloader --help
```