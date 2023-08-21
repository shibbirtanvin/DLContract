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

#    @tf.function
    def get_gradient(x, y, model, loss_fn):
        with tf.GradientTape() as tape:
            logits = model(x, training=True)
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

class LastLayer():
    def __init__(self, where=None):
        #Contract.__init__(self, where)
        pass
    #get last layer object
    def get_last_layer(model):
        last_layer=model.layers[len(model.layers) - 1]
        return last_layer
    # get last layer activation function
    def get_last_layer_activation(model):
        activation_func= str(model.layers[len(model.layers) - 1].__getattribute__('activation')).split()[1]
        return activation_func
    # get last layer input_shape
    def get_last_layer_input_shape(model):
        input_shape=model.layers[len(model.layers) - 1].input_shape
        return input_shape
    # get output class from last layer
    def get_last_layer_output_class(model):
        try:
            output_class=int(str((model.layers[len(model.layers) - 1]).output_shape).split(',').pop(-1).strip(')'))
        except AttributeError:
            try:
                output_class = model.layers[len(model.layers) - 1].units
            except AttributeError:
                output_class =1
        return output_class
    #get last layer weight
    def get_last_layer_weight(model):
        weight_last_layer = model.layers[len(model.layers) - 1].get_weights()
        return weight_last_layer

    def check_contract(self, context, value, silent):
        pass

    def __str__(self):
        return ''

    def __repr__(self):
        return 'LastLayer'

class InBetweenlayers():
    def __init__(self, where=None):
        # Contract.__init__(self, where)
        pass
    def get_all_layers_object(model):
        layers_list=[]
        for idx in range(model.layers.__len__()):
            try:
                layers_list.append(str(model.layers[idx]))
            except AttributeError:
                pass
        return layers_list
    def get_all_layers_name(model):
        layer_names=[layer.name for layer in model.layers]
        return layer_names
    def get_layers_index(model, layerName):
        index = None
        for idx, layer in enumerate(model.layers):
            if layer.name == layerName:
                index = idx
        return index
    def check_if_exists(model, x):
        layer_all = [layer.name for layer in model.layers]
        print(layer_all)
        if x in layer_all:
            print(str(x) + 'layer is inside the layers')
        else:
            print(str(x) + ' is not present in the layers')

    def get_dropout_layer(model):
        dropout_layer=''
        for idx in range(model.layers.__len__()):
            try:
                if ('Dropout' in str(model.layers[idx])):
                    dropout_layer = model.layers[idx]
                    #print(dropout_layer.rate)
            except AttributeError:
                pass
        return dropout_layer

    def get_activation_all_layers(model):
        activation_list=[]
        for idx in range(model.layers.__len__()):
            try:
                activation_list.append(str(model.layers[idx].__getattribute__('activation')).split()[1])
            except AttributeError:
                pass
        return activation_list

    def check_contract(self, context, value, silent):
        pass

    def __str__(self):
        return 'Between Layer'

    def __repr__(self):
        return 'Between Layer'


class FirstLayer():
    def __init__(self, where=None):
        #Contract.__init__(self, where)
        pass

    def check_contract(self, context, value, silent):
        pass

    def __str__(self):
        return 'First Layer'

    def __repr__(self):
        return 'FirstLayer'

class CompiledModel():
    def __init__(self, where=None):
        #Contract.__init__(self, where)
        pass
    def get_loss_value(model):
        return model.compiled_loss._losses

    def check_contract(self, context, value, silent):
        pass

    def __str__(self):
        return 'Compiled Model'

    def __repr__(self):
        return 'Compiled Model'

class ModelInputShape():
    def __init__(self, where=None):
        #Contract.__init__(self, where)
        pass
    def get_input_shape_first_layer(model):
        try:
            input_shape = str(model.layers[0].input_shape)
            const1 = (input_shape.split(",")[1:input_shape.__len__()])
        except AttributeError:
            const1 = ''
        return const1

    def check_contract(self, context, value, silent):
        pass

    def __str__(self):
        return 'Model Input Shape'

    def __repr__(self):
        return 'Model Input Shape'

