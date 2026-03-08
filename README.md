# 8-Layer Litz-Wire Axial Flux Permanent Magnet (AFPM) Stator

## Project Overview
This repository contains the design, parametric modeling scripts, and documentation for an 8-layer Axial Flux Permanent Magnet (AFPM) motor stator. The primary engineering focus of this project is to minimize AC copper losses (skin and proximity effects) at high frequencies by integrating Litz wire into a multi-layer axial flux topology.

## Key Engineering Features
* **8-Layer Winding Geometry:** Optimized for high copper fill factor and uniform magnetic flux distribution across the air gap.
* **Litz Wire Implementation:** Specifically chosen to mitigate high-frequency eddy current losses inherent in solid copper conductors.
* **Parametric CAD Automation:** The 3D models and structural parameters are generated using Python, allowing for rapid iteration and dimensional scaling.

## Repository Structure
* `docs/`: Technical documentation, cross-section analyses, and theoretical calculations (e.g., `Z-Axis.pdf`).
* `images/`: Visualizations and CAD renderings of the stator layers.
* `src/`: Python source code (`8-layer_AFPM.py`) used for the parametric generation of the stator geometry.

## Current Status & Future Work
The stator design and coil optimization phases are complete. The next phase involves:
* Designing the complementary 12-pole Neodymium (NdFeB) rotor array.
* Determining optimal magnet thickness and air gap tolerances for cogging torque reduction.
* Conducting magnetic Finite Element Analysis (FEA) to validate torque output.
