 Sepsis & Organ Stress Digital Twin

Built for the **Happiest Health - Digital Twin Challenge 2026**.

 Team & College Details
* Developer: Nikesh Kumar
* College / University: Nagaland University

 Problem Statement & Healthcare Use Case
Sepsis moves fast in ICUs. By the time routine monitors trigger an alarm, organ damage has often already started—leaving doctors with very little time to react. 
This project is a proof-of-concept **Digital Twin** that pairs real-time wearable vitals with hospital lab data (EHR). Instead of reacting to late-stage symptoms, it spots subtle patterns to predict sepsis **6 to 8 hours before** full clinical onset.

Technical Stack & AI/ML Model
* Language: Python
* ML Engine / Framework: Scikit-Learn (Random Forest Classifier)
* Data Processing: Pandas, NumPy
* Frontend Dashboard: Streamlit


 Architecture & Presentation
Architecture Diagram: Box 1: Data Sources (EHR Lab Data + Wearables Vitals)
⬇️ (Arrow down)

Box 2:  Data Preprocessing (Handling missing values, scaling)
⬇️️ (Arrow down)

Box 3:  AI/ML Engine (Random Forest Classifier)
⬇️ (Arrow down)

Box 4: 💻 Digital Twin Dashboard (Streamlit UI: Sepsis Risk Score & Organ Stress Index)


## 💡 How It Works
The Digital Twin continuously processes incoming health metrics to calculate three dynamic risk indicators:
* Sepsis Risk Score (%)** – Overall probability of sepsis developing in the next 6–8 hours.
* Kidney Stress Index** – Early detection of renal strain based on lab markers like Creatinine.
* Respiratory Stress Index – Real-time tracking of SpO2 and respiratory strain patterns.
