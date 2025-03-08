# Product_Metadata_Prediction-CodeMonkAssignment-

# Fashion Product Attribute Prediction

This project involves training a deep learning model to predict the attributes of fashion products, such as color, type, season, and gender, based on product images. The model is deployed using Flask and Streamlit for easy interaction.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Dataset](#dataset)
3. [Requirements](#requirements)
4. [Setup](#setup)
5. [Training the Model](#training-the-model)
6. [Deployment](#deployment)
7. [Results](#results)
8. [Repository Structure](#repository-structure)
9. [License](#license)

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

Install the required libraries using:
```bash
pip install -r requirements.txt
