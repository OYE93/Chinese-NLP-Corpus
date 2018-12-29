"""
transform conll data with segmentation information to sample conll data
author: Ouyang En
"""

raw_data_file_list = ["weiboNER_2nd_conll.train", "weiboNER_2nd_conll.dev", "weiboNER_2nd_conll.test"]
for data_file in raw_data_file_list:
    output_file = "simple_" + data_file
    f_out = open(output_file, "w", encoding='utf8')
    with open(data_file, "r", encoding='utf8') as f:
        for line in f.readlines():
            line = line.strip()
            if line != "":
                span_list = line.split('\t')
                raw_char = ''.join(list(span_list[0])[:-1])
                tag = span_list[-1]
                f_out.write(' '.join([raw_char, tag]) + '\n')
            else:
                f_out.write('\n')
