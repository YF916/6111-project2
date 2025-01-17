#!/bin/bash
data_dir="pretrained_spanbert"
model="tacred"
echo Downloading pre-trained SpanBERT 
curl -o $data_dir\spanbert_$model.tar.gz http://dl.fbaipublicfiles.com/fairseq/models/spanbert_$model.tar.gz
mkdir -p $data_dir
tar xvzf $data_dir/spanbert_$model.tar.gz -C $data_dir
rm $data_dir/spanbert_$model.tar.gz
