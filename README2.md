1. creata_data.ipynb
2. conver_sr.py (skip)
3. create_vocab
4. extend_embedding
5. prepare_csv_wavs.py
```
export CUDA_VISIBLE_DEVICES="6,7,4,0,1"
accelerate launch \
  /home/pham/F5-TTS-Vietnamese/src/f5_tts/train/finetune_cli.py \
  --exp_name F5TTS_v1_Base \
  --learning_rate 1e-05 \
  --batch_size_per_gpu 16 \
  --batch_size_type sample \
  --max_samples 64 \
  --grad_accumulation_steps 4 \
  --max_grad_norm 1 \
  --epochs 10 \
  --num_warmup_updates 100 \
  --save_per_updates 500 \
  --keep_last_n_checkpoints -1 \
  --last_per_updates 100 \
  --dataset_name vivoice_p1 \
  --finetune \
  --pretrain /home/pham/F5-TTS-Vietnamese/ckpts/vivoice_p1/pretrained_model_1200000.pt \
  --tokenizer char \
  --log_samples \
  --logger wandb
```
40p 1 epoch