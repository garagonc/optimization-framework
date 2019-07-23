"""
Created on Mai 28 14:22 2019

@author: nishit
"""
from optimization.baseDataReceiver import BaseDataReceiver


class BaseValueDataReceiver(BaseDataReceiver):

    def __init__(self, internal, topic_params, config, generic_name, id, buffer, dT):
        super().__init__(internal, topic_params, config, generic_name, id, buffer, dT, True)

    def preprocess_data(self, base, name, value, unit):
        if "charger" in base:
            s = name.split("/")
            data = {}
            if len(s) == 2:
                data["Hosted_EV"] = s[0]
                data[s[1]] = value
            else:
                data[s[-1]] = value
            base = base.split("/")[-1]
            return {base: data}
        return {}