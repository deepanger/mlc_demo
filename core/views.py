from django.shortcuts import render
from .models import BaseModel, AnalysisRun
from .forms import RunIdForm
import random

def prediction_info_view(request):
    form = RunIdForm()
    base_models = BaseModel.objects.all()
    
    # Mock logic to handle form submission via HTMX
    if request.htmx:
        run_ids_str = request.POST.get('run_ids', '')
        run_ids = [r.strip() for r in run_ids_str.split(',') if r.strip()]
        
        # For demo, we'll just pick the first base model
        base_model = base_models.first()
        
        runs_with_details = []
        for run_id in run_ids:
            run, created = AnalysisRun.objects.get_or_create(
                base_model=base_model,
                run_id=run_id,
                defaults={
                    'month': f'2025-0{random.randint(1,9)}',
                    'customer_count': random.randint(5000, 20000)
                }
            )
            
            # Mock table availability
            all_tables = ['transactions', 'customer_profiles', 'alerts', 'sar_filings']
            available_tables = random.sample(all_tables, random.randint(2, 4))
            
            runs_with_details.append({
                'run': run,
                'tables': [{'name': t, 'available': t in available_tables} for t in all_tables]
            })

        return render(request, 'core/partials/run_details.html', {'runs_with_details': runs_with_details})

    context = {
        'base_models': base_models,
        'selected_model_id': base_models.first().id if base_models else None,
        'form': form,
    }
    return render(request, 'core/prediction_info.html', context)

def transaction_analysis_view(request):
    base_models = BaseModel.objects.all()
    context = {
        'base_models': base_models,
        'selected_model_id': base_models.first().id if base_models else None,
    }
    return render(request, 'core/transaction_analysis.html', context)

def target_analysis_view(request):
    base_models = BaseModel.objects.all()
    context = {
        'base_models': base_models,
        'selected_model_id': base_models.first().id if base_models else None,
    }
    return render(request, 'core/target_analysis.html', context)

def model_proving_view(request):
    base_models = BaseModel.objects.all()
    context = {
        'base_models': base_models,
        'selected_model_id': base_models.first().id if base_models else None,
    }
    return render(request, 'core/model_proving.html', context)

def forecasting_view(request):
    base_models = BaseModel.objects.all()
    context = {
        'base_models': base_models,
        'selected_model_id': base_models.first().id if base_models else None,
    }
    return render(request, 'core/forecasting.html', context)

def load_run_details_view(request):
    # This view is now handled inside prediction_info_view with request.htmx
    pass
