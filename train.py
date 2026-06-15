import pandas as pd
import joblib
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report, accuracy_score

# ── 1. Տվյալների բեռնում ──────────────────────────────────────────
df = pd.read_csv("news_dataset.csv").dropna()

# Կրկնօրինակ հոդվածների հեռացում (label-ի անկախ)
before = len(df)
df = df.drop_duplicates(subset="text")
print(f"Հեռացված կրկնօրինակներ: {before - len(df)}")
print(f"Ֆինալ dataset: {len(df)} հոդված")
print(df["label"].value_counts())

X = df["text"]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# ── 2. Pipeline — word + char n-grams + LinearSVC ────────────────
#    LinearSVC-ն TF-IDF-ի հետ ավելի արդյունավետ է, քան Random Forest
#    char_wb n-grams — կօգնի հայերենի հոլովման հետ
model = Pipeline([
    ("features", FeatureUnion([
        ("word", TfidfVectorizer(
            analyzer="word",
            max_features=50000,
            ngram_range=(1, 3),
            min_df=2,
            max_df=0.90,
            sublinear_tf=True,
        )),
        ("char", TfidfVectorizer(
            analyzer="char_wb",
            max_features=50000,
            ngram_range=(3, 5),
            min_df=3,
            max_df=0.90,
            sublinear_tf=True,
        )),
    ])),
    ("clf", LinearSVC(C=1.0, max_iter=2000, random_state=42)),
])

# ── 3. Ուսուցում ──────────────────────────────────────────────────
model.fit(X_train, y_train)

# ── 4. Cross-validation — ավելի ճշգրիտ գնահատական ──────────────
cv_scores = cross_val_score(model, X, y, cv=5, scoring="accuracy", n_jobs=-1)
print(f"\n5-fold CV Accuracy: {cv_scores.mean():.3f} ± {cv_scores.std():.3f}")

# ── 5. Test set արդյունքներ ───────────────────────────────────────
pred = model.predict(X_test)
print(f"\nTest Accuracy: {accuracy_score(y_test, pred):.3f}")
print("\nClassification Report:")
print(classification_report(y_test, pred))

# ── 6. Պահում ────────────────────────────────────────────────────
joblib.dump(model, "news_classifier.pkl")
print("Մոդելը պահված է։")