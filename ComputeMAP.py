
import sys
import json
import MAP

def load_frs_score_dict_from_file(file_path):
    with open(file_path) as f:
        lines = f.readlines()

    frs_score_dict={}
    for l in lines:
        l=l.replace('\n','')
        splitted_l=l.split('\t')
        morphed_image_name=splitted_l[0]
        if morphed_image_name in frs_score_dict:
            morphed_image_score_dict=frs_score_dict[morphed_image_name]
        else:
            morphed_image_score_dict={}
            frs_score_dict[morphed_image_name]=morphed_image_score_dict

        subject_id=splitted_l[1]
        
        subject_scores=[]
        for s in splitted_l[2:]:
            subject_scores.append(float(s))

        morphed_image_score_dict[subject_id]=subject_scores

    return frs_score_dict

def check_score_dict_consistency(frs_score_dict_list):
    for frs_score_dict in frs_score_dict_list[1:]:
        if frs_score_dict_list[0].keys()!=frs_score_dict.keys():
            print('Error: not all files contain the scores of the same morphed images')
            exit()
        else:
            for morphed_image_name in frs_score_dict_list[0]:
                for subject_id in frs_score_dict_list[0][morphed_image_name]:
                    if subject_id not in frs_score_dict[morphed_image_name]:
                        print('Error: not all files contain the same subject attempts')
                        exit()

def select_subset_from_frs_score_dict(frs_score_dict,subset_search_pattern):
    subset_frs_score_dict={}
    for morphed_image in frs_score_dict:
        if subset_search_pattern in morphed_image:
            subset_frs_score_dict[morphed_image]=frs_score_dict[morphed_image]
    return subset_frs_score_dict

def print_map(map):
    attempt_count,frs_count=map.shape

    for frs_idx in range(frs_count):
        print('\t{}'.format(frs_idx+1),end = '')
    print()

    for attempt_idx in range(attempt_count):
        print('{}'.format(attempt_idx+1),end = '')
        for frs_idx in range(frs_count):
            print('\t{:.1%}'.format(map[attempt_idx,frs_idx]),end = '')
        print()

def save_map_to_text_file(file_path,map,morph_image_count):
    attempt_count,frs_count=map.shape

    with open(file_path, 'w') as f:
        for frs_idx in range(frs_count):
            f.write('\t{}'.format(frs_idx+1))
        f.write('\n')

        for attempt_idx in range(attempt_count):
            f.write('{}'.format(attempt_idx+1))
            for frs_idx in range(frs_count):
                f.write('\t{}'.format(map[attempt_idx,frs_idx]))
            f.write('\n')
        f.write('Image count:\t{}'.format(morph_image_count))

def main():
    args = sys.argv[1:]

    if len(args)!=3:
        print('Syntax error.\nUse: ComputeMAP <input_folder_path> <output_folder_path> <frs_info_file_path>')
        return

    input_folder_path=args[0]
    output_folder_path=args[1]
    frs_info_file_path=args[2]

    frs_infos = json.load(open(frs_info_file_path, 'r'))

    print('Load scores')
    frs_score_dict_list=[]
    frs_thr_list=[]
    frs_is_similarity_list=[]
    for frs_name in frs_infos:
        input_file_path='{}/{}.txt'.format(input_folder_path,frs_name)
        frs_score_dict_list.append(load_frs_score_dict_from_file(input_file_path))
        frs_thr_list.append(frs_infos[frs_name][0])
        frs_is_similarity_list.append(frs_infos[frs_name][1])

    print('Score consistency check')
    check_score_dict_consistency(frs_score_dict_list)

    print('MAP computation')
    map,map_count=MAP.compute_map(frs_score_dict_list,frs_thr_list,frs_is_similarity_list)
    print_map(map)
    save_map_to_text_file('{}/MAP.txt'.format(output_folder_path),map,len(frs_score_dict_list[0].keys()))
    save_map_to_text_file('{}/MAPCount.txt'.format(output_folder_path),map_count,len(frs_score_dict_list[0].keys()))

if __name__ == '__main__':
    main()