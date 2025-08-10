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

    # Create multiple base models
    base_models_data = [
        {
            'name': "AML_Model_v3",
            'description': "Anti-Money Laundering Model Version 3"
        },
        {
            'name': "AML_Model_v4",
            'description': "Anti-Money Laundering Model Version 4 - Enhanced"
        },
        {
            'name': "Fraud_Detection_v2",
            'description': "Fraud Detection Model Version 2"
        }
    ]

    base_models = []
    for model_data in base_models_data:
        base_model, created = BaseModel.objects.get_or_create(
            name=model_data['name'],
            defaults={'description': model_data['description']}
        )
        base_models.append(base_model)

        if created:
            print(f"Created base model: {base_model.name}")
        else:
            print(f"Base model already exists: {base_model.name}")

    # Create sample analysis runs for each model
    sample_runs_data = {
        "AML_Model_v3": [
            "aml_2025_001",
            "aml_2025_002",
            "aml_2025_003",
            "test_aml_jan",
            "prod_run_001",
        ],
        "AML_Model_v4": [
            "enhanced_2025_001",
            "enhanced_2025_002",
            "validation_run_001",
            "performance_test_v4",
        ],
        "Fraud_Detection_v2": [
            "fraud_det_001",
            "fraud_det_002",
            "fraud_validation_001",
            "production_fraud_v2",
        ]
    }

    for model in base_models:
        if model.name in sample_runs_data:
            for i, run_id in enumerate(sample_runs_data[model.name]):
                run, created = AnalysisRun.objects.get_or_create(
                    base_model=model,
                    run_id=run_id,
                    defaults={
                        'month': f'2025-0{(i % 9) + 1}',
                        'customer_count': 10000 + (i * 1500)
                    }
                )

                if created:
                    print(f"Created analysis run: {run.run_id} for {model.name}")
                else:
                    print(f"Analysis run already exists: {run.run_id} for {model.name}")

if __name__ == '__main__':
    create_sample_data()
    print("Sample data creation completed!")