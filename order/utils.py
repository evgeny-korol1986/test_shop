import pytz
from datetime import datetime


class ReportFormMixin:
    initial = {
        'start_date': datetime(year=2018, month=1, day=1, tzinfo=pytz.UTC),
        'end_date': datetime(
            year=2018, month=1, day=2, hour=23, minute=59, second=59, microsecond=999999, tzinfo=pytz.UTC),
    }
    form_class = None

    def get_form(self):
        for param in self.initial.keys():
            if param not in self.request.GET:
                return self.form_class(initial=self.initial)
        return self.form_class(data=self.request.GET)

    def get_date_range(self, data):
        return [
            data['start_date'],
            data['end_date'].replace(hour=23, minute=59, second=59, microsecond=999)
        ]

    def get_filter_params(self):
        form = self.get_form()
        if form.is_valid():
            data = {p:form.cleaned_data.get(p) for p in self.initial.keys()}
            return data
        return self.initial

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context
