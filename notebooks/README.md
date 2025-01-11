# My Experimental Notebooks

| No | Title | Date |
| --- | --- | --- |
| 1 | [MediaPipe: Sign Video to Embedding](./01_mediapipe.ipynb) | 2024-11-09 |

You are recommended to install the dependencies and run the notebooks in a virtual environment. I personally use `conda` for this.

To setup from scratch:

```powershell
# Current working directory needs to be where this README is located
# You can replace "signer" with another environment name
conda create --name signer --file environment.yml
conda activate signer
```

⚠️ Note that the `environment.yml` file is specific to my machine (e.g., I used PyTorch for CUDA 12.1). You need to modify this YAML file, or install the packages in a different way, to suit your specifications.

⚠️ I used a Windows machine, so you may want to modify the setup procedure and even some code to run on other operating systems.
