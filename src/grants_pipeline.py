from functions.extract import extract
from functions.transform import transform
from functions.load import load

def main():
    df = extract("grants_samplesource.csv")
    df = transform(df)
    load(df)

if __name__ == "__main__":
    main()
