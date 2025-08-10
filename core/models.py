from django.db import models

class BaseModel(models.Model):
    """
    Represents a base model, for example 'AML_Model_v3'.
    """
    name = models.CharField(max_length=100, unique=True, help_text="The name of the base model")
    description = models.TextField(blank=True, null=True, help_text="A brief description of the model")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class AnalysisRun(models.Model):
    """
    Stores a user-entered run_id and its associated base model.
    A run_id corresponds to one analysis session.
    """
    base_model = models.ForeignKey(BaseModel, on_delete=models.CASCADE, related_name="runs")
    run_id = models.CharField(max_length=255, help_text="The user-entered run_id")
    # Store some mock metadata
    month = models.CharField(max_length=20, default="2025-07")
    customer_count = models.IntegerField(default=10000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('base_model', 'run_id') # run_id is unique for a given model

    def __str__(self):
        return f"{self.run_id} for {self.base_model.name}"