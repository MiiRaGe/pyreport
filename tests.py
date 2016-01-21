# coding=utf-8
from unittest import TestCase

from pyreport.reporter import Report


class TestUnicode(TestCase):
    def test_unicode_msg(self):
        report = Report()
        report.create_report()
        report.info(u'ñiet')
        assert report.finalize_report()
