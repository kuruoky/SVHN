cd ~
mkdir data && cd data
wget http://ufldl.stanford.edu/housenumbers/train.tar.gz
wget http://ufldl.stanford.edu/housenumbers/test.tar.gz
wget http://ufldl.stanford.edu/housenumbers/extra.tar.gz
tar -xvzf test.tar.gz
tar -xvzf train.tar.gz
tar -xvzf extra.tar.gz
rm *.tar.gz