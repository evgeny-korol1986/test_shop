from django import forms


class DateRangeFormMixin(forms.Form):
    start_date = forms.DateTimeField(
        input_formats=['%d.%m.%Y'],
        widget=forms.DateInput(
            format='%d.%m.%Y', attrs={'class': 'form-control'}
        ),
    )
    end_date = forms.DateTimeField(
        input_formats=['%d.%m.%Y'],
        widget=forms.DateInput(
            format='%d.%m.%Y', attrs={'class': 'form-control'}
        ),
    )


class OrderReportForm(DateRangeFormMixin, forms.Form):
    pass


class ProductReportForm(DateRangeFormMixin, forms.Form):
    top = forms.TypedChoiceField(
        choices=((10, 10), (20, 20), (50, 50), (100, 100)),
        widget=forms.Select(attrs={'class': 'form-control'}), coerce=int
    )
