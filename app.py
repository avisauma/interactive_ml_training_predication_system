import time
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

st.set_page_config(page_title="Interactive ML Training & Prediction", page_icon="🧠", layout="wide")

for key, value in {
    "df": None, "model": None, "metrics": None, "prediction": None,
    "target": None, "cleaned": None, "test_data": None, "class_names": []
}.items():
    if key not in st.session_state:
        st.session_state[key] = value


def make_demo_data(n=300):
    rng = np.random.default_rng(42)
    age = rng.integers(18, 55, n)
    income = rng.integers(15000, 120000, n)
    score = np.clip(rng.normal(65, 15, n), 20, 100).round(1)
    experience = rng.integers(0, 15, n)
    target = ((score + experience * 2 + income / 15000 + age * .15) > 75).astype(int)
    df = pd.DataFrame({"age": age, "income": income, "score": score, "experience": experience, "result": target})
    df.loc[[3, 20, 55], "income"] = np.nan
    df.loc[[8, 70], "score"] = np.nan
    return pd.concat([df, df.iloc[[0, 1, 2]]], ignore_index=True)


def clean_data(df):
    before = {"rows": len(df), "columns": len(df.columns), "missing": int(df.isna().sum().sum()), "duplicates": int(df.duplicated().sum())}
    out = df.drop_duplicates().copy()
    for col in out.columns:
        if out[col].isna().any():
            if pd.api.types.is_numeric_dtype(out[col]):
                out[col] = out[col].fillna(out[col].median())
            else:
                mode = out[col].mode()
                out[col] = out[col].fillna(mode.iloc[0] if not mode.empty else "Unknown")
    after = {"rows": len(out), "columns": len(out.columns), "missing": int(out.isna().sum().sum()), "duplicates": int(out.duplicated().sum())}
    return out, before, after


def build_model(name):
    return {
        "Logistic Regression": LogisticRegression(max_iter=1000),
        "Decision Tree": DecisionTreeClassifier(max_depth=6, random_state=42),
        "Random Forest": RandomForestClassifier(n_estimators=120, random_state=42),
        "KNN": KNeighborsClassifier(n_neighbors=5),
        "SVM": SVC(kernel="rbf"),
        "Gradient Boosting": GradientBoostingClassifier(random_state=42),
    }[name]


def cnn_explainer():
    st.header("🧠 CNN Process Visualization")
    st.caption("Educational visualization of the CNN pipeline.")
    rng = np.random.default_rng(7)
    image = rng.random((8, 8))
    kernel = np.array([[-1,-1,-1],[0,0,0],[1,1,1]], dtype=float)
    feature = np.zeros((6, 6))
    for i in range(6):
        for j in range(6):
            feature[i,j] = np.sum(image[i:i+3,j:j+3] * kernel)
    feature = np.maximum(feature, 0)
    pooled = np.zeros((3,3))
    for i in range(3):
        for j in range(3):
            pooled[i,j] = np.max(feature[i*2:i*2+2,j*2:j*2+2])

    stages = [
        ("1. Input Image", image, "Image pixels enter the network as numbers."),
        ("2. Convolution", feature, "A filter scans local regions to detect patterns."),
        ("3. Feature Maps", feature, "Detected patterns form feature maps."),
        ("4. Pooling", pooled, "Max pooling reduces size while retaining strong features."),
    ]
    cols = st.columns(4)
    for col, (title, data, desc) in zip(cols, stages):
        with col:
            st.subheader(title)
            fig, ax = plt.subplots(figsize=(3,3))
            ax.imshow(data, cmap="viridis")
            ax.set_xticks([]); ax.set_yticks([])
            st.pyplot(fig, use_container_width=True)
            st.caption(desc)

    c1, c2 = st.columns(2)
    with c1:
        st.subheader("5. Dense Layer")
        dense = np.array([.82,.61,.33,.91,.48])
        fig, ax = plt.subplots(figsize=(6,2.5)); ax.bar(range(1,6), dense); ax.set_xlabel("Neuron"); ax.set_ylabel("Activation")
        st.pyplot(fig, use_container_width=True)
        st.caption("Extracted features are passed to fully connected neurons.")
    with c2:
        st.subheader("6. Prediction")
        probs = np.array([.08,.92])
        fig, ax = plt.subplots(figsize=(6,2.5)); ax.bar(["Class 0","Class 1"], probs); ax.set_ylim(0,1); ax.set_ylabel("Probability")
        st.pyplot(fig, use_container_width=True)
        st.success("Example prediction: Class 1 (92%)")
    st.info("CNN panel is an educational visual explainer. The tabular ML section trains real scikit-learn models.")


