import requests
import argparse

def main():
    parser = argparse.ArgumentParser(
                    prog='PyDictor',
                    description='Show the weather in the terminal')
    parser.add_argument('address', help='Address to check the weather')
    args = parser.parse_args()
    print(args.address) 
    l = "en-US"
    x = requests.get(f"https://nominatim.openstreetmap.org/search?q={args.address}&accept-language={l}&limit=1&format=jsonv2")
    print(x.json())

if __name__ == "__main__":
    main()
