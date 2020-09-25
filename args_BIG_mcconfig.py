import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='SMART-Vocoder', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--data_path', type=str, default='datasets/preprocessed_44kHz', help='Dataset path')
    parser.add_argument('--model_name', type=str, default='SmartVocoder', help='Model name')
    parser.add_argument('--load_step', type=int, default=0, help='Load step')
    parser.add_argument('--epochs', '-e', type=int, default=5000, help='Number of epochs to train.')
    parser.add_argument('--bsz', '-b', type=int, default=24, help='Batch size')
    parser.add_argument('--bsz_init', '-bi', type=int, default=128, help='Batch size for initializing actnorm')
    parser.add_argument('--lr', type=float, default=5e-4, help='Learning rate')
    parser.add_argument('--step_size', type=int, default=50000, help='Step size of optimizer scheduler')
    parser.add_argument('--gamma', type=float, default=0.5, help='Decay ratio of learning rate')
    parser.add_argument('--num_workers', type=int, default=0, help='Number of workers')
    parser.add_argument('--log_interval', type=int, default=100, help='Logging interval during training')
    parser.add_argument('--synth_interval', type=int, default=250, help='Sampling interval during training')
    parser.add_argument('--num_sample', type=int, default=1, help='Number of samples to synthesize during training')

    parser.add_argument('--world_size', default=1, type=int,
                        help='Number of distributed nodes.')
    parser.add_argument('--dist_url', default='tcp://127.0.0.1:9998', type=str,
                        help='url used to set up distributed training')
    parser.add_argument('--dist_backend', default='nccl', type=str,
                        help='distributed backend')
    parser.add_argument('--distributed', action='store_true',
                        help='Use multi-processing distributed training to launch '
                             'N processes per node, which has N GPUs. This is the '
                             'fastest way to use PyTorch for either single node or '
                             'multi node data parallel training')
    parser.add_argument('--rank', default=0, type=int,
                        help='node rank for distributed training')
    parser.add_argument('--gpu', default=None, type=int,
                        help='GPU id to use. None means using all available GPUs.')

    parser.add_argument('--max_time_steps', type=int, default=16000, help='Maximum time steps of audio for training')
    parser.add_argument('--sr', type=int, default=22050, help='Sampling rate')
    parser.add_argument('--hop_length', type=int, default=256, help='Hop length')

    parser.add_argument('--sqz_scale_i', type=int, default=4, help='Initial squeeze scale (do not change the value)')
    parser.add_argument('--sqz_scale', type=int, default=4, help='Squeeze scale between Equal Resolution blocks (sqz_scale shuold be 4)')
    parser.add_argument('--n_ER_blocks', type=int, default=4, help='Number of Equal Resolution blocks')
    parser.add_argument('--n_flow_blocks', type=int, default=5, help='Number of flow blocks in Equal Resolution block')
    parser.add_argument('--n_layers', type=list, default=[8, 8, 8, 8], help='Number of layers in WaveNet')
    parser.add_argument('--di_cycle', type=list, default=[8, 6, 4, 2], help='Dilation cycle in WaveNet')
    parser.add_argument('--n_channels', type=int, default=128, help='Number of channels in WaveNet')

    # for snthesize.py
    parser.add_argument('--temp', type=float, default=0.6, help='Temperature')
    parser.add_argument('--num_synth', type=int, default=10, help='Number of samples to synthesize')

    args = parser.parse_args()

    return args
