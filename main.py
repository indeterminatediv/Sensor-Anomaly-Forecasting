from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.exception import SensorException
import os,sys
from sensor.logger import logging
from sensor.pipeline.training_pipeline import TrainPipeline
from sensor.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig


if __name__ == '__main__':         

    try:
        training_pipeline = TrainPipeline()
        training_pipeline.run_pipeline()
    except Exception as e: 
        raise SensorException(e, sys)   