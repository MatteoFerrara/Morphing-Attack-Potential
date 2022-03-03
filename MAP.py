
import numpy as np

max_attempt_count=50

def compute_map_count(frs_score_dict_list,frs_thr_list,frs_is_similarity_list):
    morphed_image_names=frs_score_dict_list[0].keys()

    overall_min_attempt_count=max_attempt_count
    morph_frs_min_valid_attempt_count=np.full((len(morphed_image_names),len(frs_score_dict_list)),max_attempt_count)
    for morphed_idx,morphed_image_name in enumerate(morphed_image_names):
        for frs_idx in range(len(frs_score_dict_list)):
            for subject_id, subject_scores in frs_score_dict_list[frs_idx][morphed_image_name].items():
                overall_min_attempt_count=min(overall_min_attempt_count,len(subject_scores))
                subject_valid_attempt_count=sum(compare(s,frs_thr_list[frs_idx],frs_is_similarity_list[frs_idx]) for s in subject_scores)
                morph_frs_min_valid_attempt_count[morphed_idx,frs_idx]=min(subject_valid_attempt_count,morph_frs_min_valid_attempt_count[morphed_idx,frs_idx])

    map_count=np.zeros((overall_min_attempt_count,len(frs_score_dict_list)),dtype=int)
    for morphed_idx in range(len(morphed_image_names)):
        sorted_frs_min_valid_attempt_count=np.sort(morph_frs_min_valid_attempt_count[morphed_idx])
        for frs_count in range(len(frs_score_dict_list)):
            min_valid_attempt_count=sorted_frs_min_valid_attempt_count[-1-frs_count]
            for k in range(min_valid_attempt_count):
                map_count[k,frs_count]+=1

    return map_count
 
def compute_map(frs_score_dict_list,frs_thr_list,frs_is_similarity_list):
    map_count=compute_map_count(frs_score_dict_list,frs_thr_list,frs_is_similarity_list)
    map=map_count/len(frs_score_dict_list[0].keys())
    return map,map_count

def compare(s,thr,is_similarity):
    if is_similarity:
        return s>thr
    else:
        return s<thr
