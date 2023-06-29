# Clone the repo
conda create -n ann_lib python=3.8
conda activate ann_lib

Run pip install -r requirements.txt

uvicorn app.main:app

navigate to localhost:port/docs get port from logs.



or 
Run docker build -t ann-search_lib -f Dockerfile .