# Galaxy-Morpho

Galaxy-Morpho is a research-oriented project that combines astrophysics and machine learning to study galaxy formation and classify galaxy morphologies using real observational data. The work is part of the Equinox Summer Research Module and integrates theoretical understanding with computational implementation.

---

## Project Overview

Galaxies are fundamental building blocks of the universe, evolving over billions of years through gravitational collapse, star formation, and mergers. This project explores both:

1. The physical processes behind galaxy formation and structure  
2. Data-driven techniques to classify galaxies based on observable features  

The repository includes theoretical derivations, machine learning workflows, and a simulation component for modeling galaxy formation.

---

## Modules

### Module 1: Galaxy Formation and Structure

This module focuses on the theoretical foundations of galaxy formation.

Key topics covered include:
- Dark matter halos and the ΛCDM cosmological model  
- Gas cooling and baryonic processes  
- Stellar evolution (Population I, II, III stars)  
- Feedback mechanisms such as supernovae and AGN  
- Hierarchical merging and environmental effects  

A detailed mathematical analysis is also provided to explain why galaxies tend to form disk-like structures. This includes:
- Angular momentum conservation  
- Virial theorem and energy considerations  
- Gravitational and centrifugal force balance  

All derivations and explanations are compiled in the report.

---

### Module 2: Machine Learning for Galaxy Classification

This module implements a supervised learning pipeline to classify galaxies into morphological types.

#### Classification Categories
- Elliptical  
- Spiral  
- Irregular  

#### Approach

- Labels are generated using astrophysical proxies:
  - Sérsic index (structure)
  - g-r color index (stellar population)

- Data preprocessing includes:
  - Feature engineering
  - Feature scaling
  - Train-validation-test split

- Models used:
  - Random Forest Classifier
  - Support Vector Machine (SVM)

#### Results

- Random Forest achieved perfect classification accuracy due error in the method in which it was fitted to data, and the corresponding target variable
- SVM achieved approximately 86% accuracy and showed limitations with non-linear separations  

The results also confirm that physically meaningful features (Sérsic index and color) dominate classification.

---

### Module 3: Simulation (Optional)

This module develops a basic 2D simulation of galaxy formation using particle dynamics.

Features:
- Gravitational interactions between particles  
- Energy and angular momentum tracking  
- Visualization of evolving galaxy structures  

Different initial conditions were tested:
- High angular momentum → spiral-like structures  
- Low angular momentum → elliptical-like collapse  
- Intermediate conditions → irregular structures  

---

## Repository Structure

```text
.
├── LICENSE
├── Module_2.ipynb        # Machine learning workflow
├── Module_3.py           # Simulation code
├── Problem_Statement.pdf  # Project description and tasks
├── README.md             # Documentation
└── Report.pdf            # Final report
```


---

## Dataset

The dataset used for this project can be accessed here:

https://drive.google.com/drive/folders/1BvKNxHaAAesTNzNzpeeQCb0OJuMD_rL6?usp=sharing

### Features include:
- Photometric measurements (g, r, i, z, y bands)  
- Structural parameters such as:
  - Sérsic index  
  - Ellipticity  
  - Half-light radius  
- Redshift information  

---

## Installation and Setup

### Clone the repository
```text
git clone https://github.com/your-username/Galaxy-Morpho.git
cd Galaxy-Morpho
```


### Install dependencies
```text
pip install numpy pandas matplotlib scikit-learn
```


### Run Jupyter Notebook
```text
jupyter notebook
```


---

## Usage

### Machine Learning Pipeline
Open `Module_2.ipynb` and run the cells sequentially to:
- Load and preprocess data  
- Train classification models  
- Evaluate performance  

### Simulation
Run the simulation script:
```text
python Module_3.py
```


---

## Key Insights

- Galaxy morphology is strongly influenced by angular momentum, merger history, and environment  
- Disk formation naturally arises from conservation of angular momentum during collapse  
- Machine learning models can successfully recover physically meaningful relationships from data  
- Feature importance aligns with astrophysical expectations  

---

## Results Summary

| Model           | Accuracy | Notes |
|----------------|---------|------|
| Random Forest  | 1.00    | Captures rule-based structure effectively |
| SVM (Linear)   | 0.86    | Limited by linear decision boundary |

---

## Team

- Soham Das  
- Anurag Kole  
- Aditya Chauhan  
- Soumyadeep Patra  

---

## References

- ΛCDM cosmological model  
- Galaxy formation theory  
- GalaxiesML dataset  
- Equinox Summer Research Module  

---

## License

This project is licensed under the terms specified in the LICENSE file.

---

## Acknowledgements

This work was carried out as part of the Equinox Summer Research Module. The project draws on concepts from astrophysics, data science, and computational modeling, along with publicly available astronomical datasets.

---

## Closing Note

This project demonstrates how theoretical physics and machine learning can be combined to study complex systems like galaxies. It provides both a conceptual understanding and a practical framework for analyzing large-scale astronomical data.
