from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from common.articles.models import Article


class RootView(TemplateView):
    template_name = "common/root.html"

class SlugView(TemplateView):
    template_name = "common/slug.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = kwargs.get('slug')
        article = get_object_or_404(Article, slug=slug)
        context["slug"] = slug
        context["article"] = article
        return context