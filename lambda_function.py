import json
import sys
import entity_extractor

print('Loading function')


def lambda_handler(event, context):
    # print("Received event: " + json.dumps(event, indent=2))
    print("text = " + event['text'])
    return entity_extractor.extract_entities(event['text'])
    # raise Exception('Something went wrong')


if __name__ == '__main__':
    # print(len(sys.argv))
    # print(sys.argv)
    print(entity_extractor.extract_entities(sys.argv[1]))