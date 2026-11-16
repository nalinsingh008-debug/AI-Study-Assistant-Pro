import numpy as np
from sklearn.linear_model import LinearRegression

class PerformancePredictor:
    """Illustrative model; predictions are not validated academic outcomes."""
    def __init__(self):
        x = np.array([[0, 0], [1, 1], [2, 2], [3, 4], [4, 5], [5, 7]], dtype=float)
        y = np.array([20, 32, 45, 58, 70, 85], dtype=float)
        self.model = LinearRegression().fit(x, y)

    def predict(self, study_hours: float, tasks_completed: int) -> float:
        value = self.model.predict([[study_hours, tasks_completed]])[0]
        return round(float(np.clip(value, 0, 100)), 2)
