import boto3

# Criar um cliente para interagir com o AWS S3
/#s3_client = boto3.client('s3')
#
#files = ['matricula_co.CSV','matricula_nordeste.CSV','matricula_norte.CSV','matricula_sudeste.CSV','matricula_sul.CSV']
#
#try:
#    for fl in files:
#        s3_client.upload_file("../dados/microdados_educacao_basica_2020/DADOS/"+fl,
#                              "datalake-tancredo-dfinal1-edc-producao-421168935276",
#                              "raw-data/"+fl)
#except NameError:
#    print(NameError)
#
#
#
#
import boto3
#import pandas as pd

#Criar um cliente para interagir com o QWS S3
s3_client = boto3.client('s3')

s3_client.upload_file("../dados/microdados_educacao_basica_2020/DADOS/matricula_co.CSV",
                    "datalake-tancredo-dfinal1-edc-producao-421168935276",
                    "raw-data/matricula_co.CSV"
                    )
