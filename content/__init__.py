import json
from django.template.loader import render_to_string
import six

default_app_config = 'content.config.BowtieContentConfig'


class BowtieContent(six.text_type):

    @property
    def html(self):
        html = []
        if len(self):
            content = json.loads(self)
            for block in content['data']:
                template_name = 'bowtie-content/blocks/%s.html' % block['type']
                html.append(render_to_string(template_name, block['data']))
        return u''.join(html)


custom_blocks_registry = {}


def register_block(block, name=None):
    if name is None:
        name = block.name
    custom_blocks_registry[name] = block
