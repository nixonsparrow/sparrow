from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from streams import blocks


class FlexPage(Page):

    template = 'flex/flex_page.html'

    subtitle = models.CharField(max_length=100, null=True, blank=True)

    content = StreamField(
        [
            ('title_and_text', blocks.TitleAndTextBlock())
        ],
        null=True,
        blank=True,
        # name='title_and_text'
    )

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        StreamFieldPanel('content'),
    ]

    class Meta:
        verbose_name = 'Flex Page'
        verbose_name_plural = 'Flex Pages'
