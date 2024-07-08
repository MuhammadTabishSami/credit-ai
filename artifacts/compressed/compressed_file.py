import gzip
import shutil

# Compress train.csv
with open('artifacts/train.csv', 'rb') as f_in:
    with gzip.open('artifacts/train.csv.gz', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

# Compress data.csv
with open('artifacts/data.csv', 'rb') as f_in:
    with gzip.open('artifacts/data.csv.gz', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
