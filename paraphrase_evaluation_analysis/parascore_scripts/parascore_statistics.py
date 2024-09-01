import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import argparse
import os

def load_data(file_path):
    return pd.read_csv(file_path)

def calculate_basic_stats(df):
    score_columns = [col for col in df.columns if col.startswith('ParaScore_')] + ['Avg_ParaScore']
    percentiles = [1, 5, 10, 25, 50, 75, 90, 95, 99]
    
    def percentile_agg(x, p):
        return x.quantile(p/100)
    
    agg_functions = ['mean', 'median', 'std', 'min', 'max'] + [lambda x, p=p: percentile_agg(x, p) for p in percentiles]
    agg_names = ['mean', 'median', 'std', 'min', 'max'] + [f'{p}th_percentile' for p in percentiles]
    
    stats = df[score_columns].agg(agg_functions)
    stats.index = agg_names
    return stats.T

def plot_score_distribution(df, output_dir):
    plt.figure(figsize=(12, 6))
    sns.histplot(df['Avg_ParaScore'], kde=True, bins=50)
    plt.title('Distribution of Average ParaScores')
    plt.xlabel('Average ParaScore')
    plt.ylabel('Frequency')
    
    percentiles = [10, 25, 50, 75, 90]
    colors = ['r', 'g', 'b', 'g', 'r']
    labels = ['10th', '25th', '50th (Median)', '75th', '90th']
    
    for p, c, l in zip(percentiles, colors, labels):
        value = np.percentile(df['Avg_ParaScore'], p)
        plt.axvline(value, color=c, linestyle='--', label=f'{l} Percentile')
    
    plt.legend()
    plt.savefig(os.path.join(output_dir, 'avg_parascore_distribution.png'))
    plt.close()

def plot_score_boxplot(df, output_dir):
    score_columns = [col for col in df.columns if col.startswith('ParaScore_')]
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df[score_columns])
    plt.title('Boxplot of ParaScores for Different Rephrases')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'parascore_boxplot.png'))
    plt.close()

def calculate_correlations(df, output_dir):
    score_columns = [col for col in df.columns if col.startswith('ParaScore_')]
    corr = df[score_columns].corr()
    
    plt.figure(figsize=(12, 10))
    sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1, center=0)
    plt.title('Correlation Heatmap of ParaScores')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'parascore_correlations.png'))
    plt.close()
    
    return corr

def generate_threshold_recommendations(df):
    avg_score = df['Avg_ParaScore']
    percentiles = [25, 50, 75, 90, 95]
    thresholds = np.percentile(avg_score, percentiles)
    
    recommendations = []
    for p, t in zip(percentiles, thresholds):
        recommendations.append(f"For a threshold at the {p}th percentile (top {100-p}% of scores): {t:.4f}")
    
    return "\n".join(recommendations)

def process_file(input_file, output_dir):
    df = load_data(input_file)
    
    file_name = os.path.splitext(os.path.basename(input_file))[0]
    file_output_dir = os.path.join(output_dir, file_name)
    os.makedirs(file_output_dir, exist_ok=True)
    
    basic_stats = calculate_basic_stats(df)
    basic_stats.to_csv(os.path.join(file_output_dir, 'basic_statistics.csv'))
    
    plot_score_distribution(df, file_output_dir)
    plot_score_boxplot(df, file_output_dir)
    
    correlations = calculate_correlations(df, file_output_dir)
    correlations.to_csv(os.path.join(file_output_dir, 'parascore_correlations.csv'))
    
    threshold_recommendations = generate_threshold_recommendations(df)
    with open(os.path.join(file_output_dir, 'threshold_recommendations.txt'), 'w') as f:
        f.write(threshold_recommendations)
    
    print(f"Statistics generated for {input_file} and saved in {file_output_dir}")

def generate_statistics(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    
    for filename in os.listdir(input_dir):
        if filename.endswith('.csv'):
            input_file = os.path.join(input_dir, filename)
            process_file(input_file, output_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate statistics for parascore results.")
    parser.add_argument("input_dir", type=str, help="Directory containing parascore CSV files")
    parser.add_argument("output_dir", type=str, help="Directory to save output statistics and plots")
    args = parser.parse_args()
    
    generate_statistics(args.input_dir, args.output_dir)