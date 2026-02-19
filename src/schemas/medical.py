from pydantic import BaseModel, Field
from typing import Literal


class MedicalInput(BaseModel):
    age: int = Field(..., ge = 1, le = 120)
    gender: str = Literal["Male", "Female"]
    bmi: float = Field(..., ge = 10.0, le = 60.0)
    smoker: str = Literal["Yes", "No"]
    diabetes: bool = Literal[0, 1]
    hypertension: bool = Literal[0, 1]
    heart_disease: bool = Literal[0, 1]
    asthma: bool = Literal[0, 1]
    physical_activity_level: str = Literal["Low", "Medium", "High"]
    daily_steps: int = Field(..., ge = 0, le = 30000)
    sleep_hours: float = Field(..., ge = 0.0, le = 24.0)
    stress_level: int = Field(..., ge = 1, le = 10)
    doctor_visits_per_year: int = Field(..., ge = 0, le = 50)
    hospital_admissions: int = Field(..., ge = 0, le = 20)
    medication_count: int = Field(..., ge = 0, le = 50)
    insurance_type: str = Literal["Private", "Government"]
    insurance_coverage_pct: int = Field(..., ge = 0, le = 100)
    city_type: str = Literal["Urban", "Semi-Urban", "Rural"]
    previous_year_cost: float = Field(..., ge = 0.0)

