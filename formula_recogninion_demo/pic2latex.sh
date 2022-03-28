python3.7 -m venv omz
. omz/bin/activate
pip install -U pip
pip install openvino-dev==2021.4.2
git clone https://github.com/openvinotoolkit/open_model_zoo.git
cd open_model_zoo
pip install -r demos/requirements.txt
git checkout 2021.4.2
# Download the models
python tools/downloader/downloader.py --list demos/formula_recognition_demo/python/models.lst -o downloaded_models/
# Check demo

