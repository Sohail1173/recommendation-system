import os,sys,ast
import pandas  as pd
import  pickle
from recommed.logger.loggng import logging
from recommed.config.configration import AppConfiguration
from recommed.Exception.exception import  AppException

class DataValidation:

    def __init__(self,app_config=AppConfiguration()):
        try:
            self.data_validation_config=app_config.get_data_validation_config()
        except AppException as e:
            raise AppException(e,sys) from e
        

    def preprocess_data(self):
        try:
            ratings=pd.read_csv(self.data_validation_config.ratings_csv_file,
            sep=";",on_bad_lines="skip",encoding='latin-1')
            books=pd.read_csv(self.data_validation_config.book_csv_file,
            sep=";",on_bad_lines="skip",encoding='latin-1')
            logging.info(f"shape of ratings data file:{ratings.shape}")
            logging.info(f"shape of books data file:{books.shape}")

            books=books[['ISBN', 'Book-Title', 'Book-Author', 'Year-Of-Publication', 'Publisher',
            'Image-URL-L']]
            books.rename(columns={
            "Book-Title":"title",
            "Book-Author":"author",
            "Year-Of-Publication":"year",
            "Publisher":"publisher",
            "Image-URL-L":"img_url"
             },inplace=True)
            
            ratings.rename(columns={
            "User-ID":"user_id",
            "Book-Rating":"rating"
    
             },inplace=True)
            X=ratings["user_id"].value_counts()>200
            # x=ratings["user_id"].value_counts()>200
            y=X[X].index
            ratings=ratings[ratings["user_id"].isin(y)]
            ratings_with_books=ratings.merge(books,on="ISBN")

            
            number_of_rating=ratings_with_books.groupby("title")["rating"].count().reset_index()
            number_of_rating.rename(columns={"rating":"num_of_rating"},inplace=True)
            final_rating=ratings_with_books.merge(number_of_rating,on="title")
            final_rating=final_rating[final_rating["num_of_rating"]>=50]
            final_rating.drop_duplicates(["user_id", "title"],inplace=True)

            logging.info(f"shape of the final clean dataset:{final_rating.shape}")

            os.makedirs(self.data_validation_config.clean_data_dir, exist_ok=True)
            final_rating.to_csv(os.path.join(self.data_validation_config.clean_data_dir,"clean_data.csv"),index=False)
            logging.info(f"clean data saved in {self.data_validation_config.clean_data_dir}")

            os.makedirs(self.data_validation_config.serialized_objects_dir,exist_ok=True)
            pickle.dump(final_rating,open(os.path.join(self.data_validation_config.serialized_objects_dir,"final_rating.pkl"),"wb"))
            logging.info(f"final_rating object saved in {self.data_validation_config.serialized_objects_dir}")

        except AppException as e:
            raise AppException(e,sys) from e
        

    def initiate_data_validation(self):
        try:
            logging.info(f"{'='*20}Data Validation log started.{'='*20}")
            self.preprocess_data()
            logging.info(f"{'='*20}Data Validation log completed.{'='*20} \n\n")
        except AppException as e:
            raise AppException(e,sys) from e