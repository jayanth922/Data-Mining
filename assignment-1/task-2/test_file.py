import unittest
from tkinter import Tk, Text
from file import update_preview

class TestMarkdownPreviewer(unittest.TestCase):

    def setUp(self):
        self.root = Tk()
        self.text = Text(self.root)
        self.preview = Text(self.root, state="disabled")
        self.text.insert("1.0", "# Hello World")
        self.text.bind("<<Modified>>", lambda e: update_preview(self.text, self.preview))

    def tearDown(self):
        self.root.destroy()

    def test_update_preview(self):
        update_preview(self.text, self.preview)
        self.preview.configure(state="normal")
        preview_content = self.preview.get("1.0", "end-1c")
        self.preview.configure(state="disabled")
        self.assertIn("<h1>Hello World</h1>", preview_content)

if __name__ == '__main__':
    unittest.main()