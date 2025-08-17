from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    # Landing page (no sidebar)
    path('', views.home_view, name='home'),

    # Country-specific routes (with sidebar)
    path('<slug:country_code>/timeline/', views.country_timeline_view, name='timeline'),
    path('<slug:country_code>/retrain/', views.country_retrain_view, name='country_retrain'),

    # Feature pages per country
    path('<slug:country_code>/prediction-info/', views.prediction_info_view, name='prediction_info'),
    path('<slug:country_code>/transaction-analysis/', views.transaction_analysis_view, name='transaction_analysis'),
    path('<slug:country_code>/target-analysis/', views.target_analysis_view, name='target_analysis'),
    path('<slug:country_code>/model-proving/', views.model_proving_view, name='model_proving'),
    path('<slug:country_code>/forecasting/', views.forecasting_view, name='forecasting'),
    path('<slug:country_code>/btl-analysis/', views.btl_analysis_view, name='btl_analysis'),
    path('<slug:country_code>/benchmark/', views.benchmark_view, name='benchmark'),
    path('<slug:country_code>/documentation-helper/', views.documentation_helper_view, name='documentation_helper'),

    # HTMX-specific URLs can be added here
    path('htmx/load-run-details/', views.load_run_details_view, name='load_run_details'),
]
