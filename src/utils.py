import matplotlib.pyplot as plt
import seaborn as sns

def plot_sentiment_distribution(df):
    """
    Visualisasi distribusi label sentimen.
    """
    plt.figure(figsize=(6,4))
    sns.countplot(data=df, x='sentimen', palette='pastel')
    plt.title('Distribusi Sentimen Ulasan Produk')
    plt.xlabel('Sentimen')
    plt.ylabel('Jumlah')
    plt.tight_layout()
    plt.show()

def top_keywords_by_sentiment(df, sentiment_label='positive', n_top=10):
    """
    Menampilkan kata-kata paling umum dari sentimen tertentu.
    """
    from sklearn.feature_extraction.text import CountVectorizer

    filtered_texts = df[df['sentimen'] == sentiment_label]['preprocessed_text']
    vectorizer = CountVectorizer(stop_words='english')
    X = vectorizer.fit_transform(filtered_texts)
    sum_words = X.sum(axis=0)
    words_freq = [(word, sum_words[0, idx]) for word, idx in vectorizer.vocabulary_.items()]
    words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)[:n_top]

    print(f"Top {n_top} keywords untuk sentimen '{sentiment_label}':")
    for word, freq in words_freq:
        print(f"{word}: {freq}")
