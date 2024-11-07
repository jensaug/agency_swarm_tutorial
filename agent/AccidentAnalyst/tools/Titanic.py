import os
from pydantic import Field
from agency_swarm.tools import BaseTool
from vanna.openai import OpenAI_Chat
from vanna.chromadb import ChromaDB_VectorStore
from typing import ClassVar

class MyVanna(ChromaDB_VectorStore, OpenAI_Chat):
    def __init__(self, config=None):
        ChromaDB_VectorStore.__init__(self, config=config)
        OpenAI_Chat.__init__(self, config=config)


class Titanic(BaseTool):

    """
    This is a tool for gathering data and statistics regarding the 1912 accident when the Titanic ship sunk.
    The source for this information is the Kagge Titanic Dataset at https://www.kaggle.com/c/titanic/data
    The output of this tool is a dictionary where the key is the source of the information and the value is the answer to the question.
    """
    question: str = Field(
        ..., content= "The question for the Titanic database"
    )    

    vn : ClassVar[MyVanna] = MyVanna(config={'api_key': os.environ['OPENAI_API_KEY'], 'model': 'gpt-4o-mini', 'allow_llm_to_see_data': True})

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.vn.connect_to_sqlite('agent/AccidentAnalyst/tools/titanic.db')
        
        df_ddl = self.vn.run_sql("SELECT type, sql FROM sqlite_master WHERE sql is not null")
        for ddl in df_ddl['sql'].to_list():
            self.vn.train(ddl=ddl)

        training_data = self.vn.get_training_data()
        print(training_data)

    def run(self):
        return self.vn.ask(question=self.question, allow_llm_to_see_data=True)