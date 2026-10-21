import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_automated_visualizations(file_path):
    print("📊 Loading dataset for visualization...")
    df = pd.read_csv(file_path)
    
    # Set seaborn style
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(10, 6))
    
    # Automatically detect numerical columns and plot distribution
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    
    if len(numeric_cols) > 0:
        sns.histplot(df[numeric_cols[0]], kde=True, color='purple')
        plt.title(f'Automated Distribution Plot for {numeric_cols[0]}')
        plt.xlabel(numeric_cols[0])
        plt.ylabel('Frequency')
        
        output_path = "outputs/generated_charts.png"
        plt.savefig(output_path)
        print(f"✅ Visualization saved successfully to {output_path}")
    else:
        print("⚠️ No numerical columns found for automated plotting.")

if __name__ == "__main__":
    # Test execution
    generate_automated_visualizations("data/dataset.csv")
