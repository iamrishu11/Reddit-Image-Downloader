import unittest
import subprocess
import sys

class TestPackage(unittest.TestCase):
    def test_import(self):
        """Test that the package can be imported."""
        try:
            import reddit_image_downloader
        except ImportError as e:
            self.fail(f"Import failed: {e}")

    def test_command_line_tool(self):
        """Test the command-line tool."""
        result = subprocess.run(
            [sys.executable, '-m', 'reddit_image_downloader', '--help'],
            capture_output=True,
            text=True
        )
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)
        self.assertEqual(result.returncode, 0)


    # Add more tests as needed

if __name__ == '__main__':
    unittest.main()
