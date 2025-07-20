from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

def train_model(df):
    """
    Melatih model klasifikasi sentimen menggunakan TF-IDF dan Logistic Regression.
    """
    X_text = df['preprocessed_text']
    y = df['sentimen']

    # TF-IDF Vectorization
    tfidf = TfidfVectorizer(max_features=1000)
    X = tfidf.fit_transform(X_text)

    # Train model
    model = LogisticRegression()
    model.fit(X, y)

    return model, tfidf

def evaluate_model(model, tfidf, df):
    """
    Mengevaluasi model terhadap data ulasan.
    """
    X_test = tfidf.transform(df['preprocessed_text'])
    y_test = df['sentimen']
    y_pred = model.predict(X_test)

    print("Akurasi:", accuracy_score(y_test, y_pred))
    print("Laporan Klasifikasi:\n", classification_report(y_test, y_pred))
