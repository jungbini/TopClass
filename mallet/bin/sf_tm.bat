# 토픽 개수는 100개

# 1. Before/After Sourceforge Project

mallet import-dir --input E:\Tools\TopicDocs\sf_simple\7_bfNLP_version --keep-sequence --remove-stopwords --extra-stopwords ../stoplists/extra_en.txt --output InputDocs/bf.mallet
mallet train-topics --input InputDocs/bf.mallet --num-topics 100 --optimize-interval 20 --output-topic-keys LDA/bf_words100.csv --output-doc-topics LDA/bf_dist100.csv --inferencer-filename Inferencer/bf_infer100 --output-model Model/bf_model100 --num-threads 16

mallet import-dir --input E:\Tools\TopicDocs\sf_simple\8_afNLP_version --keep-sequence --remove-stopwords --extra-stopwords ../stoplists/extra_en.txt --output InputDocs/af.mallet
mallet train-topics --input InputDocs/af.mallet --num-topics 100 --optimize-interval 20 --output-topic-keys LDA/af_words100.csv --output-doc-topics LDA/af_dist100.csv --inferencer-filename Inferencer/af_infer100 --output-model Model/af_model100 --num-threads 16

# 2. Test/Training Sourceforge Project

mallet import-dir --input E:\Tools\TopicDocs\sf_simple\9_bfDM(0.2)_version\training1 --keep-sequence --remove-stopwords --extra-stopwords ../stoplists/extra_en.txt --output InputDocs/0.2/train1_bf.mallet
mallet import-dir --input E:\Tools\TopicDocs\sf_simple\9_bfDM(0.2)_version\training2 --keep-sequence --remove-stopwords --extra-stopwords ../stoplists/extra_en.txt --output InputDocs/0.2/train2_bf.mallet
mallet import-dir --input E:\Tools\TopicDocs\sf_simple\9_bfDM(0.2)_version\training3 --keep-sequence --remove-stopwords --extra-stopwords ../stoplists/extra_en.txt --output InputDocs/0.2/train3_bf.mallet
mallet import-dir --input E:\Tools\TopicDocs\sf_simple\9_bfDM(0.2)_version\training4 --keep-sequence --remove-stopwords --extra-stopwords ../stoplists/extra_en.txt --output InputDocs/0.2/train4_bf.mallet
mallet import-dir --input E:\Tools\TopicDocs\sf_simple\9_bfDM(0.2)_version\training5 --keep-sequence --remove-stopwords --extra-stopwords ../stoplists/extra_en.txt --output InputDocs/0.2/train5_bf.mallet
mallet import-dir --input E:\Tools\TopicDocs\sf_simple\9_bfDM(0.2)_version\training6 --keep-sequence --remove-stopwords --extra-stopwords ../stoplists/extra_en.txt --output InputDocs/0.2/train6_bf.mallet
mallet import-dir --input E:\Tools\TopicDocs\sf_simple\9_bfDM(0.2)_version\training7 --keep-sequence --remove-stopwords --extra-stopwords ../stoplists/extra_en.txt --output InputDocs/0.2/train7_bf.mallet
mallet import-dir --input E:\Tools\TopicDocs\sf_simple\9_bfDM(0.2)_version\training8 --keep-sequence --remove-stopwords --extra-stopwords ../stoplists/extra_en.txt --output InputDocs/0.2/train8_bf.mallet
mallet import-dir --input E:\Tools\TopicDocs\sf_simple\9_bfDM(0.2)_version\training9 --keep-sequence --remove-stopwords --extra-stopwords ../stoplists/extra_en.txt --output InputDocs/0.2/train9_bf.mallet
mallet import-dir --input E:\Tools\TopicDocs\sf_simple\9_bfDM(0.2)_version\training10 --keep-sequence --remove-stopwords --extra-stopwords ../stoplists/extra_en.txt --output InputDocs/0.2/train10_bf.mallet
mallet train-topics --input InputDocs/0.2/train1_bf.mallet --num-topics 100 --optimize-interval 20 --output-topic-keys LDA/0.2/train1_bf_words100.csv --output-doc-topics LDA/0.2/train1_bf_dist100.csv --inferencer-filename Inferencer/0.2/train1_bf_infer100 --output-model Model/0.2/train1_bf_model100 --num-threads 16
mallet train-topics --input InputDocs/0.2/train2_bf.mallet --num-topics 100 --optimize-interval 20 --output-topic-keys LDA/0.2/train2_bf_words100.csv --output-doc-topics LDA/0.2/train2_bf_dist100.csv --inferencer-filename Inferencer/0.2/train2_bf_infer100 --output-model Model/0.2/train2_bf_model100 --num-threads 16
mallet train-topics --input InputDocs/0.2/train3_bf.mallet --num-topics 100 --optimize-interval 20 --output-topic-keys LDA/0.2/train3_bf_words100.csv --output-doc-topics LDA/0.2/train3_bf_dist100.csv --inferencer-filename Inferencer/0.2/train3_bf_infer100 --output-model Model/0.2/train3_bf_model100 --num-threads 16
mallet train-topics --input InputDocs/0.2/train4_bf.mallet --num-topics 100 --optimize-interval 20 --output-topic-keys LDA/0.2/train4_bf_words100.csv --output-doc-topics LDA/0.2/train4_bf_dist100.csv --inferencer-filename Inferencer/0.2/train4_bf_infer100 --output-model Model/0.2/train4_bf_model100 --num-threads 16
mallet train-topics --input InputDocs/0.2/train5_bf.mallet --num-topics 100 --optimize-interval 20 --output-topic-keys LDA/0.2/train5_bf_words100.csv --output-doc-topics LDA/0.2/train5_bf_dist100.csv --inferencer-filename Inferencer/0.2/train5_bf_infer100 --output-model Model/0.2/train5_bf_model100 --num-threads 16
mallet train-topics --input InputDocs/0.2/train6_bf.mallet --num-topics 100 --optimize-interval 20 --output-topic-keys LDA/0.2/train6_bf_words100.csv --output-doc-topics LDA/0.2/train6_bf_dist100.csv --inferencer-filename Inferencer/0.2/train6_bf_infer100 --output-model Model/0.2/train6_bf_model100 --num-threads 16
mallet train-topics --input InputDocs/0.2/train7_bf.mallet --num-topics 100 --optimize-interval 20 --output-topic-keys LDA/0.2/train7_bf_words100.csv --output-doc-topics LDA/0.2/train7_bf_dist100.csv --inferencer-filename Inferencer/0.2/train7_bf_infer100 --output-model Model/0.2/train7_bf_model100 --num-threads 16
mallet train-topics --input InputDocs/0.2/train8_bf.mallet --num-topics 100 --optimize-interval 20 --output-topic-keys LDA/0.2/train8_bf_words100.csv --output-doc-topics LDA/0.2/train8_bf_dist100.csv --inferencer-filename Inferencer/0.2/train8_bf_infer100 --output-model Model/0.2/train8_bf_model100 --num-threads 16
mallet train-topics --input InputDocs/0.2/train9_bf.mallet --num-topics 100 --optimize-interval 20 --output-topic-keys LDA/0.2/train9_bf_words100.csv --output-doc-topics LDA/0.2/train9_bf_dist100.csv --inferencer-filename Inferencer/0.2/train9_bf_infer100 --output-model Model/0.2/train9_bf_model100 --num-threads 16
mallet train-topics --input InputDocs/0.2/train10_bf.mallet --num-topics 100 --optimize-interval 20 --output-topic-keys LDA/0.2/train10_bf_words100.csv --output-doc-topics LDA/0.2/train10_bf_dist100.csv --inferencer-filename Inferencer/0.2/train10_bf_infer100 --output-model Model/0.2/train10_bf_model100 --num-threads 16

