# Copyright 2011 by Ozan Onay.
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#   http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from hashlib import md5
import os
import re
import string
import urllib


URL_RE = re.compile('http(s)?\://([\w\.-]*)(\:(\d+))?(/.*)?')


class Slide(object):
    """A slide in a grunt presentation"""
    
    url = ''
    content = ''
    
    def __init__(self, raw_content):
        self._raw_content = raw_content
        self.url = self._extract_url()
        self.content = self._extract_content()
        self.slide_id = self._generate_html_id()
        self.slide_class = 'dark' if self.url else 'light'
        if not self.content:
            self.slide_class += ' empty'
    
    def _extract_content(self):
        """Extract content from raw slide definition"""
        if self.url:
            return self._raw_content.replace(self.url, '').strip()
        return self._raw_content
    
    def _generate_html_id(self):
        """Generate a url-safe generator from the slide title"""
        content = re.sub(r'[^\w^\s]', '', self.content.lower())
        html_id = '-'.join(content.split(' ')[:5])
        # Prepend a digest string, as there is no guarantee that
        # the content of two slides will be unique
        md5_hash = md5(self._raw_content.encode('ascii', 'ignore'))
        html_id = 'slide-%s-%s' % (md5_hash.hexdigest()[:5], 
                                   urllib.quote(html_id))
        return html_id
    
    def _extract_url(self):
        """Extract url from raw slide definition, if any"""
        match = URL_RE.search(self._raw_content)
        if match:
            return match.group()
        return None


def parse_slides(text):
    """Givin a string, return a list of parsed grunt slides"""
    return [Slide(s) for s in text.splitlines() if s]

