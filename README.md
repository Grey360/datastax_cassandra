# Getting started with [Datastax Astra](https://astra.datastax.com)

## Credentials and the SCB

1. Replace the `username` and `password` fields in `config.yam.sample` file.
2. Replace the `secure-connect-bundle` value to point to your [Secure Connect Bundle](https://datastax-cluster-config-prod.s3.us-east-2.amazonaws.com/69fcdbcd-0b45-42ed-b963-89f4cea7d08f/secure-connect-cassandra-0.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA2AIQRQ76TUCOHUQ4%2F20201129%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Date=20201129T141333Z&X-Amz-Expires=300&X-Amz-SignedHeaders=host&X-Amz-Signature=7b862942f095d3b1148896c02239fbd16dbd82005b8b71191dc481e7047b4983) `zip` file.
3. Rename `config.yaml.sample` to `config.yaml`.
4. Run `connect_database.py`: `python ./connect_database.py`
5. The console output displays the `release_version` from the `system.local`.
