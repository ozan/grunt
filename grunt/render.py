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

from __future__ import with_statement
import codecs
import datetime
from pkg_resources import resource_string
import string
import sys

from parse import parse_slides


BACKGROUND_IMAGE_CSS = '#%(slide_id)s { background-image: url(%(url)s); }'
SECTION_HTML = '''
<section id="%(slide_id)s" class="%(slide_class)s">
    <div>%(content)s</div>
</section>'''


def render(slides):
    """Given an iterable of slides, render the entire slideshow"""
    
    template = string.Template(resource_string(__name__, 'template.html'))
    
    context = {
        'pubdate': datetime.datetime.now().isoformat(),
        'title': slides[0].content,
        'slides': '\n'.join(SECTION_HTML % s.__dict__ for s in slides),
        'backgrounds': '\n'.join(BACKGROUND_IMAGE_CSS % s.__dict__
                                 for s in slides if s.url)}
    
    return template.safe_substitute(context)


def render_from_file(input, output=None, encoding=None):
    """Use grunt to render an HTML5 slideshow from a linebreak-delimited
    file of slides definitions.
    """
    if not encoding:
        encoding = 'utf-8'
        
    with codecs.open(input, encoding=encoding) as f:
        text = f.read()
                
    slides = parse_slides(text)
    result = render(slides)
    
    if output:
        with codecs.open(output, 'w', encoding=encoding) as f:
            f.write(result)
    else:
        sys.stdout.write(result.encode(encoding))


def parse_options():
    from optparse import OptionParser
    
    usage = 'usage: %prog source_file'
    parser = OptionParser(usage="%prog INPUT_FILE [options]")

    parser.add_option('-f', '--file', dest='filename',
                      help='write output to OUTPUT_FILE',
                      metavar="OUTPUT_FILE")
    parser.add_option('-e', '--encoding', dest='encoding', default='utf-8',
                      help='encoding for input and output files')

    (options, args) = parser.parse_args()
    
    if len(args) < 1:
        parser.error('Input file not provided.')
    elif len(args) > 1:
        parser.error('Only one input file may be specified.')
        
    return {'input': args[0],
            'output': options.filename,
            'encoding': options.encoding}
    

def main():
    """Run grunt from the command line"""
    options = parse_options()
    render_from_file(**options)
    
    
if __name__ == '__main__':
    main()
    