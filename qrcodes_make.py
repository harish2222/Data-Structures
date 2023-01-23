import tensorflow as tf
import qrcode
z = input("Input the url or anything that you want to access it with qrcode:\t")
y = input("Enter the file_name:\t")
x = qrcode.make(z)
x.save(y+".jpg")
a = tf.constant(234,tf.int64)
print(tf.config.list_physical_devices())
print(a)