class LastLayer_1():
    def __init__(self, where=None):
        #Contract.__init__(self, where)
        pass
    #get last layer object
    def get_last_layer_1(model):
        last_layer_1=model.layers[len(model.layers) - 2]
        return last_layer_1
    # get last layer activation function
    def get_last_layer_1_activation(model):
        activation_func= str(model.layers[len(model.layers) - 2].__getattribute__('activation')).split()[1]
        return activation_func
    # get last layer input_shape
    def get_last_layer_1_input_shape(model):
        input_shape=model.layers[len(model.layers) - 2].input_shape
        return input_shape
    # get output class from last layer
    def get_last_layer_1_output_class(model):
        try:
            output_class=int(str((model.layers[len(model.layers) - 2]).output_shape).split(',').pop(-1).strip(')'))
        except AttributeError:
            try:
                output_class = model.layers[len(model.layers) - 2].units
            except AttributeError:
                output_class =1
        return output_class
    #get last layer weight
    def get_last_layer_1_weight(model):
        weight_last_layer = model.layers[len(model.layers) - 2].get_weights()
        return weight_last_layer

    def check_contract(self, context, value, silent):
        pass

    def __str__(self):
        return ''

    def __repr__(self):
        return 'LastLayer_1'


class LastLayer_2():
    def __init__(self, where=None):
        #Contract.__init__(self, where)
        pass
    #get last layer object
    def get_last_layer_2(model):
        last_layer_2=model.layers[len(model.layers) - 3]
        return last_layer_2
    # get last layer activation function
    def get_last_layer_2_activation(model):
        activation_func= str(model.layers[len(model.layers) - 3].__getattribute__('activation')).split()[1]
        return activation_func
    # get last layer input_shape
    def get_last_layer_2_input_shape(model):
        input_shape=model.layers[len(model.layers) - 3].input_shape
        return input_shape
    # get output class from last layer
    def get_last_layer_2_output_class(model):
        try:
            output_class=int(str((model.layers[len(model.layers) - 3]).output_shape).split(',').pop(-1).strip(')'))
        except AttributeError:
            try:
                output_class = model.layers[len(model.layers) - 3].units
            except AttributeError:
                output_class =1
        return output_class
    #get last layer weight
    def get_last_layer_2_weight(model):
        weight_last_layer = model.layers[len(model.layers) - 3].get_weights()
        return weight_last_layer

    def check_contract(self, context, value, silent):
        pass

    def __str__(self):
        return ''

    def __repr__(self):
        return 'LastLayer_2'

class LastLayer_3():
    def __init__(self, where=None):
        #Contract.__init__(self, where)
        pass
    #get last layer object
    def get_last_layer_3(model):
        last_layer_3=model.layers[len(model.layers) - 4]
        return last_layer_3
    # get last layer activation function
    def get_last_layer_3_activation(model):
        activation_func= str(model.layers[len(model.layers) - 4].__getattribute__('activation')).split()[1]
        return activation_func
    # get last layer input_shape
    def get_last_layer_3_input_shape(model):
        input_shape=model.layers[len(model.layers) - 4].input_shape
        return input_shape
    # get output class from last layer
    def get_last_layer_3_output_class(model):
        try:
            output_class=int(str((model.layers[len(model.layers) - 4]).output_shape).split(',').pop(-1).strip(')'))
        except AttributeError:
            try:
                output_class = model.layers[len(model.layers) - 4].units
            except AttributeError:
                output_class =1
        return output_class
    #get last layer weight
    def get_last_layer_3_weight(model):
        weight_last_layer = model.layers[len(model.layers) - 4].get_weights()
        return weight_last_layer

    def check_contract(self, context, value, silent):
        pass

    def __str__(self):
        return ''

    def __repr__(self):
        return 'LastLayer_2'
