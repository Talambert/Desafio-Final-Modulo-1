import boto3
import pandas as pd

#Criar um cliente para interagir com o QWS S3
s3_client = boto3.client('s3')

s3_client.upload_file("..\dados\microdados_educacao_basica_2020\DADOS\matricula_co.CSV",
                    "datalake-tancredo-df1-edc-producao-421168935276",
                    "raw-data/matricula_co.CSV"
                    )
s3_client.upload_file("..\dados\microdados_educacao_basica_2020\DADOS\matricula_nordeste.CSV",
                    "datalake-tancredo-df1-edc-producao-421168935276",
                    "raw-data/matricula_nordeste.CSV"
                    )

s3_client.upload_file("..\dados\microdados_educacao_basica_2020\DADOS\matricula_norte.CSV",
                    "datalake-tancredo-df1-edc-producao-421168935276",
                    "raw-data/matricula_norte.CSV"
                    )

s3_client.upload_file("..\dados\microdados_educacao_basica_2020\DADOS\matricula_sudeste.CSV",
                    "datalake-tancredo-df1-edc-producao-421168935276",
                    "raw-data/matricula_sudeste.CSV"
                    )

s3_client.upload_file("..\dados\microdados_educacao_basica_2020\DADOS\matricula_sul.CSV",
                    "datalake-tancredo-df1-edc-producao-421168935276",
                    "raw-data/matricula_sul.CSV"
                    )



                    







##df = pd.read_csv("..\dados\microdados_educacao_basica_2020\DADOS\gestor.csv", sep="|")
##print(df)


##s3_client.upload_file("..\dados\microdados_educacao_basica_2020\DADOS\*.txt",
  ##                  "datalake-tancredo-igti-edc",
    ##                "data/gestor.csv"
      ##              )