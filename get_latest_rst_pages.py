from os import path
from os import listdir
import shutil

filename = 'rst_pages.txt'
filename2 = 'source_rst_pages.txt'
path2source = 'openvino/build/docs/rst'
path2target = 'pages'

prefixes = ['openvino_2_0_','openvino_docs_','openvino_inference_engine_','ovsa_','pot_','resources','workbench_docs_','openvino_deployment','accuracy_','deprecated','documentation','docs_nncf_introduction','get_started']

def compare_to_source_rst():
    with open(filename,'r') as f:
        files = f.readlines()
        dne_total_count = 0
        missing_rst_files = []
        missing_png_files = []
        for file2update in files:
            updatePath = path.join(path2source,file2update).rstrip()
            if path.isfile(updatePath):
                print("Exists: " + updatePath)
            else:
                dne_total_count += 1
                if updatePath.endswith('.rst'):
                    missing_rst_files.append(updatePath)
                elif updatePath.endswith('.png'):
                    missing_png_files.append(updatePath)
        print("Doesn't exist count: " + str(dne_total_count))
        print("Number of missing png files: " + str(len(missing_png_files)))
        print("Number of missing rst files: " + str(len(missing_rst_files)))
        print(missing_rst_files)

def find_all_rst_files_with_prefix():
    pages_found = []
    files_in_source_dir = listdir(path2source)
    for thing in files_in_source_dir:
        if thing.endswith('.rst'):
            for prefix in prefixes:
                if thing.startswith(prefix):
                    pages_found.append(thing)
    return pages_found

def get_rst_pages(pages):
    for page in pages:
        source_page_path = path.join(path2source,page)
        target_page_path = path.join(path2target,page)
        shutil.copy(source_page_path,target_page_path)

def compare_rst_files_in_source_and_output():
    files = []
    files2 = []
    with open(filename,'r') as f:
        files = f.readlines()
    with open(filename2,'r') as f2:
        files2 = f2.readlines()

    files = [i.rstrip() for i in files]
    files2 = [i.rstrip() for i in files2]

    print("***************************************")
    print("Checking for files missing in source ...")
    print("***************************************")

    for rstfile in files:
        if rstfile.endswith('.rst'):
            if rstfile not in files2:
                print(rstfile)

    print("***************************************")
    print("Checking for files missing in docs repo files ...")
    print("***************************************")

    for rstfile in files2:
        if rstfile not in files:
            print(rstfile)

# compare_to_source_rst()
rst_pages = find_all_rst_files_with_prefix()
get_rst_pages(rst_pages)

# compare_rst_files_in_source_and_output()