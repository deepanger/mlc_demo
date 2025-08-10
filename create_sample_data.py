#!/usr/bin/env python
"""
Script to create sample data for the MLC demo
"""
import os
import sys
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mlc_center.settings')
django.setup()

from core.models import BaseModel, AnalysisRun

def create_sample_data():
    """Create sample base models and analysis runs"""

    # Create base models if they don't exist
    base_model, created = BaseModel.objects.get_or_create(
        name="AML_Model_v3",
        defaults={
            'description': "Anti-Money Laundering Model Version 3"
        }
    )

    if created:
        print(f"Created base model: {base_model.name}")
    else:
        print(f"Base model already exists: {base_model.name}")

    # Create sample analysis runs
    sample_runs = [
        "run_2025_001",
        "run_2025_002",
        "run_2025_003",
        "run_2025_004",
        "run_2025_005",
        "run_2024_12_final",
        "run_test_001"
    ]

    for i, run_id in enumerate(sample_runs):
        run, created = AnalysisRun.objects.get_or_create(
            base_model=base_model,
            run_id=run_id,
            defaults={
                'month': f'2025-0{(i % 9) + 1}',
                'customer_count': 10000 + (i * 1500)
            }
        )

        if created:
            print(f"Created analysis run: {run.run_id}")
        else:
            print(f"Analysis run already exists: {run.run_id}")

if __name__ == '__main__':
    create_sample_data()
    print("Sample data creation completed!")
