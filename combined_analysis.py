from argparse import ArgumentParser
import pandas as pd
import logging
import os

def parse_args():
    """Parse command line arguments."""
    parser = ArgumentParser(description='Run analysis')
    add_arg = parser.add_argument    
    add_arg('-r', '--run', type=int, default=None, help='run number')
    add_arg('--start', type=int, default=None, help='start run number')
    add_arg('--stop', type=int, default=None, help='stop run number')
    #add_arg('-g', '--geoid', type=int, help='geoid number', required=True)
    add_arg('-n', help='number of events', type=int, default = 50000)
    add_arg('-c', '--comment', type=str, help='comment to output file name')
    add_arg('-f', '--framework', type=str, default='', help='framework to be used for analysis. corry or tbsw')
    add_arg('--file', type=str, default='export_with_text.csv', help='path to csv file')
    add_arg('--col_start', type=str, default='0', help='start column ROI plotting')
    add_arg('--col_stop', type=str, default='512', help='stop column ROI plotting')
    add_arg('--row_start', type=str, default='0', help='start row ROI plotting')
    add_arg('--row_stop', type=str, default='512', help='stop row ROI plotting')
    add_arg('--tbsw_workspace', type=str, default='~/workspace-test/', help='path to scan_runs.sh and plot_runs.sh')
    add_arg('--datapath', type=str, default='~/', help='datapath to txt files for tbsw')


    return parser.parse_args()


def get_information(csv_path,run):

    run = str(run)
    df = pd.read_csv(csv_path,encoding = 'unicode_escape',on_bad_lines='skip',sep=';')
    geoid = df.loc[(df['Run no']==run)&(df['Type']=='Run')]['ConfigID']
    geoid = str(int(geoid))
    text = str(df.loc[(df['ConfigID']==geoid) & (df['Type']=='ConfigID')]['Text'])
    beam_energy = str(text.split('Beam Energy:')[1][0:1])

    return geoid,beam_energy

if __name__ == '__main__':
    caltag = ''

    args = parse_args()
    params = []
    if args.run:
        params.append(get_information(args.file,args.run))
    elif args.start and args.stop:
        for run in range(args.start,args.stop+1,1):
            params.append(get_information(args.file,run))
    else:
        logging.error('No run number given')

    if args.framework.lower() == 'corry':
        if args.run:
            os.system(f'python3 analyze.py -r {args.run} -g {params[0][0]} -n {args.n}')
        elif args.start and args.stop:
            for i,run in enumerate(range(int(args.start), int(args.stop)+1)):
                os.system(f'python3 analyze.py -r {str(run)} -g {params[i][0]} -n {args.n}')
    elif args.framework.lower() == 'tbsw':
        if args.run:
            os.system(f'bash {args.tbsw_workspace}scan_runs.sh {args.run} {args.run} gear{params[0][0]}.xml {caltag} {args.datapath}')
            os.system(f'bash {args.tbsw_workspace}plot_runs.sh {args.run} {args.run} {args.col_start} {args.col_stop} {args.row_start} {args.row_stop}')
        elif args.start and args.stop:
            for i,run in enumerate(range(int(args.start), int(args.stop)+1)):
                os.system(f'bash {args.tbsw_workspace}scan_runs.sh {str(run)} {str(run)} gear{params[i][0]}.xml {caltag} {args.datapath}')
                os.system(f'bash {args.tbsw_workspace}plot_runs.sh {str(run)} {str(run)} {args.col_start} {args.col_stop} {args.row_start} {args.row_stop}')
    else:
        logging.error(f'{args.framework}??? We dont do that here. Please choose tbsw or corry.')                