mallet import-dir --input E:\Tools\TopicDocs\sf_simple\9_bfDM(0.2)_version\test1 --keep-sequence --remove-stopwords --extra-stopwords ../stoplists/extra_en.txt --use-pipe-from InputDocs/0.2/train1_bf.mallet --output InputDocs/0.2/test1_bf.mallet
mallet import-dir --input E:\Tools\TopicDocs\sf_simple\9_bfDM(0.2)_version\test2 --keep-sequence --remove-stopwords --extra-stopwords ../stoplists/extra_en.txt --use-pipe-from InputDocs/0.2/train2_bf.mallet --output InputDocs/0.2/test2_bf.mallet
mallet import-dir --input E:\Tools\TopicDocs\sf_simple\9_bfDM(0.2)_version\test3 --keep-sequence --remove-stopwords --extra-stopwords ../stoplists/extra_en.txt --use-pipe-from InputDocs/0.2/train3_bf.mallet --output InputDocs/0.2/test3_bf.mallet
mallet import-dir --input E:\Tools\TopicDocs\sf_simple\9_bfDM(0.2)_version\test4 --keep-sequence --remove-stopwords --extra-stopwords ../stoplists/extra_en.txt --use-pipe-from InputDocs/0.2/train4_bf.mallet --output InputDocs/0.2/test4_bf.mallet
mallet import-dir --input E:\Tools\TopicDocs\sf_simple\9_bfDM(0.2)_version\test5 --keep-sequence --remove-stopwords --extra-stopwords ../stoplists/extra_en.txt --use-pipe-from InputDocs/0.2/train5_bf.mallet --output InputDocs/0.2/test5_bf.mallet
mallet import-dir --input E:\Tools\TopicDocs\sf_simple\9_bfDM(0.2)_version\test6 --keep-sequence --remove-stopwords --extra-stopwords ../stoplists/extra_en.txt --use-pipe-from InputDocs/0.2/train6_bf.mallet --output InputDocs/0.2/test6_bf.mallet
mallet import-dir --input E:\Tools\TopicDocs\sf_simple\9_bfDM(0.2)_version\test7 --keep-sequence --remove-stopwords --extra-stopwords ../stoplists/extra_en.txt --use-pipe-from InputDocs/0.2/train7_bf.mallet --output InputDocs/0.2/test7_bf.mallet
mallet import-dir --input E:\Tools\TopicDocs\sf_simple\9_bfDM(0.2)_version\test8 --keep-sequence --remove-stopwords --extra-stopwords ../stoplists/extra_en.txt --use-pipe-from InputDocs/0.2/train8_bf.mallet --output InputDocs/0.2/test8_bf.mallet
mallet import-dir --input E:\Tools\TopicDocs\sf_simple\9_bfDM(0.2)_version\test9 --keep-sequence --remove-stopwords --extra-stopwords ../stoplists/extra_en.txt --use-pipe-from InputDocs/0.2/train9_bf.mallet --output InputDocs/0.2/test9_bf.mallet
mallet import-dir --input E:\Tools\TopicDocs\sf_simple\9_bfDM(0.2)_version\test10 --keep-sequence --remove-stopwords --extra-stopwords ../stoplists/extra_en.txt --use-pipe-from InputDocs/0.2/train10_bf.mallet --output InputDocs/0.2/test10_bf.mallet
mallet infer-topics --input InputDocs/0.2/test1_bf.mallet --inferencer Inferencer/0.2/train1_bf_infer100 --output-doc-topics LDA/0.2/test1_bf_infer100.csv
mallet infer-topics --input InputDocs/0.2/test2_bf.mallet --inferencer Inferencer/0.2/train2_bf_infer100 --output-doc-topics LDA/0.2/test2_bf_infer100.csv
mallet infer-topics --input InputDocs/0.2/test3_bf.mallet --inferencer Inferencer/0.2/train3_bf_infer100 --output-doc-topics LDA/0.2/test3_bf_infer100.csv
mallet infer-topics --input InputDocs/0.2/test4_bf.mallet --inferencer Inferencer/0.2/train4_bf_infer100 --output-doc-topics LDA/0.2/test4_bf_infer100.csv
mallet infer-topics --input InputDocs/0.2/test5_bf.mallet --inferencer Inferencer/0.2/train5_bf_infer100 --output-doc-topics LDA/0.2/test5_bf_infer100.csv
mallet infer-topics --input InputDocs/0.2/test6_bf.mallet --inferencer Inferencer/0.2/train6_bf_infer100 --output-doc-topics LDA/0.2/test6_bf_infer100.csv
mallet infer-topics --input InputDocs/0.2/test7_bf.mallet --inferencer Inferencer/0.2/train7_bf_infer100 --output-doc-topics LDA/0.2/test7_bf_infer100.csv
mallet infer-topics --input InputDocs/0.2/test8_bf.mallet --inferencer Inferencer/0.2/train8_bf_infer100 --output-doc-topics LDA/0.2/test8_bf_infer100.csv
mallet infer-topics --input InputDocs/0.2/test9_bf.mallet --inferencer Inferencer/0.2/train9_bf_infer100 --output-doc-topics LDA/0.2/test9_bf_infer100.csv
mallet infer-topics --input InputDocs/0.2/test10_bf.mallet --inferencer Inferencer/0.2/train10_bf_infer100 --output-doc-topics LDA/0.2/test10_bf_infer100.csv


