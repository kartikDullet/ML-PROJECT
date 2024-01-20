import os
import sys
sys.path.append(os.path.abspath('D:\ML-PROJECT/src')) 
from src.exception import CustomException
from src.exception import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConifig:
    train_data_path: str=os.path.join('artificats', "train.csv")
    test_data_path: str=os.path.join('artificats', "test.csv")
    raw_data_path: str=os.path.join('artificats',"data.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConifig()


    def initiate_dat_ingestion(self):
        logging.info("Entered the data ingestion method")
        try:
            df=pd.read_csv('notebook\StudentsPerformance.csv')
            logging.info(" Read the data set")

            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Inmgestion of the data iss completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:  
            raise CustomException(e , sys) 



if __name__=="__main__":
    obj=DataIngestion() 
    obj.initiate_dat_ingestion()
