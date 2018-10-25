def convert(imgf, outf, n):
    f = open(imgf, "rb")
    o = open(outf, "w")

    f.read(16)
    images = []
    image = []

    for i in range(n):
        for j in range(28 * 28):
            image.append(ord(f.read(1)))
        images.append(image)

    for image in images:
        o.write(",".join(str(pix) for pix in image) + "\n")
    f.close()
    o.close()


convert("MNIST_data/train-images.idx3-ubyte", "mnist_train_image.csv", 60000)
convert("MNIST_data/t10k-images.idx3-ubyte", "mnist_test_image.csv", 10000)

print("Convert Finished!")