# 3. Other Project

# 3-1. jbpm Before/After
mallet import-dir --input E:\Tools\TopicDocs\sf_simple_test\7_bfNLP_version\jbpm --keep-sequence --remove-stopwords --extra-stopwords ../stoplists/extra_en.txt --use-pipe-from InputDocs/bf.mallet --output InputDocs/otherproject/bf_jbpm.mallet
mallet infer-topics --input InputDocs/otherproject/bf_jbpm.mallet --inferencer Inferencer/bf_infer100 --output-doc-topics LDA/otherproject/bf_jbpm_dist100.csv
mallet import-dir --input E:\Tools\TopicDocs\sf_simple_test\8_afNLP_version\jbpm --keep-sequence --remove-stopwords --extra-stopwords ../stoplists/extra_en.txt --use-pipe-from InputDocs/af.mallet --output InputDocs/otherproject/af_jbpm.mallet
mallet infer-topics --input InputDocs/otherproject/af_jbpm.mallet --inferencer Inferencer/af_infer100 --output-doc-topics LDA/otherproject/af_jbpm_dist100.csv

# 3-2. GWT Before/After
mallet import-dir --input E:\Tools\TopicDocs\sf_simple_test\7_bfNLP_version\gwt --keep-sequence --remove-stopwords --extra-stopwords ../stoplists/extra_en.txt --use-pipe-from InputDocs/bf.mallet --output InputDocs/otherproject/bf_gwt.mallet
mallet infer-topics --input InputDocs/otherproject/bf_gwt.mallet --inferencer Inferencer/bf_infer100 --output-doc-topics LDA/otherproject/bf_gwt_infer100.csv
mallet import-dir --input E:\Tools\TopicDocs\sf_simple_test\8_afNLP_version\gwt --keep-sequence --remove-stopwords --extra-stopwords ../stoplists/extra_en.txt --use-pipe-from InputDocs/af.mallet --output InputDocs/otherproject/af_gwt.mallet
mallet infer-topics --input InputDocs/otherproject/af_gwt.mallet --inferencer Inferencer/af_infer100 --output-doc-topics LDA/otherproject/af_gwt_infer100.csv

