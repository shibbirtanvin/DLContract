import math

from pyparsing import Or
import tensorflow as tf
import numpy as np

class Gradient():
    def __init__(self, where=None):
        #Contract.__init__(self, where)
        pass
    gradient_list = []
    def gradient_zero_ratio(gradient_list):
        kernel = []
        bias = []
        total_zero = 0
        total_size = 0
        for i in range(len(gradient_list)):
            zeros = np.sum(gradient_list[i] == 0)
            total_zero += zeros
            total_size += len(gradient_list[i])
            if i % 2 == 0:
                kernel.append(zeros / len(gradient_list[i]))
            else:
                bias.append(zeros / len(gradient_list[i]))
        total = float(total_zero) / float(total_size)
        return total

 #   @tf.function
    def get_gradient(x, y, model, loss_fn):
        with tf.GradientTape() as tape:
            #logits = model(x, training=True)
            logits = model(x)
            loss_value = loss_fn(y, logits)
        grads = tape.gradient(loss_value, model.trainable_weights)

        # optimizer.apply_gradients(zip(grads, model.trainable_weights))
        # train_acc_metric.update_state(y, logits)
        return loss_value, grads

    def gradient_norm(gradient_list):
        assert len(gradient_list) % 2 == 0
        norm_kernel_list = []
        norm_bias_list = []
        for i in range(int(len(gradient_list) / 2)):
            # average_kernel_list.append(np.mean(np.abs(gradient_list[2*i])))
            # average_bias_list.append(np.mean(np.abs(gradient_list[2*i+1])))
            norm_kernel_list.append(np.linalg.norm(np.array(gradient_list[2 * i])))
            norm_bias_list.append(np.linalg.norm(np.array(gradient_list[2 * i + 1])))
        return norm_kernel_list, norm_bias_list

    def check_contract(self, context, value, silent):
        pass

    def __str__(self):
        return ''

    def __repr__(self):
        return 'Gradient'
