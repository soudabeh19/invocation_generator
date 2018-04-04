#!/user/bin/env python
import os,sys
import logging
from argparse import ArgumentParser
def parse_file (input_file):
    with open (input_file, 'r') as f:
        content = f.readlines()
        content = [x.strip() for x in content]
    return content
def write_file (subject,output_base_path):
    diff_file = open(output_base_path+str(subject)+".json",'w')
    content = "{\n"+'\t"subject_folder": "$HOME/projects/def-glatard/hcp-results/PreFreeSurfer/CentOS5/'+str(subject)+'",\n' + '\t"execution_name": "demo-FS"  \n' + "}"
    diff_file.write(content)

def main (args=None):
    parser=ArgumentParser("invoc_generator.py" )
    parser.add_argument("input_file")# input file
    #parser.add_argument("path")# path directory of subjects
    parser.add_argument("base_name")# It's better to name it invocation
    parser.add_argument("output_folder")# to make folder 
    args=parser.parse_args()
    lines=parse_file(args.input_file)   
    if args.base_name is not None and args.output_folder is not None:
        if not os.path.exists(args.output_folder):
            os.makedirs(args.output_folder)
    output_base_path=args.output_folder+"/"+args.base_name
    for subject in lines:
        write_file (subject,output_base_path)

if __name__ =='__main__':
    main()
