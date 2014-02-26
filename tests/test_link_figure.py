# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import sys
import unittest

sys.path.append(os.path.join('plugins', 'link_figure'))

from nikola.utils import LOGGER
import logbook

from .test_rst_compiler import ReSTExtensionTestCase


class TestLinkFigure(ReSTExtensionTestCase):
    @staticmethod
    def setUpClass():
        LOGGER.notice('--- TESTS FOR link_figure')
        LOGGER.level = logbook.WARNING

    @staticmethod
    def tearDownClass():
        sys.stdout.write('\n')
        LOGGER.level = logbook.NOTICE
        LOGGER.notice('--- END OF TESTS FOR link_figure')

    def test_default(self):
        # the result should be
        # <meta itemprop="datePublished" content="2009-05-08">May 8, 2009
        expected = (
            '<a class=""href="http://getnikola.com/"title="getnikola.com">getnikola.com</a>'
        )
        self.sample = '.. link_figure:: http://getnikola.com/'
        self.basic_test()
        import pdb; pdb.set_trace()
        self.assertHTMLEqual(expected.strip())

    def test_full(self):
        # the result should be
        # <meta itemprop="datePublished" content="2009-05-08">May 8, 2009
        expected = (
            '<div class="link-figure">'
            '<div class="link-figure-media">'
            '<a class="link-figure-image" href="http://getnikola.com/" target="_blank">'
            '<img src="http://getnikola.com/galleries/demo/tesla2_lg.jpg" alt="Nikola | Nikola" />'
            '</a></div><div class="link-figure-content">'
            '<a class="link-figure-title" href="http://getnikola.com/" target="_blank">Nikola | Nikola</a>'
            '<p class="link-figure-description">In goes content, out comes a website, ready to deploy.</p>'
            '<p class="link-figure-author">@ <a href="http://ralsina.me/" target="_blank">Roberto Alsina</a>'
            '</p></div></div>'
        )
        self.sample = """.. link_figure:: http://getnikola.com/
            :title: Nikola | Nikola
            :description: In goes content, out comes a website, ready to deploy.
            :class: link-figure
            :image_url: http://getnikola.com/galleries/demo/tesla2_lg.jpg
            :author: Roberto Alsina
            :author_url: http://ralsina.me/
        """
        self.basic_test()
        import pdb; pdb.set_trace()
        self.assertHTMLEqual(expected.strip())

if __name__ == '__main__':
    unittest.main()
