# shitAI0
plastic + extra detection for garbagePenny

## Preparing the image data sets

In order to start the transfer learning process, a folder named training_dataset needs to be created in the root of the project folder. This folder will contain the image data sets for all the subjects, for whom the classification is to be performed. A zip file is included for convinence.

## Initiate transfer learning
 
Go to the project directory and run -

```javascript
$ bash train.sh
```
This script installs the ``Inception`` model and initiates the re-training process for the specified image data sets.

Once the process is complete, it will return a training accuracy somewhere between ``85% - 100%``.

The ``training summaries``, ``retrained graphs`` and ``retrained labels`` will be saved in a folder named ``tf_files``.


https://colab.research.google.com/drive/1Zl7HJ3xNjDsD6iqjbP-YWZLy65PdbyZG#scrollTo=I-98E1sleZHn
