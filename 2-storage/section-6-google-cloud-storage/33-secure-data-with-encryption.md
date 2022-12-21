
# Secure Data With Encryption

## Encryption

  - Google Managed Encryption Keys
    * No Configuration
    * Fully Managed

  - Customer Managed Encryption Keys
    * Create Keyring in Cloud KMS
    * key will be managed by customer, like key rotation
    
  - Customer supplied Encryption keys
    * we will generate key with: openssl rand=base64 32
    * gsutil - encrypt with CSEK
