curl -o data/genes.zip "https://www.pharmgkb.org/download.do?objId=genes.zip&dlCls=common"
unzip data/genes.zip -d data/
rm data/genes.zip

curl -o data/drugs.zip "https://www.pharmgkb.org/download.do?objId=drugs.zip&dlCls=common"
unzip data/drugs.zip -d data/
rm data/drugs.zip

curl -o data/drugLabels.zip "https://www.pharmgkb.org/download.do?objId=drugLabels.zip&dlCls=common"
unzip data/drugLabels.zip -d data/
rm data/drugLabels.zip

deb http://security.ubuntu.com/ubuntu lucid-security main
deb http://cz.archive.ubuntu.com/ubuntu lucid main
sudo apt-get update
sudo apt-get install graphviz

pip install -r requirements.txt