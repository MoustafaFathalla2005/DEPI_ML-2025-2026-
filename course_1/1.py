# جرب استيراد كل المكتبات
try:
    import torch, torchvision, torchaudio
    import sklearn, scipy, numpy, pandas
    import matplotlib, seaborn, plotly, streamlit
    import pyswip, jupyter, notebook
    import xgboost, tensorflow, keras
    print("✅ كل المكتبات اتعملها import بنجاح")
except Exception as e:
    print("❌ في مشكلة:", e)

# تأكيد إن PyTorch شايف الـ GPU
print("PyTorch GPU available:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("GPU name:", torch.cuda.get_device_name(0))