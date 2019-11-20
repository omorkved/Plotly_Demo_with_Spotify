#!/bin/bash
echo "Installing Plotly"
echo `pip install -r requirements.txt`
echo "Running sample"
echo `python readdata.py SampleStreamingHistory.json`