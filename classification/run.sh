# sudo apt-get install axel

#axel -n 8 https://zihao-openmmlab.obs.cn-east-3.myhuaweicloud.com/20220716-mmclassification/dataset/fruit81/fruit81_full.zip -o classification.zip

#unzip classification.zip >> /dev/null

#find ./fruit81_full -iname '__MACOSX'
#find ./fruit81_full -iname '.DS_Store'
#find ./fruit81_full -iname '.ipynb_checkpoints'
#
#for i in `find ./fruit81_full -iname '__MACOSX'`; do rm -rf $i; done
#for i in `find ./fruit81_full -iname '.DS_Store'`; do rm -rf $i; done
#for i in `find ./fruit81_full -iname '.ipynb_checkpoints'`; do rm -rf $i; done
#
#python pre_poss.py


wget https://zihao-openmmlab.obs.cn-east-3.myhuaweicloud.com/20220716-mmclassification/dataset/SimHei.ttf -O /home/ilab/anaconda3/envs/py311_torch200_cuda118/lib/python3.11/site-packages/matplotlib/mpl-data/fonts/ttf/SimHei.ttf
rm -rf /home/featurize/.cache/matplotlib