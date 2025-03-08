# Fashion Product Attribute Prediction

This project involves training a deep learning model to predict the attributes of fashion products, such as color, type, season, and gender, based on product images. The model is deployed using Flask and Streamlit for easy interaction.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Dataset](#dataset)
3. [Requirements](#requirements)
4. [Repository Structure](#repository-structure)
5. [Setup](#setup)

## Project Overview
The goal of this project is to build a deep learning model that can predict the following attributes of a fashion product:
- **Color**
- **Type** (e.g., T-shirt, shoes, dress)
- **Season** (e.g., summer, winter)
- **Gender** (e.g., men, women, unisex)

The model is trained on the [Fashion Product Images Dataset](https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-dataset) and deployed using Flask and Streamlit.

## Dataset
The dataset contains:
- **Images**: Product images in `.jpg` format.
- **Metadata**: A CSV file (`styles.csv`) with product attributes.

Download the dataset from [Kaggle](https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-dataset).

## Requirements
To run this project, you need the following:
- Python 3.8 or higher
- Libraries listed in `requirements.txt`

## Repository Structure

CodeMonk_Assignment/
├── data/
│   ├── images/                  
│   └── styles.csv               
├── notebooks/
│   └── codemonk-assignment-nb.ipynb  
├── models/
│   ├── fashion_cnn_model_tensorflow.h5
│   └── label_encoders.pkl     
├── apiserver_and_application/
│   ├── Flask_server.py  
│   └── label_encoders.pkl
├── requirements.txt
└── README.md                   

## Set Up
Clone this repository:
```bash
git clone https://github.com/Preetpatel30112002/Product_Metadata_Prediction-CodeMonkAssignment.git
cd Product_Metadata_Prediction-CodeMonkAssignment


