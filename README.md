# This Anime Face Does Not Exist 🎨🤖  

A deep learning project utilizing DCGANs to generate AI-created anime faces.  

## 🔥 Overview  
This repository implements a **Deep Convolutional Generative Adversarial Network (DCGAN)** to synthesize anime-style faces at a resolution of 64×64 pixels. The project follows the standard GAN framework, where a **generator** learns to create realistic images while a **discriminator** distinguishes real from fake. By training on an anime dataset, the model progressively improves at generating high-quality, visually convincing anime faces.  

The trained model is then integrated into a **Streamlit web application**, which is hosted on **Hugging Face Spaces**, allowing users to generate AI-made anime faces with a single click.  

## 🚀 Features  
- **DCGAN Implementation**: A neural network trained on anime faces to generate new, unique characters.  
- **Training Pipeline**: Data preprocessing, model architecture design, loss functions, and evaluation metrics.  
- **Streamlit App**: Interactive UI for generating and visualizing AI-generated anime faces.  
- **Deployment on Hugging Face**: Access the model through a simple web-based interface (https://huggingface.co/spaces/HussainAhmed10/This_Anime_Face_Does_not_Exist)

## 📂 Contents  
- **DCGAN Training Notebook**: Code to train and fine-tune the model.  
- **Pretrained Model**: Save and load trained weights.  
- **Streamlit App**: Python script for user-friendly deployment.  

## 💻 Installation & Usage  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/HussainAhmed10/This-Anime-Face-Does-Not-Exist.git  
   cd This-Anime-Face-Does-Not-Exist  
   ```  
2. Install dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  
3. Run the Streamlit app:  
   ```bash  
   streamlit run app.py  
   ```  

## 📸 Sample Results  
![Epoch-wise_Results](https://github.com/user-attachments/assets/32d44fcf-c058-4573-93b3-b5dd478f435c)




## 📜 Acknowledgments  
Inspired by [This Person Does Not Exist](https://thispersondoesnotexist.com/) and anime dataset sources. Built with **PyTorch, Streamlit, and Hugging Face Spaces**.  
