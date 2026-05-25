import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "backend"))
try:
    from api.main import app
    print("FastAPI app imported successfully!")
except Exception as e:
    import traceback
    traceback.print_exc()
