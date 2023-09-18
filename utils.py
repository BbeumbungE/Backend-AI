import tensorflow as tf

def preprocess_edge(edge_img):
    edge_img = tf.cast(edge_img, tf.float32)
    edge_img = edge_img / 255.0
    edge_img = tf.clip_by_value(edge_img, 0, 1)
    edge_img = tf.expand_dims(edge_img, axis=0)

    return edge_img

def postprocess_result(result):
    result = (result + 1) * 127.5
    result = tf.cast(result, tf.int32)
    result = tf.clip_by_value(result, 0, 255)

    # batch dim 제거
    if len(result.shape) == 3:
        return result
    elif len(result.shape) == 4:
        return result[0]