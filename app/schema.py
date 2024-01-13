#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field


class EmbryoGradingInput(BaseModel):
    """
    Input values for model inference
    """
    patient_age: str = Field(..., example='32', title='Patient Age')
    biopsy_date: str = Field(..., example='mm-dd-yyyy', title='Biopsy Date (mm-dd-yyyy)')
    sample_acession_number: str = Field(..., example='512631C1', title='Sample Acession Number')
    embryo_grade: str = Field(..., example='5AA', title='Embryo Grade')
    donor_type: str = Field(...,example='None',title='Donor Type')
    ivf_icsi: int=Field(...,example=0,title='IVF ICSI')
    file_url:str=Field(...,example='file path to S3',title='File Path to AWS S3 Bucket')
    biopsy_type:str=Field(...,example='',title='Biopsy Type')
    embryo_culture:str=Field(...,example='Group',title='Embryo Culture')
    patient_bmi:float=Field(...,example=28.4,title='Patient BMI')


class EmbryoGradingResult(BaseModel):
    """
    Inference result from the model
    """
    ai_embryo_grade: str


class EmbryoGradingResponse(BaseModel):
    """
    Output response for model inference
    """
    error: bool = Field(..., example=False, title='Whether there is error')
    message:str
    results: EmbryoGradingResult = ...


class ErrorResponse(BaseModel):
    """
    Error response for the API
    """
    error: bool = Field(..., example=True, title='Whether there is error')
    message: str = Field(..., example='', title='Error message')
    traceback: str = Field(None, example='', title='Detailed traceback of the error')
