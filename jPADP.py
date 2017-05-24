"""
Features:

* Datetime indexes all operations;
* Optionally saves all raw data files;
* Logs raw data files, dependencies to remote APIs, API calls, data ETL operations,
  persistence of preliminary data files, and workflow executions.

Output: pickle file in '[current_path]/trial/trial-[k].padp'

Operations:

* load_dataset(file_path, label=None)
* register_url(base_url, label=None)
* query_url(query_path, query_phrase, label=None)
* modify_data(columns, row_ids, label=None)
* interaction_by_scientist(column, value, label=None)
* save(partial_result, label=None)
* run_workflow(workflow_name, run_environment, configurations, label=None)
"""

import datetime
import os
import pickle


class jupyterPADP():
    
    save_raw = False

    DATASETS = {}
    URLS = {}
    QUERIES = {}
    ETLS = {}
    INTERACTIONS = {}
    RESULTS = {}
    RUNS = {}
    
    t_id = 0
    path = None
    
    def __init__(self, save_raw=False):
        self.save_raw = save_raw
        self.path = os.path.join(os.getcwd(), 'trials')
        self.t_id = 0
        
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        else:
            onlyfiles = next(os.walk(self.path))[2]
            self.t_id = len(onlyfiles)
    
    def get_now(self):
        return datetime.datetime.now()
    
    def load_dataset(self, file_path, label=None):
        dataset_obj = {}
        dataset_obj['path'] = file_path
        
        if self.save_raw:
            try:
                with open(file_path, 'r') as f:
                    dataset_obj['content'] = f.read()
            except:
                pass
        
        if label:
            dataset_obj['label'] = label  
        self.DATASETS[self.get_now()] = dataset_obj
    
    def register_url(self, base_url, label=None):
        urls_obj = {}
        urls_obj['base_url'] = base_url
        if label:
            urls_obj['label'] = label  
        self.URLS[self.get_now()] = urls_obj
    
    def query_url(self, query_path, query_phrase, label=None):
        query_obj = {}
        query_obj['query_path'] = query_path
        query_obj['query_phrase'] = query_phrase
        if label:
            query_obj['label'] = label  
        self.QUERIES[self.get_now()] = query_obj
    
    def modify_data(self, columns, row_ids, label=None):
        etl_obj = {}
        etl_obj['columns'] = columns
        etl_obj['row_ids'] = row_ids
        if label:
            etl_obj['label'] = label  
        self.ETLS[self.get_now()] = etl_obj
    
    def interaction_by_scientist(self, column, value, label=None):
        interaction_obj = {}
        interaction_obj['column'] = column
        interaction_obj['value'] = value
        if label:
            interaction_obj['label'] = label  
        self.INTERACTIONS[self.get_now()] = interaction_obj
        
    def save(self, partial_result, label=None):
        save_obj = {}
        save_obj['content'] = partial_result
        if label:
            save_obj['label'] = label  
        self.RESULTS[self.get_now()] = save_obj

    def run_workflow(self, workflow_name, run_environment, configurations, label=None):
        run_obj = {}
        run_obj['workflow_name'] = workflow_name
        run_obj['run_environment'] = run_environment
        run_obj['configurations'] = configurations
        if label:
            run_obj['label'] = label  
        self.RUNS[self.get_now()] = run_obj
    
    def commit(self):
        dump_obj = {}
        dump_obj['DATASETS'] = self.DATASETS
        dump_obj['URLS'] = self.URLS
        dump_obj['QUERIES'] = self.QUERIES
        dump_obj['ETLS'] = self.ETLS
        dump_obj['INTERACTIONS'] = self.INTERACTIONS
        dump_obj['RESULTS'] = self.RESULTS
        dump_obj['RUNS'] = self.RUNS
        
        with open(os.path.join(self.path, 'trial-%s.padp'%self.t_id), 'wb') as f:
            pickle.dump(dump_obj, f)

