resource "aws_s3_bucket_object" "upload" {
  bucket = aws_s3_bucket.dldesafio.id
  key    = "emr-code/pyspark/upload.py"
  acl    = "private"
  source = "../etl/upload.py"
  etag   = filemd5("../etl/upload.py")
}

resource "aws_s3_bucket_object" "job_spark_etl1" {
  bucket = aws_s3_bucket.dldesafio.id
  key    = "emr-code/pyspark/job_spark_etl1.py"
  acl    = "private"
  source = "../etl/job_spark_etl1.py"
  etag   = filemd5("../etl/job_spark_etl1.py")
}

 