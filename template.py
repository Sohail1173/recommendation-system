import logging
import os
from datetime import datetime
from pathlib import Path
logging.basicConfig(level=logging.INFO,
    format="[%(asctime)s-%(levelname)s]: %(message)s")

project_name="recommed"
list_of_files=[
f"{project_name}/__init__.py",
f"{project_name}/components/__init__.py",
f"{project_name}/components/data_ingestion.py",
f"{project_name}/components/data_validation.py",
f"{project_name}/components/data_transformation.py",
f"{project_name}/components/model_trainer.py",
f"{project_name}/config/configration.py",
f"{project_name}/config/__init__.py",
f"{project_name}/constant/__init__.py",
f"{project_name}/entity/config.py",
f"{project_name}/Exception/__init__.py",
f"{project_name}/Exception/exception.py",
f"{project_name}/logger/__init__.py",
f"{project_name}/logger/loggng.py",
f"{project_name}/training_pipeline/__init__.py",
f"{project_name}/training_pipeline/training_pipeline.py",
f"{project_name}/utls/__init__.py",
f"{project_name}/util.py",
"requirements.txt",
"config/config.yaml",
"app.py",
"setup.py",
"Dockerfile",
".dockerignore"
]

for files in list_of_files:
    files=Path(files)
    file_dir,file=os.path.split(files)
    if file_dir!="":
        os.makedirs(file_dir, exist_ok=True)
        logging.info("directories created")
    if (not os.path.exists(file)) or (os.path.getsize(file)==0):
        with open(files,"w") as f:
            pass
            logging.info(f"{files} created")
    else:
        logging.info(f"{files} already exists")