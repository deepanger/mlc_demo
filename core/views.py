from django.shortcuts import render
from django.contrib import messages
from .models import BaseModel, AnalysisRun
from .forms import RunIdForm
from .analysis_utils import generate_transaction_analysis, generate_target_analysis
import random
import re

def prediction_info_view(request):
    base_models = BaseModel.objects.all()

    # Get selected base model from request or default to first
    selected_model_id = request.GET.get('base_model') or request.POST.get('base_model')
    if selected_model_id:
        try:
            selected_model = BaseModel.objects.get(id=selected_model_id)
        except BaseModel.DoesNotExist:
            selected_model = base_models.first()
    else:
        selected_model = base_models.first()

    form = RunIdForm(initial={'base_model': selected_model})

    # Auto-display recent 5 runs for selected model when page loads
    recent_runs = AnalysisRun.objects.filter(base_model=selected_model).order_by('-created_at')[:5]
    runs_with_details = []

    for run in recent_runs:
        # Mock table availability
        all_tables = ['transactions', 'customer_profiles', 'alerts', 'sar_filings']
        available_tables = random.sample(all_tables, random.randint(2, 4))

        runs_with_details.append({
            'run': run,
            'tables': [{'name': t, 'available': t in available_tables} for t in all_tables]
        })

    # Handle form submission
    if request.method == 'POST':
        form = RunIdForm(request.POST)
        if form.is_valid():
            base_model = form.cleaned_data['base_model']
            run_ids = form.cleaned_data['run_ids']

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

            if request.headers.get('HX-Request'):
                return render(request, 'core/partials/run_details.html', {'runs_with_details': runs_with_details})
        else:
            # Form has validation errors
            if request.headers.get('HX-Request'):
                return render(request, 'core/partials/form_errors.html', {'form': form})

    context = {
        'base_models': base_models,
        'selected_model_id': selected_model.id if selected_model else None,
        'form': form,
        'recent_runs_with_details': runs_with_details,
    }
    return render(request, 'core/prediction_info.html', context)

def transaction_analysis_view(request):
    base_models = BaseModel.objects.all()

    # Get selected base model from request
    selected_model_id = request.GET.get('base_model')
    if selected_model_id:
        try:
            selected_model = BaseModel.objects.get(id=selected_model_id)
        except BaseModel.DoesNotExist:
            selected_model = base_models.first()
    else:
        selected_model = base_models.first()

    # Get run IDs for selected base model only
    run_objs = AnalysisRun.objects.filter(base_model=selected_model).order_by('run_id')

    # Check for selected run_id from query parameters
    selected_run = request.GET.get('run_id')

    # Generate analysis data if run_id is selected
    df_html = None
    chart_data = None
    if selected_run:
        # Verify that the run_id belongs to the selected model
        if run_objs.filter(run_id=selected_run).exists():
            df_html, chart_data = generate_transaction_analysis(selected_run)
        else:
            selected_run = None  # Invalid run_id for this model

    context = {
        'base_models': base_models,
        'selected_model_id': selected_model.id if selected_model else None,
        'run_ids': run_objs,
        'selected_run_id': selected_run,
        'df_html': df_html,
        'chart_data': chart_data,
    }
    return render(request, 'core/transaction_analysis.html', context)

def target_analysis_view(request):
    base_models = BaseModel.objects.all()

    # Get selected base model from request
    selected_model_id = request.GET.get('base_model')
    if selected_model_id:
        try:
            selected_model = BaseModel.objects.get(id=selected_model_id)
        except BaseModel.DoesNotExist:
            selected_model = base_models.first()
    else:
        selected_model = base_models.first()

    # Get run IDs for selected base model only
    run_objs = AnalysisRun.objects.filter(base_model=selected_model).order_by('run_id')

    # Check for selected run_id from query parameters
    selected_run = request.GET.get('run_id')

    # Generate analysis data if run_id is selected
    df_html = None
    chart_data = None
    if selected_run:
        # Verify that the run_id belongs to the selected model
        if run_objs.filter(run_id=selected_run).exists():
            df_html, chart_data = generate_target_analysis(selected_run)
        else:
            selected_run = None  # Invalid run_id for this model

    context = {
        'base_models': base_models,
        'selected_model_id': selected_model.id if selected_model else None,
        'run_ids': run_objs,
        'selected_run_id': selected_run,
        'df_html': df_html,
        'chart_data': chart_data,
    }
    return render(request, 'core/target_analysis.html', context)

def model_proving_view(request):
    base_models = BaseModel.objects.all()
    
    # Get selected base model from request or default to first
    selected_model_id = request.GET.get('base_model')
    if selected_model_id:
        try:
            selected_model = BaseModel.objects.get(id=selected_model_id)
        except BaseModel.DoesNotExist:
            selected_model = base_models.first()
    else:
        selected_model = base_models.first()
    
    context = {
        'base_models': base_models,
        'selected_model_id': selected_model.id if selected_model else None,
    }
    return render(request, 'core/model_proving.html', context)

def forecasting_view(request):
    base_models = BaseModel.objects.all()
    
    # Get selected base model from request or default to first
    selected_model_id = request.GET.get('base_model')
    if selected_model_id:
        try:
            selected_model = BaseModel.objects.get(id=selected_model_id)
        except BaseModel.DoesNotExist:
            selected_model = base_models.first()
    else:
        selected_model = base_models.first()
    
    context = {
        'base_models': base_models,
        'selected_model_id': selected_model.id if selected_model else None,
    }
    return render(request, 'core/forecasting.html', context)

def btl_analysis_view(request):
    base_models = BaseModel.objects.all()
    
    # Get selected base model from request or default to first
    selected_model_id = request.GET.get('base_model')
    if selected_model_id:
        try:
            selected_model = BaseModel.objects.get(id=selected_model_id)
        except BaseModel.DoesNotExist:
            selected_model = base_models.first()
    else:
        selected_model = base_models.first()
    
    context = {
        'base_models': base_models,
        'selected_model_id': selected_model.id if selected_model else None,
    }
    return render(request, 'core/btl_analysis.html', context)

def benchmark_view(request):
    base_models = BaseModel.objects.all()
    
    # Get selected base model from request or default to first
    selected_model_id = request.GET.get('base_model')
    if selected_model_id:
        try:
            selected_model = BaseModel.objects.get(id=selected_model_id)
        except BaseModel.DoesNotExist:
            selected_model = base_models.first()
    else:
        selected_model = base_models.first()
    
    # Get runs for selected model for the benchmark dropdown
    runs = AnalysisRun.objects.filter(base_model=selected_model).order_by('-created_at')
    
    context = {
        'base_models': base_models,
        'selected_model_id': selected_model.id if selected_model else None,
        'runs': runs,
    }
    return render(request, 'core/benchmark.html', context)

def documentation_helper_view(request):
    base_models = BaseModel.objects.all()
    
    # Get selected base model from request or default to first
    selected_model_id = request.GET.get('base_model')
    if selected_model_id:
        try:
            selected_model = BaseModel.objects.get(id=selected_model_id)
        except BaseModel.DoesNotExist:
            selected_model = base_models.first()
    else:
        selected_model = base_models.first()
    
    context = {
        'base_models': base_models,
        'selected_model_id': selected_model.id if selected_model else None,
    }
    return render(request, 'core/documentation_helper.html', context)

def load_run_details_view(request):
    # This view is now handled inside prediction_info_view with request.htmx
    pass
