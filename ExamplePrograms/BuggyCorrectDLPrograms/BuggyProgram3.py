import time
start = time.time()
try:
    import resource
    import numpy as np
    import tensorflow as tf
    from tensorflow import keras
    # import keras
    from tensorflow.keras import layers
    #from tensorflow.python.keras.callbacks import History
    from tensorflow.keras import backend as k
    #from tensorflow.python.keras import backend as K
    import resource

    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
    x_train = x_train.astype("float32")/255
    x_test = x_test.astype("float32")/255
    x_train = np.expand_dims(x_train, -1)
    x_test = np.expand_dims(x_test, -1)
    y_train = keras.utils.to_categorical(y_train, 10)
    y_test = keras.utils.to_categorical(y_test, 10)
    model = keras.Sequential([
            keras.Input(shape=(28, 28, 1)),
            layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
            layers.MaxPooling2D(pool_size=(2, 2)),
            layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
            layers.Flatten(),
            layers.Dropout(0.5),
            layers.Dense(10, activation="softmax"),])
    model.compile(loss="binary_crossentropy", optimizer="adam",
                  metrics=["accuracy"])
    #tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir="./logs")
    model.fit(x_train, y_train, batch_size=128, epochs=5, validation_split=0.1)
    score = model.evaluate(x_test, y_test, verbose=0)

finally:
    end  =time.time()
    time_elapsed = end-start
    print(end-start)
    memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
    print("%5.1f secs %5.1f MByte" % (time_elapsed, memMb))
