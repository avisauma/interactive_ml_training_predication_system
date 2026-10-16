# Interactive Machine Learning Model Training and Prediction System

Streamlit educational project showing:
Dataset -> Cleaning -> Preprocessing -> Training -> Evaluation -> Prediction

Includes six real scikit-learn classifiers and an educational CNN visualization.

## Run
```bash
pip install -r requirements.txt
streamlit run app.py
```

If you do not have a CSV, use the built-in Demo Dataset.

## CNN note
The CNN tab visualizes the CNN pipeline (input, convolution, feature maps, pooling, dense layer, prediction). It is an educational explainer, not actual CNN training. Actual CNN training would require an image dataset and TensorFlow/PyTorch.
