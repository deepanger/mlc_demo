from django import forms

class RunIdForm(forms.Form):
    run_ids = forms.CharField(
        label="Run IDs",
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter one or more run_ids, separated by commas'
        }),
        help_text="e.g., run_123,run_456"
    )
