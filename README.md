# T-Index & PCME Framework  
### Prime–Composite Energy Matching for High-Sensitivity Numerical Field Analysis  
**By Tareq Majeed Al-Karimi (2025)**  

---

## 📌 Overview

This repository contains the **full implementation**, **scientific model**, and **computational framework** developed by *Tareq Majeed Al-Karimi* for analyzing numerical fields using prime–composite structures.  

The project introduces two major analytical tools:

1. **T-Index (Original Prime–Composite Indicator)**  
2. **PCME – Prime–Composite Matching Energy (New Model)**  

Together, these models demonstrate that prime–composite structural symmetry can detect extremely subtle variations in numerical fields—even when those variations are deeply hidden inside noisy or chaotic maps.

---

## 🧠 Scientific Motivation

Natural and synthetic numerical fields often contain **hidden embedded signals**. Traditional statistical tools may miss these patterns.

However, prime and composite numbers exhibit **unique structural signatures** that remain stable even after transformation, scaling, or noise injection.

This observation led to the development of:

- **T-Index:** Measures the structural difference between prime regions and composite regions.  
- **PCME:** A new energy-based metric that quantifies how strongly a field aligns with prime–composite patterns.

---

## 📐 Mathematical Foundations

### **1. Prime–Composite Masking**
Given a field \( K(x,y) \), a prime mask \( P \) and composite mask \( C \) are generated:

\[
P_{ij} = 
\begin{cases}
1 & \text{if } K_{ij} \text{ is prime} \\
0 & \text{otherwise}
\end{cases}
\]

\[
C_{ij} = 
\begin{cases}
1 & \text{if } K_{ij} \text{ is composite} \\
0 & \text{otherwise}
\end{cases}
\]

---

### **2. Original T-Index**
Measures the statistical separation between prime and composite responses:

\[
T = \frac{|\mu_P - \mu_C|}{\sigma_P + \sigma_C + \varepsilon}
\]

Where:

- \( \mu_P, \mu_C \) = mean response in prime and composite regions  
- \( \sigma_P, \sigma_C \) = their standard deviations  
- \( \varepsilon \) = small stabilizer  

---

### **3. PCME (Prime–Composite Matching Energy)**
Introduced in this repository.

For a matching radius \( k \):

\[
E(k) = \sum_{i,j} \left| F(i,j) - F(i+k,j+k) \right|
\]

Breaking it into prime–composite components:

\[
S_{\text{prime}} = \sum E(k) \cdot P
\]
\[
S_{\text{comp}}  = \sum E(k) \cdot C
\]

PCME reveals long-range order that T-Index alone cannot detect.

---

## 📂 Project Structure

