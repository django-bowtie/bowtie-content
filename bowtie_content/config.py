from django.apps import AppConfig


class BowtieContentConfig(AppConfig):

    label = 'bowtie-content'

    name = 'bowtie_content'
    verbose_name = 'bowtie_content'

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

