import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

def load_and_clean_data():
    """
    Load the page view data and clean it by filtering out outliers.
    Outliers are defined as days where page views are in the top 2.5% or bottom 2.5%.
    """
    # Load data from CSV
    df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')
    
    # Clean data by removing outliers (top 2.5% and bottom 2.5%)
    lower_bound = df['value'].quantile(0.025)
    upper_bound = df['value'].quantile(0.975)
    df_clean = df[(df['value'] >= lower_bound) & (df['value'] <= upper_bound)]
    
    return df_clean

def draw_line_plot(df):
    """
    Draw a line chart showing daily freeCodeCamp forum page views over time.
    """
    fig, ax = plt.subplots(figsize=(14, 6))
    
    ax.plot(df.index, df['value'], color='#d62728', linewidth=1)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019', fontsize=14)
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Page Views', fontsize=12)
    
    plt.tight_layout()
    plt.savefig('line_plot.png', dpi=100)
    print("[v0] Line plot saved as 'line_plot.png'")
    return fig

def draw_bar_plot(df):
    """
    Draw a bar chart showing average daily page views for each month, grouped by year.
    """
    # Prepare data for bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month
    
    # Calculate average page views per month
    df_pivot = df_bar.groupby(['year', 'month'])['value'].mean().unstack()
    
    # Create bar plot
    fig, ax = plt.subplots(figsize=(12, 6))
    
    month_labels = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December']
    
    df_pivot.plot(kind='bar', ax=ax, width=0.8)
    ax.set_xlabel('Years', fontsize=12)
    ax.set_ylabel('Average Page Views', fontsize=12)
    ax.legend(title='Months', labels=month_labels, loc='upper left')
    ax.set_xticklabels(df_pivot.index, rotation=90)
    
    plt.tight_layout()
    plt.savefig('bar_plot.png', dpi=100)
    print("[v0] Bar plot saved as 'bar_plot.png'")
    return fig

def draw_box_plot(df):
    """
    Draw two adjacent box plots:
    1. Year-wise box plot showing distribution of page views by year
    2. Month-wise box plot showing distribution of page views by month
    """
    # Prepare data for box plots
    df_box = df.copy()
    df_box['year'] = df_box.index.year
    df_box['month'] = df_box.index.strftime('%b')
    df_box['month_num'] = df_box.index.month
    df_box = df_box.sort_values('month_num')
    
    # Create figure with two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    # Year-wise box plot
    sns.boxplot(data=df_box, x='year', y='value', ax=ax1, palette='Set2')
    ax1.set_title('Year-wise Box Plot (Trend)', fontsize=14)
    ax1.set_xlabel('Year', fontsize=12)
    ax1.set_ylabel('Page Views', fontsize=12)
    
    # Month-wise box plot
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.boxplot(data=df_box, x='month', y='value', order=month_order, ax=ax2, palette='Set3')
    ax2.set_title('Month-wise Box Plot (Seasonality)', fontsize=14)
    ax2.set_xlabel('Month', fontsize=12)
    ax2.set_ylabel('Page Views', fontsize=12)
    
    plt.tight_layout()
    plt.savefig('box_plot.png', dpi=100)
    print("[v0] Box plot saved as 'box_plot.png'")
    return fig

def main():
    """
    Main function to run the time series visualizer.
    """
    print("[v0] Starting time series visualization...")
    
    # Check if CSV file exists
    csv_path = Path('fcc-forum-pageviews.csv')
    if not csv_path.exists():
        print("[v0] ERROR: 'fcc-forum-pageviews.csv' not found!")
        print("[v0] Please download the data from:")
        print("[v0] https://raw.githubusercontent.com/freeCodeCamp/boilerplate-page-view-time-series-visualizer/master/fcc-forum-pageviews.csv")
        return
    
    # Load and clean data
    print("[v0] Loading and cleaning data...")
    df = load_and_clean_data()
    print(f"[v0] Data loaded: {len(df)} rows after cleaning")
    
    # Generate all three visualizations
    print("[v0] Generating line plot...")
    draw_line_plot(df)
    
    print("[v0] Generating bar plot...")
    draw_bar_plot(df)
    
    print("[v0] Generating box plots...")
    draw_box_plot(df)
    
    print("[v0] All visualizations complete!")
    print("[v0] Generated files: line_plot.png, bar_plot.png, box_plot.png")

if __name__ == "__main__":
    main()