st.title("🧠 Interactive Machine Learning Model Training & Prediction System")
st.write("**Visualize the complete ML workflow — before, during and after each stage.**")
tabs = st.tabs(["📂 Dataset", "🧹 Cleaning", "⚙️ Preprocessing", "🏋️ Training", "📊 Evaluation", "🔮 Prediction", "🧠 CNN Explainer"])

with tabs[0]:
    st.header("📂 Dataset Upload & Inspection")
    uploaded = st.file_uploader("Upload a CSV dataset", type=["csv"])
    if uploaded:
        try:
            st.session_state.df = pd.read_csv(uploaded)
            st.success(f"Loaded {len(st.session_state.df)} rows and {len(st.session_state.df.columns)} columns.")
        except Exception as e:
            st.error(f"Could not read CSV: {e}")
    if st.button("Use Demo Dataset"):
        st.session_state.df = make_demo_data()
        st.success("Demo dataset loaded.")
    if st.session_state.df is not None:
        st.subheader("Before Processing — Raw Dataset")
        st.dataframe(st.session_state.df.head(12), use_container_width=True)
        a,b,c = st.columns(3)
        a.metric("Rows", len(st.session_state.df)); b.metric("Missing Values", int(st.session_state.df.isna().sum().sum())); c.metric("Duplicates", int(st.session_state.df.duplicated().sum()))

with tabs[1]:
    st.header("🧹 Cleaning Visualization")
    if st.session_state.df is None:
        st.warning("Upload a CSV or use the Demo Dataset first.")
    else:
        cleaned, before, after = clean_data(st.session_state.df)
        a,b = st.columns(2)
        with a:
            st.subheader("Before Cleaning"); st.metric("Rows", before["rows"]); st.metric("Missing", before["missing"]); st.metric("Duplicates", before["duplicates"])
        with b:
            st.subheader("After Cleaning"); st.metric("Rows", after["rows"]); st.metric("Missing", after["missing"]); st.metric("Duplicates", after["duplicates"])
        st.write("**Cleaning Flow:** Raw Dataset → Detect Missing Values → Fill Missing Values → Remove Duplicates → Clean Dataset")
        st.dataframe(cleaned.head(12), use_container_width=True)
        st.session_state.cleaned = cleaned

with tabs[2]:
    st.header("⚙️ Preprocessing Visualization")
    if st.session_state.df is None:
        st.warning("Upload a CSV or use the Demo Dataset first.")
    else:
        cleaned,_,_ = clean_data(st.session_state.df)
        default_target = st.session_state.target if st.session_state.target in cleaned.columns else cleaned.columns[-1]
        target = st.selectbox("Select Target Column", cleaned.columns, index=list(cleaned.columns).index(default_target))
        X = cleaned.drop(columns=[target])
        st.session_state.target = target; st.session_state.cleaned = cleaned
        for title, desc in [
            ("1️⃣ Raw Data", "Original feature values."),
            ("2️⃣ Missing Values Handled", "Numeric values use median; categorical values use the most frequent value."),
            ("3️⃣ Encoding", "Categorical features are converted to numeric representation."),
            ("4️⃣ Scaling", "Numeric features are standardized for algorithms that depend on feature scale."),
            ("5️⃣ Model-Ready Data", "The transformed features are ready for model training."),
        ]:
            with st.expander(title, expanded=title == "1️⃣ Raw Data"):
                st.write(desc); st.dataframe(X.head(6), use_container_width=True)

