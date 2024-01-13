#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from fastapi.testclient import TestClient

from ..main import app


@pytest.fixture
def client():
    # use "with" statement to run "startup" event of FastAPI
    with TestClient(app) as c:
        yield c


def test_main_predict(client):
    """
    Test predction response
    """

    headers = {}
    body = {
        "patient_age":'32',
        "biopsy_date":'23-10-2022',
        "sample_acession_number":'51343CF1',
        "embryo_grade":'3NDND',
        "donor_type":'None',
        "ivf_icsi":0,
        "file_url":'0102_03.png',
        "biopsy_type":'NA',
        "embryo_culture":'Single',
        "patient_bmi":26.2
    }
    response = client.post("/api/v1/embryos/store",
                           headers=headers,
                           json=body)
    
    try:
        assert response.status_code == 200
        reponse_json = response.json()
        print("JSONREsponse",reponse_json)
        assert reponse_json['error'] == False

    except AssertionError:
        print(response.status_code)
        print(response.json())
        raise
