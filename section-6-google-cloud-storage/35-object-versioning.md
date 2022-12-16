
# Object Versioning

  - Help to prevent accidental deletion of object

  - Enable/Disable versioning at bucket level

  - Get access to an older version with (object key + version number)

  - if you dont specify version number, always retrieve latest version


## commands

  - gsutil cp hello.txt gs://my-first-bucket-gcp-course-123123 (copy file to bucket)

  - gsutil ls gs://my-first-bucket-gcp-course-123123 (view all files)

  - gsutil ls -a gs://my-first-bucket-gcp-course-123123 (view all files at every version point)

  - gsutil rm gs://my-first-bucket-gcp-course-123123/hello.txt (remove file)
