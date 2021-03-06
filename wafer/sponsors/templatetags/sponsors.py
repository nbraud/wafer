from django import template

from wafer.sponsors.models import Sponsor, SponsorshipPackage

register = template.Library()


@register.inclusion_tag('wafer.sponsors/sponsors_block.html')
def sponsors():
    return {
        'sponsors': Sponsor.objects.all().order_by('packages', 'order', 'id'),
        'packages': SponsorshipPackage.objects.all().prefetch_related('files'),
    }


@register.simple_tag()
def sponsor_image_url(sponsor, name):
    """Returns the corresponding url from the sponsors images"""
    if sponsor.files.filter(name=name).exists():
        # We avoid worrying about multiple matches by always
        # returning the first one.
        return sponsor.files.filter(name=name).first().item.url
    return ''
