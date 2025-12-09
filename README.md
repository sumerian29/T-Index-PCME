# T-Index & PCES — Prime–Composite Early Symmetry Toolkit

This repository contains the implementation of:

- **T-Index**: a curl/divergence-based metric for detecting vortex-like patterns in 2D fields.
- **PCME** (Prime–Composite Matching Energy): a new, more sensitive metric inspired by a rare
  numerical symmetry between prime and composite numbers, described in the
  **Prime–Composite Early Symmetry (PCES) Theory**.

Author: **Tareq Majeed Al-Karimi**  
Collaborator: ChatGPT (OpenAI, AI-assisted co-design)

---

## 1. Scientific Idea

The project explores a bridge between:

- **Number theory**: an early, rare equality between cumulative sums of primes and composites,
- **Digital cosmology**: simulated “digital universes” on 2D grids,
- **Pattern detection**: new metrics that can distinguish noise-only fields from signal+noise fields.

PCME measures how similar the total “curl-like energy” is on **prime-index radial shells**
compared to **composite-index radial shells**, especially in the early shells.  
A higher PCME suggests a rare global balance, analogous (in spirit) to early-universe symmetry.

---

## 2. Repository Structure

```text
src/        Core algorithms (T-Index, PCME, simulation, visualization)
examples/   Example scripts to run experiments
docs/       Method notes and concept documentation
paper/      LaTeX source for the PCES research paper
figures/    Python scripts to generate figures (PNG, PDF)
tests/      Unit tests (can be expanded later)
