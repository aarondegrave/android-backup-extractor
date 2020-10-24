__Author__ = "Aaron DeGrave"
import zlib
import tarfile
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", help = "Point me to the file", type=str)
args = parser.parse_args()

with open(args.file, 'rb') as f:
    b = 0
    for data in f:
        f.seek(24)
        data= f.read()
        stream = zlib.decompress(data)
        with open ("tarfile.tar", "ab") as e:
            e.write(stream)
        continue
        e.close()