# 3-3. Openoffice Before/After
mallet import-dir --input E:\Tools\TopicDocs\sf_simple_test\7_bfNLP_version\openoffice --keep-sequence --remove-stopwords --extra-stopwords ../stoplists/extra_en.txt --use-pipe-from InputDocs/bf.mallet --output InputDocs/otherproject/bf_openoffice.mallet
mallet infer-topics --input InputDocs/otherproject/bf_openoffice.mallet --inferencer Inferencer/bf_infer100 --output-doc-topics LDA/otherproject/bf_openoffice_infer100.csv
mallet import-dir --input E:\Tools\TopicDocs\sf_simple_test\8_afNLP_version\openoffice --keep-sequence --remove-stopwords --extra-stopwords ../stoplists/extra_en.txt --use-pipe-from InputDocs/af.mallet --output InputDocs/otherproject/af_openoffice.mallet
mallet infer-topics --input InputDocs/otherproject/af_openoffice.mallet --inferencer Inferencer/af_infer100 --output-doc-topics LDA/otherproject/af_openoffice_infer100.csv

# 3-4. Libreoffice Before/After
mallet import-dir --input E:\Tools\TopicDocs\sf_simple_test\7_bfNLP_version\libreoffice --keep-sequence --remove-stopwords --extra-stopwords ../stoplists/extra_en.txt --use-pipe-from InputDocs/bf.mallet --output InputDocs/otherproject/bf_libreoffice.mallet
mallet infer-topics --input InputDocs/otherproject/bf_libreoffice.mallet --inferencer Inferencer/bf_infer100 --output-doc-topics LDA/otherproject/bf_libreoffice_infer100.csv
mallet import-dir --input E:\Tools\TopicDocs\sf_simple_test\8_afNLP_version\libreoffice --keep-sequence --remove-stopwords --extra-stopwords ../stoplists/extra_en.txt --use-pipe-from InputDocs/af.mallet --output InputDocs/otherproject/af_libreoffice.mallet
mallet infer-topics --input InputDocs/otherproject/af_libreoffice.mallet --inferencer Inferencer/af_infer100 --output-doc-topics LDA/otherproject/af_libreoffice_infer100.csv

