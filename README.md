# Low-Power Pixel Operator for Image Processing

Welcome to the GitHub repository for the **Low-Power Pixel Operator for Image Processing** project! This repository contains all the necessary files, scripts, and documentation to understand, implement, and replicate the project. The design optimizes dynamic power consumption while performing multiple image processing operations using Verilog and Python scripts.

---

## Overview
This project focuses on developing a modular, low-power pixel operator for image processing tasks such as:

- Brightness increase
- Brightness decrease
- Thresholding
- Pixel inversion

The Verilog design incorporates techniques like clock gating to minimize power consumption and uses pipeline registers for accurate data synchronization.

---

## Features
1. **Modular Design**:
   - Separate modules for input, processing, clock gating, and output for easier debugging and scalability.
2. **Power Optimization**:
   - Reduces dynamic power usage using clock gating techniques.
3. **Python Integration**:
   - Python scripts for handling image-to-hexadecimal conversion and vice versa.
4. **Simulation and Verification**:
   - Comprehensive testbench for functional verification and power analysis.

---

## Repository Structure
```plaintext
├── Verilog/
│   ├── pixel_operator.v        # Verilog implementation of the pixel operator
│   ├── d_flipflop.v           # D flip-flop module
│   ├── clock_gating.v         # Clock gating module
│   ├── pixel_operator_tb.v    # Testbench for verification
├── Python/
│   ├── image_to_hex.py        # Script to convert images to hexadecimal
│   ├── hex_to_image.py        # Script to convert hexadecimal back to images
├── Images/
│   ├── input_image.png        # Sample input image
│   ├── output_image.png       # Processed output image
│   ├── output_hex.txt         # Hexadecimal data of the output image
├── README.md                  # Documentation for the project
├── LICENSE                    # License for the project
```

---

## Getting Started

### Prerequisites
- Vivado (or any Verilog simulation tool)
- Python 3.6 or higher
- Required Python libraries:
  - `numpy`
  - `pillow`

### Steps to Run the Project
1. Clone this repository:
   ```bash
   git clone https://github.com/your_username/low-power-pixel-operator.git
   cd low-power-pixel-operator
   ```

2. **Verilog Simulation:**
   - Open the Verilog files in Vivado or your preferred simulation tool.
   - Run the testbench (`pixel_operator_tb.v`) to verify functionality and power efficiency.

3. **Image-to-Hexadecimal Conversion:**
   - Use the Python script `image_to_hex.py` to convert an input image to hexadecimal format:
     ```bash
     python Python/image_to_hex.py
     ```
   - Provide the resulting `.txt` file as input to the Verilog pipeline.

4. **Hexadecimal-to-Image Conversion:**
   - After Verilog processing, use the `hex_to_image.py` script to convert the output `.txt` file back to an image:
     ```bash
     python Python/hex_to_image.py
     ```

5. **Analyze Results:**
   - Compare the output image with the expected results to validate the functionality.

---

---

## Results
- **Power Efficiency:**
  - Dynamic Power Reduction: 43% (normalized).
  - Static Power Consumption: 0.1 (base).
- **Functional Accuracy:**
  - Verified with a 98304-pixel image.
  - Accurate for all operations: brightness adjustment, thresholding, and inversion.

---

## Future Work
- Extend the pipeline for more complex image processing tasks.
- Implement real-time processing on FPGA hardware.
- Enhance power optimization techniques with adaptive clock scaling.

---

## Contributions
Contributions are welcome! Feel free to open issues or submit pull requests.

---

## Contact
For any queries, reach out at:
- **Author:** Syed Maarij
- **Email:** syedmaarij61@gmail.com

---

