
# Signed URL

  - temporary access

  - you can give access to a user who does not have a google account

  - URL expired after time period is defined.

  - Max period for which URL is valid is 7 days.

  - create url command: "gsutil signurl -d 10m -u gs://<bucket>/<object>" (for 10 min access link)
    or "gsutil signurl -d 60s signed-key.json gs://gcp-course-signed-url/uniform.txt"
