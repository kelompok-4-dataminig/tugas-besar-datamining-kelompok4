from data_loader import load_clean_data
from model import train_model, evaluate_model
from utils import plot_sentiment_distribution, top_keywords_by_sentiment

def main():
    # === 1. Load & Bersihkan Data ===
    print("Memuat data...")
    df = load_clean_data()  # gunakan path default

    # === 2. Visualisasi Distribusi Sentimen ===
    print("Menampilkan distribusi sentimen...")
    plot_sentiment_distribution(df)

    # === 3. Latih Model Sentimen ===
    print("Melatih model klasifikasi sentimen...")
    model, tfidf = train_model(df)

    # === 4. Evaluasi Model ===
    print("Mengevaluasi model...")
    evaluate_model(model, tfidf, df)

    # === 5. Tampilkan Kata Kunci Utama per Sentimen ===
    for label in df['sentimen'].unique():
        print(f"\nTop keywords untuk sentimen: {label}")
        top_keywords_by_sentiment(df, sentiment_label=label)

if __name__ == "__main__":
    main()
