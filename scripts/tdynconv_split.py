import sys
import os
import json

if __name__ == '__main__':
    folder = sys.argv[1]

    split_dict = json.loads(open("data/XSum-TRAINING-DEV-TEST-SPLIT-90-5-5.json").read())
    data_dict = {}
    data_types = ["test", "validation", "train"]

    output_directory = "data/bbc-split"
    os.system("mkdir -p " + output_directory)

    # Reverse split dict
    for dtype in data_types:
        for doc_id in split_dict[dtype]:
            data_dict[doc_id] = dtype

    # Read files in folder
    summ_folder = os.path.join(os.getcwd(), folder, 'firstsentence')
    doc_folder = os.path.join(os.getcwd(), folder, 'restbody')

    output = {
        'train': {'doc': [], 'summ': []},
        'validation': {'doc': [], 'summ': []},
        'test': {'doc': [], 'summ': []}
    }

    for summ_file in os.listdir(summ_folder):
        doc_id = summ_file.split('.')[0]
        # print('Processed document {}'.format(doc_id))
        summ_infile = open(os.path.join(summ_folder, summ_file))
        doc_infile = open(os.path.join(doc_folder, '{}.{}'.format(doc_id, 'restbody')))
        if doc_id not in data_dict:
            print('{} not found'.format(doc_id))
            continue
        doc = []
        for sent in doc_infile.readlines():
            doc.append(sent.lower().strip())
            if len(doc) > 400:
                break
        doc = ' '.join(doc)
        summ = ' '.join([sent.lower().strip() for sent in summ_infile.readlines()])
        output[data_dict[doc_id]]['doc'].append(doc)
        output[data_dict[doc_id]]['summ'].append(summ)
        summ_infile.close()
        doc_infile.close()

    for dtype in data_types:
        summ_file = open(os.path.join(
            output_directory, '{}.summary'.format(dtype)), 'w')
        doc_file = open(os.path.join(
            output_directory, '{}.document'.format(dtype)), 'w')
        summ_file.write('\n'.join(output[dtype]['summ']))
        doc_file.write('\n'.join(output[dtype]['doc']))
        summ_file.close()
        doc_file.close()

