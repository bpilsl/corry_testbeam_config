#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# BGNet (Background prediction with neural nets for Belle II at SuperKEKB)
# Author: The BGNet developers
#
# See git log for contributors and copyright holders.
# This file is licensed under MIT licence, see LICENSE.md.
import getpass
import time
import traceback
import requests
import datetime
import pytz
#from bs4 import BeautifulSoup
import logging
import glob
#from read_h5 import readh5
import json
import pickle
import os
import sys
#sys.path.append('/home/yannik/vtx/tj-monopix2-daq/tjmonopix2/scans')


class elog():
    """
    Class to manage the upload of reports to the elog.

    Usage:
    elog('Year', 'Month', 'Day', 'Type of Report', attachments=['path/to/file',], credFileElog='path/to/credFile').uploadToElog()

    Parameters
    ----------
    year : str
        Year of report as YYYY.
    month : str
        Month of report as MM.
    day : str
        Day of report as DD.
    type : str
        Type of report to be submitted. Displayed in elog.
    attachments : list of str, default []
        List of paths to files to attach to elog report.
    username : str, default None
        Desy username to log in to elog.
    password : str, default None
        Desy password to log in to elog.
    credFile : str, default None
        Path to textfile with Desy credentials.

    See Also
    -------
    goReporter.py : Calls this class, member functions.
    """
    types = ['Run',
             'ConfigID',
             'General',
             'TJ-Scan',
             'Analysis'
             ]
    category = ['Beam',
                'Scan',
                'Test',
                'other'
                ]

    def __init__(
            self,
            configID='',
            output_data='',
            category='generic analysis',
            scanned_register='',
            comment_in_conf='',
            conf_folder='',
            run_number='0',
            type='Anaylsis',
            postMessageOfReport=False,
            attachments=None,
            username=None,
            password=None,
            credFileElog=None,
            credFileb2rc=None):
        '''Constructor.'''
        super(elog, self).__init__()
        self.type = type
        self.category = category
        self.configID = configID
        self.subject = 'Desy TB 2022 Run'
        # parameters for URL
        self.prefix = 'https'
        self.hostname = 'elog.belle2.org'
        self.port = '443'
        self.logbook = 'VTX+TJ+Monopix2+beam+test'
        if not self.logbook.startswith('elog/'):
            self.logbook = 'elog/' + self.logbook
        # 3 Options to give login credentials: text file, command prompt, keyword
        self.author = ''
        if username is None or password is None:
            if credFileElog:
                with open(credFileElog) as file:
                    lines = [line.rstrip() for line in file]
                self.username = lines[0]
                self.password = lines[1]
                try:
                    self.author = lines[2]
                except BaseException:
                    self.author = ''
            else:
                print("ELOG user credentials (DESY Account):")
                self.username = input("Username:")
                self.password = getpass.getpass("Password:")

        if self.author == '':
            #self.author = self.username
            self.author = 'Testbeam Crew'

        self.starttime = datetime.datetime.now(pytz.timezone('Europe/Berlin')).strftime("%Y/%m/%d %H:%M CET")  # Time of upload/End of run
        # Figure out endtime
        # start = datetime.datetime.strptime('{}/{}/{} 00:00'.format(year, month, day), "%Y/%m/%d %H:%M")
        # timedelta_day = datetime.timedelta(days=1)
        # timedelta_minute = datetime.timedelta(minutes=1)
        # start = start+timedelta_day-timedelta_minute
        # self.endtime = start.strftime("%Y/%m/%d %H:%M")

        self.file_text = ''  # Placeholder in case we want to write something in the report
        if attachments is not None:
            self.attachments = attachments  # Option to use shutil to validate path
        else: 
            self.attachments = []
        #self.failedElogPath = './failed_elog_uploads/'
        #self.failedElogDict = {}
        self.comment_in_conf = comment_in_conf

        #self.output_data = output_data
        # self.output_data = '/home/yannik/vtx/tj-monopix2-daq/tjmonopix2/scans/output_data'
        #if self.output_data.endswith('/'):
        #    self.output_data = self.output_data[:-1]

        #raw_dir_files = sorted(glob.glob(self.output_data+'/*.raw'))
        #h5_dir_files = sorted(glob.glob(self.output_data+'/output_data/module_0/chip_0/*scan.h5'))

        #only_date = [(i, file[-16:]) for i, file in enumerate(raw_dir_files)]
        #self.raw_dir_file = raw_dir_files[max(only_date, key=lambda item:item[1])[0]].split("/")[-1]
        #h5_dir_file = h5_dir_files[-1].split("/")[-1]
        #self.h5_dir_file = h5_dir_file
        #h5_dir_file_path = h5_dir_files[-1]
        #settings, registers, run_config, scan_config = readh5(h5_dir_file_path, ['settings', 'registers', 'run_config', 'scan_config']).run()

        #self.scan_id = run_config['scan_id']
        #self.start_column = int(scan_config['start_column'])
        #self.stop_column = int(scan_config['stop_column'])
        #self.start_column_str = scan_config['start_column']
        #self.stop_column_str = scan_config['stop_column']
        #self.device = settings['chip_sn']
        #self.registers = registers
        #self.regName = scanned_register
        #if self.regName != '':
        #    self.regVal = str(self.registers[self.regName])
        #else:
        #    self.regVal = ''
        #print('regs!!!!!!!!!!!!!', scanned_register, self.regName, self.regVal)

        self.run_number = run_number
        #if run_number != '0':
        #    self.run_number = run_number
        #else:
            #self.run_number = self.raw_dir_file.split("_")[1][3:]

        #if conf_folder == '':
        #    conf_folder = '/mnt/Disk1/VTX/data_producer_runs/run_folder'
        #    #conf_folder = '/home/yannik'
        #if conf_folder.endswith('/'):
        #    conf_folder = conf_folder[:-1]
        #conf_file_path = str(conf_folder)+'/config_run_'+str(self.run_number)+'.txt'
        #self.attachments.append(conf_file_path)
        #print(self.attachments)

        #with open(self.failedElogPath+'register_dump_for_elog_run'+self.run_number+'.txt', 'w') as dumpfile:
        #    dumpfile_name = dumpfile.name
        #    json.dump(registers, dumpfile, indent=2)

        #self.attachments.append(dumpfile_name)
        #startime is now() for analysis. Endtime not needed
        #starttime_year = h5_dir_file[0:4]
        #starttime_month = h5_dir_file[4:6]
        #starttime_day = h5_dir_file[6:8]
        #starttime_hour = h5_dir_file[9:11]
        #starttime_minute = h5_dir_file[11:13]
        # starttime_second = h5_dir_file[13:15]

        #start = datetime.datetime.strptime('{}/{}/{} {}:{} CET'.format(starttime_year, starttime_month, starttime_day, starttime_hour, starttime_minute), "%Y/%m/%d %H:%M CET")
        #self.starttime = start.strftime("%Y/%m/%d %H:%M CET")
        # print('starttime', self.starttime)
        # self.starttime = "{0}/{1}/{2} {3}:{4}:{5} CET".format(starttime_year, starttime_month, starttime_day, starttime_hour, starttime_minute, starttime_second)

        self.postMessageOfReport = False
        ''' Ignore b2rc for now
        # possible way to build different reports/define which function is used for which report
        # self.createElog = getattr(self, "create%s" % self.type)
        self.postMessageOfReport = postMessageOfReport
        self.alias = 'VTX Bot'
        self._b2rc_url = 'https://chat.belle2.org'
        self._b2rc_userid = ''
        self._b2rc_username = ''
        self._b2rc_token = ''
        self._resume = False
        self._b2rc_session = None
        self.usernameb2rc = ''
        self.passwordb2rc = ''
        #self.avatar = 'https://owncloud.gwdg.de/index.php/apps/files_sharing/ajax/publicpreview.php?x=1848&y=593&a=true&file=Selection_111.png&t=WiMaxhyNuewsmMy&scalingup=0'
        if self.postMessageOfReport:
            self._b2rc_session = requests.Session()
            self._b2rc_session.auth = requests.auth.HTTPBasicAuth('cosmic', 'running')
            if credFileb2rc:
                with open(credFileb2rc) as file:
                    lines = [line.rstrip() for line in file]
                self.usernameb2rc = lines[0]
                self.passwordb2rc = lines[1]
                try:
                    self.alias = lines[2]
                except BaseException:
                    self.alias = 'BGNet Bot'
            else:
                self.usernameb2rc = input("Username:")
                self.passwordb2rc = getpass.getpass("Password:")
    '''
    def get_frontends(self):

        frontends = ['Normal FE', 'Normal FE Casc', 'HV FE Casc', 'HV FE']
        start = 0
        end = 0
        if self.start_column < 224:
            start = 0
        elif self.start_column < 448 and self.start_column >= 224:
            start = 1
        elif self.start_column < 480 and self.start_column >= 448:
            start = 2
        elif self.start_column >= 480:
            start = 3

        if self.stop_column <= 224:
            end = 1
        elif self.stop_column <= 448 and self.stop_column > 224:
            end = 2
        elif self.stop_column <= 480 and self.stop_column > 448:
            end = 3
        elif self.stop_column > 480:
            end = 4
        return ', '.join(frontends[start:end])

    def text_template(self, data):

        self.file_text += self.comment_in_conf
        self.file_text += ' \n'
        self.file_text += self.scan_id+' with '+self.device
        self.file_text += ' \n'
        self.file_text += 'Pixels: '+self.start_column_str+':'+self.stop_column_str+' --> Frontends: ' + self.get_frontends()
        # self.file_text += json.dumps(self.registers, indent=2)
        self.file_text += ' \n'
        # self.file_text += json.dumps(data, indent=2)
        # self.file_text += ' \n'
        self.file_text += str(self.h5_dir_file)
        self.file_text += ' \n'
        self.file_text += str(self.raw_dir_file)

    def buildRequest(self):
        """
        Build requests.Request object for report.

        Put together the elog address.
        Collect data and attachments for the elog report. Data fills strings in elog.
        Attachments are media files attached to elog report.

        Returns
        -------
        request.Request
            Request object to use to open a session.
        """
        req_address = "{}://{}:{}/{}".format(self.prefix, self.hostname, self.port, self.logbook)
        auth = requests.auth.HTTPBasicAuth(self.username, self.password)

        # data = {
        #    'cmd': 'Submit',
        #    'Type': self.type,
        #    'Author': self.author,
        #    'Date': self.endtime,
        #    'Category': self.subject,
        #    'Device': self.device
        # }

        #print(self.run_number)
        data = {
            'cmd': 'Submit',
            'Date': '',
            'Author': self.author,
            'Subject': self.subject,
            'Type': self.type,
            'Category': self.category,
            'Start': self.starttime,
            #'Stop': self.endtime,
            'Run_no': self.run_number,
            'ConfigID': self.configID,
            #'Device': self.device,
            #'RegName': self.regName,
            #'RegVal': self.regVal
        }
        #self.text_template(data)
        files = [
            ('Text', self.file_text)
        ]
        for attachment in self.attachments:
            files.append(
                ('attfile', open(attachment, 'rb'))
            )
        #self.failedElogDict['req_address'] = req_address
        #self.failedElogDict['data'] = data
        #self.failedElogDict['attachments'] = self.attachments
        #self.failedElogDict['Text'] = self.file_text
        return requests.Request('POST', req_address, auth=auth, data=data, files=files)

    def uploadFailedElogs(self):
        failed_elogs = sorted(glob.glob(self.failedElogPath+'elog_run*.pkl'))
        auth = requests.auth.HTTPBasicAuth(self.username, self.password)
        upload_success = False
        print(failed_elogs)
        if len(failed_elogs) == 0:
            return
        else:
            for elog in failed_elogs:
                print(elog)
                try:
                    elog_request_dict = pickle.load(open(elog, "rb"))
                except Exception:
                    continue
                files=[]
                loaded_attachments = elog_request_dict['attachments']
                for attachment in loaded_attachments:
                    files.append(('attfile', open(attachment, 'rb')))
                files.append(('Text', elog_request_dict['Text']))
                elog_request = requests.Request('POST', elog_request_dict['req_address'], auth=auth, data=elog_request_dict['data'], files=files)
                with requests.Session() as s:
                    s.auth = elog_request.auth
                    try:
                        s.request("GET", elog_request.url)
                        prep = s.prepare_request(elog_request)
                        settings = s.merge_environment_settings(prep.url, {}, None, None, None)
                        resp = s.send(prep, **settings)
                        upload_success = resp.ok
                        if upload_success:
                            pass
                        else:
                            print('(Reupload) Timeout: Skipping rest of upload')
                            break
                    except Exception as e:
                        logging.error(traceback.format_exc())
                        print('(Reupload) Error: Skipping rest of upload')
                        break
                if upload_success:
                    print("Reupload of elog successful. Removing pickle file.")
                    os.remove(elog)

    def uploadToElog(self):
        """
        Open session and uploads report to elog.

        Call function to upload a report to the elog

        Returns
        -------
        bool
            True when upload successful, False if upload unsuccessful.
        """
        time.sleep(1)
        #self.uploadFailedElogs()
        requestToElog = self.buildRequest()
        upload_success = False
        if isinstance(requestToElog, requests.Request):
            resp = None
            with requests.Session() as s:
                s.auth = requestToElog.auth
                tries = 6
                sleep = 0.5
                for t in range(tries):
                    try:
                        s.request("GET", requestToElog.url)
                        prep = s.prepare_request(requestToElog)
                        settings = s.merge_environment_settings(prep.url, {}, None, None, None)
                        resp = s.send(prep, **settings)
                        upload_success = resp.ok
                        if upload_success:
                            break
                        else:
                            print('Timeout: Try {}/{}, sleep {}s and try again...'.format(t, tries, sleep))
                            print('Reason: {}'.format(resp.reason))
                            time.sleep(sleep)
                            continue
                    except Exception as e:
                        logging.error(traceback.format_exc())
                        print('Error: Try {}/{}, sleep {}s and try again...'.format(t, tries, sleep))
                        time.sleep(sleep)
                        continue
            if upload_success:
                print("Elog Entry successfully transmitted to:")
                print("{}".format(requestToElog.url))
                print('Attachments uploaded:')
                for attachment in self.attachments:
                    print(attachment)
                if self.postMessageOfReport:
                    print('Post message to rocket chat')
                    self.rocketChat()
            else:
                print("Error during transmitting Elog.")
                #print('Saving request object in '+self.failedElogPath)
                #os.makedirs(os.path.dirname(self.failedElogPath), exist_ok=True)
                #pickle_file = open(self.failedElogPath+'elog_run'+self.run_number+'.pkl', 'wb')
                #pickle.dump(self.failedElogDict, pickle_file)
                #pickle_file.close()
                
                return False

            return True
        else:
            print('No valid instance of requests.Request')
            return False

