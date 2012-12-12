from django.contrib.syndication.feeds import Feed
from mysite.books.models import Book
class LatestEntries(Feed):
    title = 'My Blog'
    link = '/archieve/'
    description = 'The latest news about stuff.'

    def items(self):
        return Book.objects.order_by('-publication_date')[:5]
    def item_link(self, item):
        return '/feeds/latest_description.html'

