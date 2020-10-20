__Author__ = "Aaron DeGrave"
import zlib
import tarfile
import argparse
import io
import json

parser = argparse.ArgumentParser()
parser.add_argument("file", help = "Point me to the file", type=str)
parser.add_argument("--chunk", help="enter int chunk size in bytes", type=int)
args = parser.parse_args()

with open(args.file, 'rb') as f:
    b = 0
    for data in f:
        if args.chunk:
            b = b + 1
            f.seek(24)
            data= f.read(args.chunk*b)
            continue
        else:
            f.seek(24)
            data=f.read()
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