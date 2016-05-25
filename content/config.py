from django.apps import AppConfig


class BowtieContentConfig(AppConfig):

    label = 'bowtie-content'

    name = 'content'
    verbose_name = 'content'

    BLOCK_TYPES = [
        'Text',
        'List',
        'Quote',
        'Image',
        'Video',
        'Tweet',
        'Heading'
    ]

    DEFAULT_TYPE = None
    BLOCK_LIMIT = 0
    BLOCK_TYPE_LIMITS = {}
    REQUIRED = []

