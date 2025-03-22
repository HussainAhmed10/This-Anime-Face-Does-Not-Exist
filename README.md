# This-Anime-Face-Does-Not-Exist
A deep learning project utilizing DCGANs to generate AI-created anime faces.

🔥 Overview
This repository implements a Deep Convolutional Generative Adversarial Network (DCGAN) to synthesize anime-style faces at a resolution of 64×64 pixels. The project follows the standard GAN framework, where a generator learns to create realistic images while a discriminator distinguishes real from fake. By training on an anime dataset, the model progressively improves at generating high-quality, visually convincing anime faces.

The trained model is then integrated into a Streamlit web application, which is hosted on Hugging Face Spaces, allowing users to generate AI-made anime faces with a single click.

🚀 Features
DCGAN Implementation: A neural network trained on anime faces to generate new, unique characters.
Training Pipeline: Data preprocessing, model architecture design, loss functions, and evaluation metrics.
Streamlit App: Interactive UI for generating and visualizing AI-generated anime faces.
Deployment on Hugging Face: Access the model through a simple web-based interface.

📂 Contents
DCGAN Training Notebook: Code to train and fine-tune the model.
Pretrained Model: Save and load trained weights.
Streamlit App: Python script for user-friendly deployment.

📸 Sample Results
![6  epoch_100](https://github.com/user-attachments/assets/02bc378a-1876-44e6-b75d-17b347869f93)

📜 Acknowledgments
Inspired by This Person Does Not Exist and anime dataset sources. Built with PyTorch, Streamlit, and Hugging Face Spaces.
