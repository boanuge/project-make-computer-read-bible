import timeit
import argparse
from src.utils import setup_dbqa

# Prerequisite : $ pip install -r ./src/requirements.txt
# Your query may take about one minute for the answer.
# $ python wwhss.py --query "Who is Holy Spirit?"

def main():
    parser = argparse.ArgumentParser(description='Query the DBQA system.')
    parser.add_argument('--query', type=str, help='The query for the DBQA system.')

    args = parser.parse_args()

    if not args.query:
        print("Please provide a query following the --query option within double quotation marks.\nFor example: $ python wwhss.py --query \"Who is Holy Spirit?\"")
        return

    # Setup DBQA
    start = timeit.default_timer()
    dbqa = setup_dbqa()

    # Query the DBQA system
    response = dbqa({'query': args.query})
    end = timeit.default_timer()

    # Print the result
    print('='*80)
    print(f'Answer:\n{response["result"]}')
    print('='*80)

    # Process source documents
    source_docs = response['source_documents']
    for i, doc in enumerate(source_docs):
        print(f'Reference text:\n{doc.page_content}')
        print(f'Source data:\n{doc.metadata["source"]}')
        print('='*80)

    print(f"Time(in seconds) to retrieve the answer: {end - start}")

if __name__ == "__main__":
    main()
