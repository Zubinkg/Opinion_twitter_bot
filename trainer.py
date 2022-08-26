import gpt_2_simple as gpt2

gpt2.download_gpt2()

sess = gpt2.start_tf_sess()
gpt2.finetune(sess, model_name='124M', dataset='training.txt', steps=50)  #specify number of steps my modifying steps parameter

gpt2.generate(sess)