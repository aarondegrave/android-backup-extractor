__Author__ = "Aaron DeGrave"
import zlib
import tarfile
import argparse
import io
import json

parser = argparse.ArgumentParser()
parser.add_argument("file", help = "Point me to the file", type=str)
args = parser.parse_args()

with open(args.file, 'rb') as f:
    b = 0
    for data in f:
        n= 4096
        b = b + 1
        f.seek(24)
        data= f.read(n*b)
        continue
    stream = zlib.decompress(data)
    tar = tarfile.open(fileobj=io.BytesIO(stream))
    members = tar.getmembers()
    for member in members:
        try:
            a = tar.extractfile(member)
            data = a.read()
            with open('file.tar', 'ab') as c:
                c.write(data)
            print(data)
        except AttributeError as e:
            continue
        except UnicodeDecodeError as e:
            continue