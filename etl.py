import boto3
import requests
import pandas as pd


def extract_from_api():
    resp = requests.get('https://example.com/api/data')
    return resp.json()


def load_csv(file):
    return pd.read_csv(file)


def transform_data(data):
    # Validate, cleanse data
    return data


def load_data(data):
    # Insert into database
    database.insert_data(data)

def get_microbiome_data():
    # Connect to S3 bucket with sequence files
    s3 = boto3.client('s3')

    # Download fastq files
    s3.download_file('bucket', 'sample1.fq', 'sample1.fq')
    s3.download_file('bucket', 'sample2.fq', 'sample2.fq')

    # Run through annotation pipeline
    results = annotate_microbiome(fastq_files)

    return results


def annotate_microbiome(files):
    # QC with FastQC
    # Taxonomic classification with Kraken2
    # Functional annotation with HUMAnN
    # Diversity analysis with QIIME2

    return annotated_data