from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.prediction_info_view, name='prediction_info'),
    path('transaction-analysis/', views.transaction_analysis_view, name='transaction_analysis'),
    path('target-analysis/', views.target_analysis_view, name='target_analysis'),
    path('model-proving/', views.model_proving_view, name='model_proving'),
    path('forecasting/', views.forecasting_view, name='forecasting'),
    path('btl-analysis/', views.btl_analysis_view, name='btl_analysis'),
    path('benchmark/', views.benchmark_view, name='benchmark'),
    path('documentation-helper/', views.documentation_helper_view, name='documentation_helper'),
    # HTMX-specific URLs can be added here
    path('htmx/load-run-details/', views.load_run_details_view, name='load_run_details'),
]
