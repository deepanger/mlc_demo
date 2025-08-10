import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import numpy as np
import io
import base64
from datetime import datetime, timedelta
import random

def generate_transaction_analysis(run_id):
    """
    Generate mock transaction data and chart for the given run_id
    Returns: (DataFrame as HTML, Base64 encoded chart)
    """
    # Generate mock transaction data
    np.random.seed(hash(run_id) % 2**32)  # Consistent data for same run_id

    # Create date range for last 30 days
    end_date = datetime.now()
    start_date = end_date - timedelta(days=29)
    date_range = pd.date_range(start=start_date, end=end_date, freq='D')

    # Generate transaction data
    data = {
        'Date': date_range,
        'Transaction_Count': np.random.poisson(1500, len(date_range)),
        'Total_Amount': np.random.normal(2500000, 500000, len(date_range)),
        'Suspicious_Count': np.random.poisson(25, len(date_range)),
        'Alert_Rate': np.random.uniform(0.01, 0.05, len(date_range))
    }

    df = pd.DataFrame(data)
    df['Total_Amount'] = np.abs(df['Total_Amount'])  # Ensure positive amounts
    df['Alert_Rate'] = (df['Alert_Rate'] * 100).round(2)  # Convert to percentage

    # Create chart
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

    # Transaction count chart
    ax1.bar(df['Date'], df['Transaction_Count'], alpha=0.7, color='#9A2A2A')
    ax1.set_title(f'Daily Transaction Count - Run ID: {run_id}')
    ax1.set_ylabel('Transaction Count')
    ax1.tick_params(axis='x', rotation=45)

    # Alert rate chart
    ax2.plot(df['Date'], df['Alert_Rate'], marker='o', color='#ff6b6b', linewidth=2)
    ax2.set_title('Daily Alert Rate (%)')
    ax2.set_ylabel('Alert Rate (%)')
    ax2.set_xlabel('Date')
    ax2.tick_params(axis='x', rotation=45)

    plt.tight_layout()

    # Convert chart to base64
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', dpi=150, bbox_inches='tight')
    buffer.seek(0)
    chart_data = base64.b64encode(buffer.read()).decode()
    plt.close()

    # Convert DataFrame to HTML with better formatting
    df_formatted = df.copy()
    df_formatted['Date'] = df_formatted['Date'].dt.strftime('%Y-%m-%d')
    df_formatted['Total_Amount'] = df_formatted['Total_Amount'].apply(lambda x: f"${x:,.0f}")

    df_html = df_formatted.to_html(
        classes='table table-striped table-hover',
        table_id='transaction-table',
        index=False,
        escape=False,
        border=0
    )

    return df_html, chart_data

def generate_target_analysis(run_id):
    """
    Generate mock target data and chart for the given run_id
    Returns: (DataFrame as HTML, Base64 encoded chart)
    """
    # Generate mock target data
    np.random.seed(hash(run_id + "_target") % 2**32)  # Consistent data for same run_id

    # Create monthly data for last 12 months
    months = pd.date_range(start='2024-09-01', end='2025-08-01', freq='MS')

    data = {
        'Month': months.strftime('%Y-%m'),
        'Main_Targets': np.random.poisson(150, len(months)),
        'Other_Targets': np.random.poisson(75, len(months)),
        'Total_Targets': np.random.poisson(225, len(months)),
        'Detection_Rate': np.random.uniform(0.75, 0.95, len(months))
    }

    df = pd.DataFrame(data)
    df['Detection_Rate'] = (df['Detection_Rate'] * 100).round(1)  # Convert to percentage

    # Create chart
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    # Stacked bar chart for targets
    ax1.bar(df['Month'], df['Main_Targets'], label='Main Targets', color='#9A2A2A', alpha=0.8)
    ax1.bar(df['Month'], df['Other_Targets'], bottom=df['Main_Targets'],
            label='Other Targets', color='#ff6b6b', alpha=0.8)
    ax1.set_title(f'Monthly Target Distribution - Run ID: {run_id}')
    ax1.set_ylabel('Target Count')
    ax1.legend()
    ax1.tick_params(axis='x', rotation=45)

    # Detection rate line chart
    ax2.plot(df['Month'], df['Detection_Rate'], marker='s', color='#2E8B57', linewidth=2, markersize=6)
    ax2.set_title('Detection Rate Trend')
    ax2.set_ylabel('Detection Rate (%)')
    ax2.set_ylim(70, 100)
    ax2.tick_params(axis='x', rotation=45)
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()

    # Convert chart to base64
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', dpi=150, bbox_inches='tight')
    buffer.seek(0)
    chart_data = base64.b64encode(buffer.read()).decode()
    plt.close()

    # Convert DataFrame to HTML with better formatting
    df_formatted = df.copy()
    df_formatted['Detection_Rate'] = df_formatted['Detection_Rate'].apply(lambda x: f"{x}%")

    df_html = df_formatted.to_html(
        classes='table table-striped table-hover',
        table_id='target-table',
        index=False,
        escape=False,
        border=0
    )

    return df_html, chart_data
