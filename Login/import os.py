import os
for dirname, _, filenames in os.walk('/kaggle/input/llama-2/pytorch/13b/1/'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
