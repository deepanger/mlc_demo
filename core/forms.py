from django import forms
import re
from .models import BaseModel

class RunIdForm(forms.Form):
    base_model = forms.ModelChoiceField(
        queryset=BaseModel.objects.all(),
        label="Base Model",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    run_ids = forms.CharField(
        label="Run IDs",
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter one or more run_ids, separated by commas (must start with letter)'
        }),
        help_text="e.g., run_123,test_456 (run_id must start with a letter)"
    )

    def clean_run_ids(self):
        run_ids_str = self.cleaned_data['run_ids']
        run_ids = [r.strip() for r in run_ids_str.split(',') if r.strip()]

        # Validate each run_id format (must start with letter)
        pattern = re.compile(r'^[a-zA-Z][a-zA-Z0-9_]*$')
        invalid_ids = []

        for run_id in run_ids:
            if not pattern.match(run_id):
                invalid_ids.append(run_id)

        if invalid_ids:
            raise forms.ValidationError(
                f"Invalid run_id format: {', '.join(invalid_ids)}. "
                "Run IDs must start with a letter and contain only letters, numbers, and underscores."
            )

        return run_ids