# 3-5. iText Before/After
mallet import-dir --input E:\Tools\TopicDocs\sf_simple_test\7_bfNLP_version\itext --keep-sequence --remove-stopwords --extra-stopwords ../stoplists/extra_en.txt --use-pipe-from InputDocs/bf.mallet --output InputDocs/otherproject/bf_itext.mallet
mallet infer-topics --input InputDocs/otherproject/bf_itext.mallet --inferencer Inferencer/bf_infer100 --output-doc-topics LDA/otherproject/bf_itext_infer100.csv
mallet import-dir --input E:\Tools\TopicDocs\sf_simple_test\8_afNLP_version\itext --keep-sequence --remove-stopwords --extra-stopwords ../stoplists/extra_en.txt --use-pipe-from InputDocs/af.mallet --output InputDocs/otherproject/af_itext.mallet
mallet infer-topics --input InputDocs/otherproject/af_itext.mallet --inferencer Inferencer/af_infer100 --output-doc-topics LDA/otherproject/af_itext_infer100.csv

# 3-6. jasperserver Before/After
mallet import-dir --input E:\Tools\TopicDocs\sf_simple_test\7_bfNLP_version\jasperserver --keep-sequence --remove-stopwords --extra-stopwords ../stoplists/extra_en.txt --use-pipe-from InputDocs/bf.mallet --output InputDocs/otherproject/bf_jasperserver.mallet
mallet infer-topics --input InputDocs/otherproject/bf_jasperserver.mallet --inferencer Inferencer/bf_infer100 --output-doc-topics LDA/otherproject/bf_jasperserver_infer100.csv
mallet import-dir --input E:\Tools\TopicDocs\sf_simple_test\8_afNLP_version\jasperserver --keep-sequence --remove-stopwords --extra-stopwords ../stoplists/extra_en.txt --use-pipe-from InputDocs/af.mallet --output InputDocs/otherproject/af_jasperserver.mallet
mallet infer-topics --input InputDocs/otherproject/af_jasperserver.mallet --inferencer Inferencer/af_infer100 --output-doc-topics LDA/otherproject/af_jasperserver_infer100.csv

# 3-7. jbossserver Before/After
mallet import-dir --input E:\Tools\TopicDocs\sf_simple_test\7_bfNLP_version\jbossserver --keep-sequence --remove-stopwords --extra-stopwords ../stoplists/extra_en.txt --use-pipe-from InputDocs/bf.mallet --output InputDocs/otherproject/bf_jbossserver.mallet
mallet infer-topics --input InputDocs/otherproject/bf_jbossserver.mallet --inferencer Inferencer/bf_infer100 --output-doc-topics LDA/otherproject/bf_jbossserver_infer100.csv
mallet import-dir --input E:\Tools\TopicDocs\sf_simple_test\8_afNLP_version\jbossserver --keep-sequence --remove-stopwords --extra-stopwords ../stoplists/extra_en.txt --use-pipe-from InputDocs/af.mallet --output InputDocs/otherproject/af_jbossserver.mallet
mallet infer-topics --input InputDocs/otherproject/af_jbossserver.mallet --inferencer Inferencer/af_infer100 --output-doc-topics LDA/otherproject/af_jbossserver_infer100.csv


