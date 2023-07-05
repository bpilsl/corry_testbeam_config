import re
import glob
import os 

corry_bin = '~/vtx/corryvreckan/bin/corry'
data_folder = '../VTX/data_producer_runs/desy'
output_dir = '../corry_textwriter_dump'
corry_config_template = 'filewriter_tbsw.conf'
data_in_files = glob.glob(data_folder + '/*.raw')

print(data_in_files)

number_of_events = 50000
force_processing = False


out_files = glob.glob(output_dir +'/*.txt')



available_runs_mpx2 = {}
available_runs_tel = {}

alrdy_processed_runs = []

run_nmb = None
for file in data_in_files:
    m = re.search(r'run(\d+)', file)
    run_nmb = int(m.group(1))
    m = re.search(f'run000*{run_nmb}+_monopix2.', file)
    if m:
        available_runs_mpx2[run_nmb] = file
    m = re.search(f'run000*{run_nmb}+_adenium.', file)
    if m:
        available_runs_tel[run_nmb] = file
    



for file in out_files:
    m = re.search(r'run(\d+)', file)
    # print('out = ', file, ' match = ', m)
    if m:
        alrdy_processed_runs.append(int(m.group(1)))


available_nmb = []

for nmb in available_runs_mpx2.keys():

    available_nmb.append(nmb)


diff = list(set(available_runs_mpx2.keys()) - set(alrdy_processed_runs))

# print('avail ', available_runs_mpx2.keys())

# print('proc ', alrdy_processed_runs)
print('diff = ', diff)

files_to_process = []

print('tel_keys= ', available_runs_tel.keys())
print('mpx2_keys= ', available_runs_mpx2.keys())

if not force_processing:
    for run in diff:
        if run in available_runs_tel.keys():
            tmp = (available_runs_mpx2[run], available_runs_tel[run])
            files_to_process.append(tmp)
        else:
            print('mpx2 file available, but no telescope file!!!!!!!!!!!')  

else:

    print('tel_keys= ', available_runs_tel.keys())
    print('mpx2_keys= ', available_runs_mpx2.keys())
    for run in available_runs_mpx2.keys():

        if run in available_runs_tel.keys():
            print(available_runs_mpx2[run], available_runs_tel[run])
            tmp = (available_runs_mpx2[run], available_runs_tel[run])

            files_to_process.append(tmp)

        else:
            print('mpx2 file available, but no telescope file!!!!!!!!!!!')

print('2proc ', files_to_process)
for f in files_to_process:
    output_file = re.search(r'run\d+', f[0]).group(0)
    mpx_f = f[0]
    tel_f = f[1]
    corry_cmd = f'{corry_bin} -c {corry_config_template} -o number_of_events={number_of_events} -o output_directory={output_dir} -o EventLoaderEUDAQ2.file_name={f[1]} -o EventLoaderEUDAQ2:Monopix2_0.file_name={f[0]} -o TextWriter.file_name={output_file}.txt'

    print('executing ', corry_cmd)
    os.system(corry_cmd)
