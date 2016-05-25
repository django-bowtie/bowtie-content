import json
from django import forms
from django.forms.widgets import Media
from bowtie_content import custom_blocks_registry
from config import BowtieContentConfig as conf


class BowtieContentWidget(forms.Textarea):

    def __init__(self, *args, **kwargs):

        if 'attrs' not in kwargs:
            kwargs['attrs'] = {}

        class_list = kwargs['attrs'].get('class', '').split()
        class_list.append('js-st-instance')
        kwargs['attrs']['class'] = ' '.join(class_list)

        sirtrevor_conf = {
            'blockTypes': kwargs.pop(
                'st_block_types', conf.BLOCK_TYPES
            ),
            'defaultType': kwargs.pop(
                'st_default_type', conf.DEFAULT_TYPE
            ),
            'blockLimit': kwargs.pop(
                'st_block_limit', conf.BLOCK_LIMIT
            ),
            'blockTypeLimits': kwargs.pop(
                'st_block_type_limits', conf.BLOCK_TYPE_LIMITS
            ),
            'required': kwargs.pop('st_required', conf.REQUIRED),
        }
        kwargs['attrs']['data-sirtrevor-conf'] = json.dumps(sirtrevor_conf)
        super(BowtieContentWidget, self).__init__(*args, **kwargs)

    @property
    def media(self):
        media = Media(css=self.Media.css, js=self.Media.js)
        for name in conf.BLOCK_TYPES:
            if name in custom_blocks_registry:
                block = custom_blocks_registry[name]
                block_media = Media(
                    css=getattr(block.Media, 'css', {}),
                    js=getattr(block.Media, 'js', [])
                )
                media += block_media
        return media

    class Media:
        js = [
            'http://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.4.4/underscore-min.js',
            'http://cdnjs.cloudflare.com/ajax/libs/eventable/1.0.5/eventable.min.js',

            'bowtie-content/components/sir-trevor-js/sir-trevor.js',
            'bowtie-content/init.js',
        ]

        css = {
            'all': [
                'bowtie-content/components/sir-trevor-js/sir-trevor.css'
            ]
        }
