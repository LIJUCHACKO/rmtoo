#
# Config Class for the requirements for rmtoo
#

class Config:
    # development - team at flonatel
    # users - users from the Internet (sourceforge replies and wishes)
    # customers - people and companies who are flonatel's customers
    stakeholders = ["development", "management", "users", "customers"]
    inventors = ["flonatel", ]

    topic_specs = \
        {
          "ts_common": ["doc/topics", "ReqsDocument"],
         # "ts_input_only": ["doc/topics", "Input"],
        }

    output_specs = \
        [
          ["prios", 
           ["ts_common", "doc/latex2/reqsprios.tex"]],
        ]