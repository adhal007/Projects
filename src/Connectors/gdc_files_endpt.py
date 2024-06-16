
import json
import requests
import src.Connectors.gdc_endpt_base as gdc_endpt_base
import src.Connectors.gdc_filters as gdc_flt
import src.Connectors.gdc_fields as gdc_fld
import src.Connectors.gdc_field_validator as gdc_vld
import pandas as pd
"""
Copyright (c) 2024 OmixHub.  All rights are reserved.
GDC Files Endpt Class and high-level API functions

@author: Abhilash Dhal
@date:  2024_22_27
"""
class GDCFilesEndpt(gdc_endpt_base.GDCEndptBase):
    def __init__(self, homepage='https://api.gdc.cancer.gov', endpt='files'):
        super().__init__(homepage, endpt='files')
        # if self.check_valid_endpt():
        self.gdc_flt = gdc_flt.GDCFilters(self.endpt)
        self.gdc_fld = gdc_fld.GDCQueryFields(self.endpt)
        self.gdc_vld = gdc_vld.GDCValidator()

######### APPLICATION ORIENTED python functions ################################################
################################################################################################
    def fetch_rna_seq_star_counts_data(self, new_fields=None, ps_list=None, race_list=None, gender_list=None):
        if ps_list is None:
            raise ValueError("List of primary sites must be provided")
        
        # for x in ps_list:
        #     if x not in self.gdc_vld.list_of_primary_sites:
        #         raise ValueError(f"Incorrect primary site queried by user: Please check the list of allowed primary sites from {','.join(self.gdc_vld.list_of_primary_sites)}")
            
        if new_fields is None:
            fields = self.gdc_fld.dft_rna_seq_star_count_data_fields
        else:
            ## Adding logic for checking fields
            for x in new_fields:
                if x not in self.gdc_vld.file_endpt_fields:
                    raise ValueError("Field provided is not in the list of fields by GDC")
            self.gdc_fld.update_fields('dft_rna_seq_star_count_data_fields', new_fields)
            fields = self.gdc_fld.dft_rna_seq_star_count_data_fields        
        fields = ",".join(fields)

        filters = self.gdc_flt.rna_seq_star_count_filter(ps_list=ps_list, race_list=race_list, gender_list=gender_list)
        # Here a GET is used, so the filter parameters should be passed as a JSON string.
        print(filters)
        params = {
            "filters": json.dumps(filters),
            "fields": fields,
            "format": "json",
            "size": "50000"
            }
        print(params)
        response = requests.get(self.files_endpt, params = params)
        json_data = json.loads(response.text)
        return json_data, filters
    # def list_projects_by_ps_race_gender_exp(self, 
    #                                         new_fields=None,
    #                                         ps_list=None, 
    #                                         race_list=None, 
    #                                         exp_list=None, 
    #                                         size=100, 
    #                                         format='json'):
    #     if new_fields is None:
    #         fields = self.gdc_fld.dft_primary_site_race_gender_exp_fields
    #     else:
    #         self.gdc_fld.update_fields('dft_primary_site_race_gender_exp_fields', new_fields)
    #         fields = self.gdc_fld.dft_primary_site_race_gender_exp_fields
    #     print(fields)
    #     fields = ",".join(fields)

    #     filters = self.gdc_flt.ps_race_gender_exp_filter(ps_list=ps_list, race_list=race_list, exp_list=exp_list)
    #     params = self.make_params_dict(filters, fields, size=size, format=format)
    #     json_data = self.get_json_data(self.files_endpt, params)
    #     return json_data

    # def search_files_by_criteria(self, new_fields=None, primary_sites=None, experimental_strategies=None, data_formats='json', size=100):
    #     """
    #     Search files based on primary site, experimental strategy, and data format.
    #     """
    #     files_endpt = "https://api.gdc.cancer.gov/files"
    #     filters = self.gdc_flt.primary_site_exp_filter(primary_sites, experimental_strategies, data_formats='tsv')
    #     if new_fields is None:
    #         fields = self.gdc_fld.dft_primary_site_exp_fields
    #     else:
    #         self.gdc_fld.update_fields('dft_primary_site_exp_fields', new_fields)
    #         fields = self.gdc_fld.dft_primary_site_exp_fields       

    #     fields = ",".join(fields)
    #     params = self.make_params_dict(filters, fields, size=size, format=data_formats)
    #     json_data = self.get_json_data(files_endpt, params)
    #     # return self.search('/files', filters=filters, fields=fields, format=data_formats, size=100)
    #     return json_data