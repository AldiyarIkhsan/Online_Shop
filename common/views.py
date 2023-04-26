class TitleMixin:
    title = None

    def get_contxt_data(self, **kwargs):
        context = super(TitleMixin, self).get_contxt_data(**kwargs)
        context['title'] = self.title
        return context