import os
import zipfile

# Create the folder structure for the Genesis Network
base_dir = "/mnt/data/Genesis_Network_Project"
folders = [
    "Genesis_Network_Project",
    "Genesis_Network_Project/docs",
    "Genesis_Network_Project/code",
    "Genesis_Network_Project/data",
    "Genesis_Network_Project/models",
    "Genesis_Network_Project/notebooks",
    "Genesis_Network_Project/scripts",
]
readme_content = """
# Genesis Network: README

## Overview
The Genesis Network is the foundational layer of interconnected nodes representing dynamic knowledge, relationships, and resilience. It forms the backbone for the Cube4D framework, enabling infinite scalability and adaptability.

## Key Concepts
1. **Node0** - The Origin:
   - Represents the immutable truth, the anchor for all connections and expansions.
   - Acts as a loopback for the network, ensuring self-referential consistency.

2. **Cube4D** - Multi-Dimensional Knowledge:
   - Built on the principles of relational and recursive networks.
   - Designed for dynamic growth, infinite scalability, and inherent resilience.

3. **Dynamic Relationship Expansion (DRE)**:
   - Ensures relationships evolve contextually, adapting to new data and scenarios.
   - Bridges the gap between static knowledge and dynamic inference.

## Project Structure
- **docs/**:
  Contains in-depth explanations of the concepts, architecture, and algorithms.

- **code/**:
  Houses the source code for the Genesis Network framework.

- **data/**:
  Includes datasets for testing and experimentation.

- **models/**:
  Stores pre-trained models for quick deployment and integration.

- **notebooks/**:
  Features tutorials, exploratory analyses, and demonstrations.

- **scripts/**:
  Utility scripts for deployment, testing, and automation.

## Getting Started
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the desired folder and explore the resources.
3. Run notebooks to understand and visualize the framework in action.

## Contact
For inquiries or contributions, reach out to: callum@youmatter.systems

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

Let's build the future of knowledge and connectivity together.
"""

# Create folders and README file
os.makedirs(base_dir, exist_ok=True)
for folder in folders:
    os.makedirs(folder, exist_ok=True)

readme_path = os.path.join(base_dir, "README.md")
with open(readme_path, "w") as f:
    f.write(readme_content)

# Create a zip file
zip_path = "Genesis_Network_Project.zip"
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            full_path = os.path.join(root, file)
            arcname = os.path.relpath(full_path, base_dir)
            zipf.write(full_path, arcname)

zip_path
