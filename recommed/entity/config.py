from collections import namedtuple

DataIngestionConfig=namedtuple("DataIngestionConfig",["dataset_download_url",
                                                      "raw_data_dir",
                                                      "ingested_dir"])
DataValidationConfig=namedtuple("DataValidationConfig",["clean_data_dir",
                                                        "book_csv_file",
                                                        "ratings_csv_file",
                                                        "serialized_objects_dir"])