# 4. Other Project Before
# infer는 샘플이 작을 경우 토픽이 안나오는 경우가 많아서 아예 새롭게 토픽 모델링을 해서 word 유사도를 비교
mallet import-dir --input E:\Tools\TopicDocs\sf_simple_test\7_bfNLP_version\jbpm --keep-sequence --remove-stopwords --extra-stopwords ../stoplists/extra_en.txt --output InputDocs/otherproject2/bf_jbpm.mallet
mallet import-dir --input E:\Tools\TopicDocs\sf_simple_test\7_bfNLP_version\gwt --keep-sequence --remove-stopwords --extra-stopwords ../stoplists/extra_en.txt --output InputDocs/otherproject2/bf_gwt.mallet
mallet import-dir --input E:\Tools\TopicDocs\sf_simple_test\7_bfNLP_version\openoffice --keep-sequence --remove-stopwords --extra-stopwords ../stoplists/extra_en.txt --output InputDocs/otherproject2/bf_openoffice.mallet
mallet import-dir --input E:\Tools\TopicDocs\sf_simple_test\7_bfNLP_version\libreoffice --keep-sequence --remove-stopwords --extra-stopwords ../stoplists/extra_en.txt --output InputDocs/otherproject2/bf_libreoffice.mallet
mallet import-dir --input E:\Tools\TopicDocs\sf_simple_test\7_bfNLP_version\itext --keep-sequence --remove-stopwords --extra-stopwords ../stoplists/extra_en.txt --output InputDocs/otherproject2/bf_itext.mallet
mallet import-dir --input E:\Tools\TopicDocs\sf_simple_test\7_bfNLP_version\jasperserver --keep-sequence --remove-stopwords --extra-stopwords ../stoplists/extra_en.txt --output InputDocs/otherproject2/bf_jasperserver.mallet
mallet import-dir --input E:\Tools\TopicDocs\sf_simple_test\7_bfNLP_version\jbossserver --keep-sequence --remove-stopwords --extra-stopwords ../stoplists/extra_en.txt --output InputDocs/otherproject2/bf_jbossserver.mallet
mallet train-topics --input InputDocs/otherproject2/bf_jbpm.mallet --num-topics 100 --optimize-interval 20 --output-topic-keys LDA/otherproject2/bf_jbpm_words100.csv --output-doc-topics LDA/otherproject2/bf_jbpm_dist100.csv --inferencer-filename Inferencer/otherproject2/bf_jbpm_infer100 --output-model Model/otherproject2/bf_jbpm_model100 --num-threads 16
mallet train-topics --input InputDocs/otherproject2/bf_gwt.mallet --num-topics 100 --optimize-interval 20 --output-topic-keys LDA/otherproject2/bf_gwt_words100.csv --output-doc-topics LDA/otherproject2/bf_gwt_dist100.csv --inferencer-filename Inferencer/otherproject2/bf_gwt_infer100 --output-model Model/otherproject2/bf_gwt_model100 --num-threads 16
mallet train-topics --input InputDocs/otherproject2/bf_openoffice.mallet --num-topics 100 --optimize-interval 20 --output-topic-keys LDA/otherproject2/bf_openoffice_words100.csv --output-doc-topics LDA/otherproject2/bf_openoffice_dist100.csv --inferencer-filename Inferencer/otherproject2/bf_openoffice_infer100 --output-model Model/otherproject2/bf_openoffice_model100 --num-threads 16
mallet train-topics --input InputDocs/otherproject2/bf_libreoffice.mallet --num-topics 100 --optimize-interval 20 --output-topic-keys LDA/otherproject2/bf_libreoffice_words100.csv --output-doc-topics LDA/otherproject2/bf_libreoffice_dist100.csv --inferencer-filename Inferencer/otherproject2/bf_libreoffice_infer100 --output-model Model/otherproject2/bf_libreoffice_model100 --num-threads 16
mallet train-topics --input InputDocs/otherproject2/bf_itext.mallet --num-topics 100 --optimize-interval 20 --output-topic-keys LDA/otherproject2/bf_itext_words100.csv --output-doc-topics LDA/otherproject2/bf_itext_dist100.csv --inferencer-filename Inferencer/otherproject2/bf_itext_infer100 --output-model Model/otherproject2/bf_itext_model100 --num-threads 16
mallet train-topics --input InputDocs/otherproject2/bf_jasperserver.mallet --num-topics 100 --optimize-interval 20 --output-topic-keys LDA/otherproject2/bf_jasperserver_words100.csv --output-doc-topics LDA/otherproject2/bf_jasperserver_dist100.csv --inferencer-filename Inferencer/otherproject2/bf_jasperserver_infer100 --output-model Model/otherproject2/bf_jasperserver_model100 --num-threads 16
mallet train-topics --input InputDocs/otherproject2/bf_jbossserver.mallet --num-topics 100 --optimize-interval 20 --output-topic-keys LDA/otherproject2/bf_jbossserver_words100.csv --output-doc-topics LDA/otherproject2/bf_jbossserver_dist100.csv --inferencer-filename Inferencer/otherproject2/bf_jbossserver_infer100 --output-model Model/otherproject2/bf_jbossserver_model100 --num-threads 16
