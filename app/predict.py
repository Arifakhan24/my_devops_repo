#!/usr/bin/python3
# -*- coding: utf-8 -*-

import torch
import torchvision.transforms as transforms
from config import CONFIG
import numpy as np
from PIL import Image


def preprocess(package: dict, input: list) -> list:
    """
    Preprocess data before running with model, for example scaling and doing one hot encoding

    :param package: dict from fastapi state including model and preocessing objects
    :param package: list of input to be proprocessed
    :return: list of proprocessed input
    """

    # scale the data based with scaler fit during training
    scaler = package['scaler']
    input = scaler.transform(input)

    return input


def predict(package: dict, input: list):
    """
    Run model and get result

    :param package: dict from fastapi state including model and preocessing objects
    :param package: list of input values
    :return: numpy array of model output
    """
    mean = [0.5, 0.5, 0.5]
    std = [0.5, 0.5, 0.5]
    val_transform=transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean,std)
    ])
    # process data
    X = input#preprocess(package, input)

    # run model
    model = package['model']
    image_path = X[6]
    print("filename = ",image_path)
    
    img = Image.open("tests/"+image_path)
    img = val_transform(img)
    with torch.no_grad():
        # convert input from list to Tensor
        # move tensor to device
        print("Device - ", CONFIG['DEVICE'])
        img = img.unsqueeze(0).to(CONFIG['DEVICE'])

        # run model
        y_pred = model(img)

    # convert result to a numpy array on CPU
    predicted_EXP = torch.argmax(y_pred['EXP'],1).item()
    predicted_ICM = torch.argmax(y_pred['ICM'],1).item()
    predicted_TE = torch.argmax(y_pred['TE'],1).item()

    
    mapping={0:'A',1:'B',2:'C',3:'ND'}
    mapped_predicted_EXP = predicted_EXP+1
    mapped_predicted_ICM = mapping.get(predicted_ICM,predicted_ICM)
    mapped_predicted_TE = mapping.get(predicted_TE,predicted_TE)
    combined_prediction = str(mapped_predicted_EXP)+mapped_predicted_ICM+mapped_predicted_TE
    return combined_prediction