# #################################
# B2RC posting
# #################################
    def api_get(self, name, params=None):
        """Send GET request."""
        result = None
        success = False
        retries = 0
        while True:
            try:
                result = self._b2rc_session.get(self._b2rc_url + name, params=params)
                result.raise_for_status()
                success = True
            except Exception as e:
                logging.error(traceback.format_exc())
                time.sleep(10)
                retries += 1
            if success:
                break
            if retries >= 10:
                logging.warning('Elog timeout')
                break
        return result

    def api_post(self, name, data, files=None):
        """Send POST request."""
        result = None
        success = False
        retries = 0
        while True:
            try:
                result = self._b2rc_session.post(self._b2rc_url + name,
                                                 data=data, files=files)
                result.raise_for_status()
                success = True
            except Exception as e:
                logging.error(traceback.format_exc())
                time.sleep(10)
                retries += 1
            if success:
                break
            if retries >= 10:
                logging.warning('Elog timeout')
                break
        return result

    def logout(self):
        '''Logout from API.'''
        if not self._resume:
            self.api_get('/api/v1/logout')

    def authenticate(self, token=None):
        '''Authenticate, manage and test API session.'''
        # clear old authentication
        if self._b2rc_token:
            self.logout()
            self._b2rc_session.headers.update({'X-Auth-Token': None,
                                               'X-User-Id': None})
        if token:
            result = self.api_post('/api/v1/login', data={'resume': token})
        else:
            result = self.api_post('/api/v1/login', data={'user': self.usernameb2rc, 'password': self.passwordb2rc})
        if not result:
            logging.warning('Could not reach b2rc login')
            return False
        if result.status_code != 200 or result.json()['status'] != 'success':
            logging.warning('B2rc api: Invalid authentication')
            return False
        self._resume = (token is not None)
        self._b2rc_token = result.json()['data']['authToken']
        self._b2rc_userid = result.json()['data']['userId']
        self._b2rc_username = result.json()['data']['me']['name']
        self._b2rc_session.headers.update({'X-Auth-Token': self._b2rc_token,
                                           'X-User-Id': self._b2rc_userid})
        return True

    def get_ref_from_html(self, html):
        '''Clean html file to retrieve latest report URL.'''
        if html == []:
            logging.info('Elog empty or not reachable, no URL for b2rc posting')
            return ''
        soup = BeautifulSoup(html, "html.parser")
        hrefs = soup.find_all("a", href=True)
        cleaned_hrefs = []
        for ref in hrefs:
            cleaned_hrefs.append(ref['href'])
        base_ref = cleaned_hrefs[0]
        cleaned_hrefs = sorted(list(set(cleaned_hrefs)))
        cleaned_hrefs = [string for string in cleaned_hrefs if not string.endswith(
            (".pdf", ".png", ".jpg", ".txt", ".log")) and string.startswith("../"+self.logbook+"/")]
        number_of_report = []
        for href in cleaned_hrefs:
            number = href.replace("../"+self.logbook+"/", "")
            if number != "":
                number_of_report.append(int(number))
        number_of_report
        latest_report_url = base_ref+self.logbook+"/"+str(max(number_of_report))
        return latest_report_url

    def search_elog(self):
        '''GET html file of elog logbook page.'''
        # TODO use params/header for server query, could improve performance and simplify code
        # search_params = {}
        # search_params['mode']='XML'
        # search_params['reverse']='1'
        # search_params['last']=timeFrame
        # search_params['npp']='100'
        # search_params['type'] = '%5EDaily+Report%24'
        with requests.Session() as s:
            s.auth = requests.auth.HTTPBasicAuth(self.username, self.password)
            url_str = "{}://{}:{}/{}/".format(self.prefix, self.hostname, self.port, self.logbook)
            success = False
            retries = 0
            while True:
                try:
                    result = s.get(url_str)
                    result.raise_for_status()
                    success = True
                except Exception as e:
                    logging.error(traceback.format_exc())
                    time.sleep(10)
                    retries += 1
                if success:
                    break
                if retries >= 10:
                    logging.warning('B2rc posting timeout')
                    break
            return result.text

    def postMessage(self, msg, ch, alias=None, avatar=None, emoji=None):
        '''Build and post message to RC.'''
        if not ch.startswith('#') and not ch.startswith('@'):
            raise AssertionError(f'Invalid channel or user name {ch}')
        data = {'channel': ch, 'text': msg}
        if self.alias:
            data['alias'] = self.alias
        if emoji and emoji.startswith(':'):
            data['emoji'] = ':'.join(('', str(emoji).strip(':'), ''))
        if self.avatar and self.avatar.startswith('http'):
            data['avatar'] = self.avatar

        result = self.api_post('/api/v1/chat.postMessage', data)
        if not result:
            logging.warning('Could not reach b2rc login')
            return False

        return result.json()['success']

    def postReport(self, url):
        '''Define message text and channel.'''
        text = '{} {}\n[{}]({})'.format(
            self.starttime, self.type, url, url)
        result = self.postMessage(text, '#bgnet')
        if result is not True:
            raise RuntimeError('postReport: Sending shift report to b2rc failed')
        return result

    def rocketChat(self):
        '''Logs on to b2rc api and creates message wit latest elog entry.'''
        self.authenticate()
        for i in range(5):
            time.sleep(1)
            try:
                html = self.search_elog()
            except Exception as e:
                logging.error(traceback.format_exc())
                continue
            last_report_url = self.get_ref_from_html(html)
            # TODO get time information and reference to uploaded report. Cant be sure that last report is this one
        try:
            self.postReport(last_report_url)
        except Exception as e:
            logging.warning('RocketChat: Sending shift report to b2rc failed: {}'.format(e))
            return False
        return True
