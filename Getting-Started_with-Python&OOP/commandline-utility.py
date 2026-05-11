import argparse
parser = argparse.ArgumentParser()

# Add command line arguments
parser.add_argument("url",help="url of the file to download")
parser.add_argument("output",help="by which name do you want to save your file")

# parse the arguments
args = parser.parse_args()

# use the argumets in the code
print(args.url)
print(args.output)
download_file(args.url,args.output)