with tabs[3]:
    st.header("🏋️ Model Training Visualization")
    if st.session_state.df is None:
        st.warning("Upload a CSV or use the Demo Dataset first.")
    else:
        cleaned,_,_ = clean_data(st.session_state.df)
        default_target = st.session_state.target if st.session_state.target in cleaned.columns else cleaned.columns[-1]
        target = st.selectbox("Target Column", cleaned.columns, index=list(cleaned.columns).index(default_target))
        algorithm = st.selectbox("Choose Algorithm", ["Logistic Regression","Decision Tree","Random Forest","KNN","SVM","Gradient Boosting"])
        test_size = st.slider("Test Size", .2, .4, .2, .05)
        st.subheader("Before Training")
        st.info("The model has not learned from the training data yet.")
        if st.button("🚀 Start Training", type="primary"):
            X = cleaned.drop(columns=[target]); y = cleaned[target]
            if y.dtype == "object":
                le = LabelEncoder(); y = pd.Series(le.fit_transform(y), index=y.index); st.session_state.class_names = list(le.classes_)
            else:
                st.session_state.class_names = [str(x) for x in sorted(pd.Series(y).unique())]
            num_cols = X.select_dtypes(include=np.number).columns.tolist(); cat_cols = X.select_dtypes(exclude=np.number).columns.tolist()
            transformers=[]
            if num_cols:
                transformers.append(("num", Pipeline([("imputer",SimpleImputer(strategy="median")),("scaler",StandardScaler())]), num_cols))
            if cat_cols:
                transformers.append(("cat", Pipeline([("imputer",SimpleImputer(strategy="most_frequent")),("onehot",OneHotEncoder(handle_unknown="ignore"))]), cat_cols))
            pipe = Pipeline([("preprocessor", ColumnTransformer(transformers=transformers)), ("model", build_model(algorithm))])
            X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=test_size,random_state=42,stratify=y if y.nunique()>1 else None)
            progress=st.progress(0); status=st.empty()
            status.write("Preparing training data..."); progress.progress(20); time.sleep(.25)
            status.write("Applying preprocessing..."); progress.progress(40); time.sleep(.25)
            status.write(f"Training {algorithm}..."); progress.progress(65); pipe.fit(X_train,y_train); time.sleep(.25)
            status.write("Testing trained model..."); progress.progress(85); pred=pipe.predict(X_test); progress.progress(100); status.write("Training completed successfully.")
            st.session_state.model=pipe; st.session_state.metrics={"Accuracy":accuracy_score(y_test,pred),"Precision":precision_score(y_test,pred,average="weighted",zero_division=0),"Recall":recall_score(y_test,pred,average="weighted",zero_division=0),"F1 Score":f1_score(y_test,pred,average="weighted",zero_division=0)}; st.session_state.test_data=(X_test,y_test,pred); st.session_state.target=target; st.session_state.cleaned=cleaned; st.session_state.algorithm=algorithm
            st.success("✅ Training completed.")
            st.subheader("After Training"); st.write(f"Trained algorithm: **{algorithm}** | Training rows: **{len(X_train)}** | Testing rows: **{len(X_test)}**")

with tabs[4]:
    st.header("📊 Model Evaluation")
    if st.session_state.metrics is None:
        st.info("Train a model first.")
    else:
        cols=st.columns(4)
        for col,(name,val) in zip(cols,st.session_state.metrics.items()): col.metric(name,f"{val*100:.2f}%")
        X_test,y_test,pred=st.session_state.test_data
        cm=confusion_matrix(y_test,pred)
        fig,ax=plt.subplots(figsize=(6,4)); sns.heatmap(cm,annot=True,fmt="d",cmap="Blues",ax=ax); ax.set_xlabel("Predicted"); ax.set_ylabel("Actual"); ax.set_title("Confusion Matrix"); st.pyplot(fig,use_container_width=False)

with tabs[5]:
    st.header("🔮 Prediction Visualization")
    if st.session_state.model is None:
        st.warning("Train a model first.")
    else:
        cleaned=st.session_state.cleaned; target=st.session_state.target; features=[c for c in cleaned.columns if c!=target]
        st.subheader("Before Prediction"); st.info("Enter feature values, then click Predict.")
        input_values={}; cols=st.columns(2)
        for i,colname in enumerate(features):
            with cols[i%2]:
                s=cleaned[colname]
                if pd.api.types.is_numeric_dtype(s): input_values[colname]=st.number_input(colname,value=float(s.median()),key="pred_"+colname)
                else:
                    opts=s.dropna().astype(str).unique().tolist(); input_values[colname]=st.selectbox(colname,opts or ["Unknown"],key="pred_"+colname)
        if st.button("🔮 Predict",type="primary"):
            st.subheader("ML Prediction Process")
            status=st.empty()
            for msg in ["🟢 1. Input Received","🟡 2. Preparing Input Data","🔵 3. Sending Data to Trained Model","🟣 4. Generating Prediction"]:
                status.write(msg); time.sleep(.35)
            input_df=pd.DataFrame([input_values],columns=features); prediction=st.session_state.model.predict(input_df)[0]; st.session_state.prediction=prediction
            st.subheader("After Prediction"); st.success(f"Predicted Class: **{prediction}**"); st.dataframe(input_df,use_container_width=True)

with tabs[6]:
    cnn_explainer()
