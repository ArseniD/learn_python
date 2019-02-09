import unittest
import os
import tempfile
import io

from html_page import HtmlPagesConverter, FileAccessWrapper, _convert_html


class HtmlPageTest(unittest.TestCase):
    def test_convert_html_helper(self):
        new_text = _convert_html("'plain text'")
        self.assertEqual("&#x27;plain text&#x27;<br />", new_text)

    def test_inserts_br_tags_for_linebreaks(self):
        converter = HtmlPagesConverter(FakeFileWrapper("plain text\n"))
        new_text = converter.get_html_page(0)
        self.assertEqual("plain text<br />", new_text)

    def test_qoutes_escaped(self):
        converter = HtmlPagesConverter(FakeFileWrapper("text with 'quotes'"))
        new_text = converter.get_html_page(0)
        self.assertEqual("text with &#x27;quotes&#x27;<br />", new_text)

    def test_random_access_pages(self):
        converter = HtmlPagesConverter(FakeFileWrapper("page one\nPAGE_BREAK\npage two\nPAGE_BREAK"))
        page_two = converter.get_html_page(1)
        self.assertEqual("page two<br />", page_two)


class FakeFileWrapper:
    def __init__(self, text):
        self.text = text

    def open(self):
        return io.StringIO(self.text)
